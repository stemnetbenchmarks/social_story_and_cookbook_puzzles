# visual_novel_browser_server.py
import argparse
import http.server
import json
import mimetypes
import re
import socketserver
import sys
import traceback
import urllib.parse
from pathlib import Path

"""
visual_novel_browser_server.py
==============================

Visual Novel Browser Server, version 1.

A minimal local-only HTTP server that exposes a directory tree of game logs
to a browser-based visual novel viewer. The viewer polls this server every
few seconds for the most recent round of play and renders, in three stacked
layers:

    Layer 1 (background) : solid black
    Layer 2 (figures)    : a player avatar image on the left column,
                           and the player's ASCII POV map on the right column
                           (rendered in a monospaced font).
    Layer 3 (dialogue)   : a dialogue / memo box across the bottom showing
                           the player's action summary and note_share_memo.

This server uses ONLY the Python standard library. No third-party
dependencies are imported anywhere in this file.

Design notes
------------
- The HTTP handler subclass is the only class. All meaningful logic lives
  in module-level pure functions, which makes them easy to unit-test and
  reason about independently of the HTTP transport.
- Every API request re-scans the configured logs directory. There is no
  in-memory cache and no filesystem watcher. The volume of files per
  round is small and this is a single-user local tool, so the simplicity
  is preferable to the complexity of cache invalidation.
- Path traversal is defended against in `serve_static_file_under_root`
  by resolving the requested path and verifying it lies inside the
  configured static root directory.
- All configuration (paths, port) comes from command-line arguments.
  No environment-specific values are hard-coded.

Run
---
    python visual_novel_browser_server.py \\
        --logs-root-directory ./logs \\
        --web-root-directory ./web \\
        --vn-images-root-directory ./vn_images \\
        --listen-port 8765

Then open  http://127.0.0.1:8765/  in a browser.
"""

# ---------------------------------------------------------------------------
# Filename pattern constants
# ---------------------------------------------------------------------------
# These regular expressions are used with re.fullmatch() so that any file
# whose name does not match the exact expected schema is ignored rather
# than mis-parsed. Anchoring the patterns avoids partial-match bugs.

GAME_DIRECTORY_NAME_PATTERN = re.compile(r"game_\d{8}_\d{6}")

ROUND_DIRECTORY_NAME_PATTERN = re.compile(r"round_(?P<round_number>\d+)")

PLAYER_LOG_FILENAME_PATTERN = re.compile(
    r"playerlog_(?P<log_timestamp>\d{8}_\d{6})_(?P<player_id>[A-Za-z0-9]+)\.json"
)

PLAYER_POV_MAP_FILENAME_PATTERN = re.compile(
    r"gm_(?P<player_id>[A-Za-z0-9]+)_pov_map_(?P<map_timestamp>\d{8}_\d{6,})\.txt"
)

GENERIC_ROUND_MAP_FILENAME_PATTERN = re.compile(
    r"gm_generic_round_dungeon_so_far_(?P<map_timestamp>\d{8}_\d{6,})\.txt"
)

# The per-game start state file. It lives directly inside a game directory
# and contains the mapping from player name (a, b, c, ...) to element
# (ice, fire, water, ...). The element is what selects the avatar image,
# because element-to-player assignment is randomized per game.
START_STATE_FILENAME = "start_state.json"

# ---------------------------------------------------------------------------
# Element Images
# ---------------------------------------------------------------------------

def find_start_state_file_in_game_directory(
    game_directory: Path,
) -> Path | None:
    """
    Return the path to the 'start_state.json' file directly inside
    game_directory, or None if it is not present.

    The start state file contains the mapping from player name (the same
    short identifier 'a', 'b', 'c', ... used in playerlog filenames) to
    the player's element ('ice', 'fire', 'water', ...). The element is
    used to choose the avatar image, since element-to-player assignment
    is randomized at game start and cannot be hard-coded.

    Parameters
    ----------
    game_directory : Path
        A specific 'game_YYYYMMDD_HHMMSS' directory.

    Returns
    -------
    Path | None
        Path to the start_state.json file, or None if missing.

    Raises
    ------
    FileNotFoundError
        If game_directory itself does not exist.
    NotADirectoryError
        If game_directory is not a directory.
    """
    if not game_directory.exists():
        raise FileNotFoundError(
            f"Game directory does not exist: {game_directory}"
        )
    if not game_directory.is_dir():
        raise NotADirectoryError(
            f"Game path is not a directory: {game_directory}"
        )

    candidate_start_state_path = game_directory / START_STATE_FILENAME
    if not candidate_start_state_path.is_file():
        return None
    return candidate_start_state_path


def parse_player_id_to_element_mapping_from_start_state(
    start_state_file_path: Path,
) -> dict[str, str]:
    """
    Read 'start_state.json' and return a dict mapping each player_id
    (the 'name' field, e.g. 'a', 'b', 'c') to its element string
    (e.g. 'ice', 'fire', 'water', 'forest', 'void').

    Source structure
    ----------------
    The relevant subtree of the file looks like this:

        {
            "object_state": {
                "player_character_state": {
                    "3": { "name": "e", "element": "forest", ... },
                    "4": { "name": "b", "element": "void",   ... },
                    ...
                }
            }
        }

    The integer-string keys ('3', '4', ...) are character slot ids in
    the source system and are NOT the player_id used by the viewer. We
    intentionally key the returned mapping by the 'name' field so that
    callers can look up by the same player_id used in playerlog
    filenames.

    Players whose entry is missing 'name' or 'element' are skipped with
    a warning to stderr rather than raising, because the visual novel
    viewer should still render whatever data is available.

    Parameters
    ----------
    start_state_file_path : Path
        Path to a 'start_state.json' file.

    Returns
    -------
    dict[str, str]
        Mapping from player_id (str) to element (str). Empty dict if no
        usable entries were found.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    json.JSONDecodeError
        If the file is not valid JSON.
    KeyError
        If the expected 'object_state' / 'player_character_state'
        subtree is entirely absent (this is a structural error in the
        source file and is worth surfacing loudly).
    """
    raw_start_state_text: str = read_utf8_text_file_contents(start_state_file_path)
    parsed_start_state_object: dict = json.loads(raw_start_state_text)

    object_state_subobject = parsed_start_state_object.get("object_state")
    if not isinstance(object_state_subobject, dict):
        raise KeyError(
            f"start_state.json is missing 'object_state' object: "
            f"{start_state_file_path}"
        )
    player_character_state_subobject = object_state_subobject.get(
        "player_character_state"
    )
    if not isinstance(player_character_state_subobject, dict):
        raise KeyError(
            f"start_state.json is missing "
            f"'object_state.player_character_state' object: "
            f"{start_state_file_path}"
        )

    assembled_player_id_to_element_mapping: dict[str, str] = {}
    for character_slot_id_string, character_state_object in (
        player_character_state_subobject.items()
    ):
        if not isinstance(character_state_object, dict):
            sys.stderr.write(
                f"[vn-browser] Skipping non-object character entry at "
                f"slot {character_slot_id_string!r} in "
                f"{start_state_file_path}\n"
            )
            continue
        player_id_value = character_state_object.get("name")
        element_value = character_state_object.get("element")
        if not isinstance(player_id_value, str) or not isinstance(element_value, str):
            sys.stderr.write(
                f"[vn-browser] Skipping character entry at slot "
                f"{character_slot_id_string!r} in {start_state_file_path}: "
                f"missing or non-string 'name' or 'element' "
                f"(name={player_id_value!r}, element={element_value!r})\n"
            )
            continue
        assembled_player_id_to_element_mapping[player_id_value] = element_value

    return assembled_player_id_to_element_mapping


# ---------------------------------------------------------------------------
# File discovery functions
# ---------------------------------------------------------------------------

def find_latest_game_directory(logs_root_directory: Path) -> Path | None:
    """
    Return the most recent 'game_YYYYMMDD_HHMMSS' subdirectory of
    logs_root_directory, or None if no such subdirectory exists.

    Selection rule
    --------------
    Game directories use zero-padded timestamps, so plain lexicographic
    sorting of their names is equivalent to chronological sorting. The
    last entry after sort is therefore the most recent.

    Parameters
    ----------
    logs_root_directory : Path
        The directory expected to contain one or more
        'game_YYYYMMDD_HHMMSS' subdirectories.

    Returns
    -------
    Path | None
        Path to the latest matching game directory, or None if there are
        no matching subdirectories.

    Raises
    ------
    FileNotFoundError
        If logs_root_directory does not exist.
    NotADirectoryError
        If logs_root_directory exists but is not a directory.
    """
    if not logs_root_directory.exists():
        raise FileNotFoundError(
            f"Logs root directory does not exist: {logs_root_directory}"
        )
    if not logs_root_directory.is_dir():
        raise NotADirectoryError(
            f"Logs root path is not a directory: {logs_root_directory}"
        )

    candidate_game_directories: list[Path] = [
        directory_entry
        for directory_entry in logs_root_directory.iterdir()
        if directory_entry.is_dir()
        and GAME_DIRECTORY_NAME_PATTERN.fullmatch(directory_entry.name)
    ]

    if not candidate_game_directories:
        return None

    candidate_game_directories.sort(key=lambda directory: directory.name)
    return candidate_game_directories[-1]


def find_latest_round_directory(game_directory: Path) -> Path | None:
    """
    Return the 'round_N' subdirectory of game_directory with the highest N,
    or None if there are no round subdirectories.

    Selection rule
    --------------
    The integer N is parsed from the directory name and used as the sort
    key so that 'round_10' is correctly ordered after 'round_2'.

    Parameters
    ----------
    game_directory : Path
        A specific 'game_YYYYMMDD_HHMMSS' directory.

    Returns
    -------
    Path | None
        Path to the latest round directory, or None if none exist.

    Raises
    ------
    FileNotFoundError
        If game_directory does not exist.
    NotADirectoryError
        If game_directory is not a directory.
    """
    if not game_directory.exists():
        raise FileNotFoundError(
            f"Game directory does not exist: {game_directory}"
        )
    if not game_directory.is_dir():
        raise NotADirectoryError(
            f"Game path is not a directory: {game_directory}"
        )

    parsed_round_directories: list[tuple[int, Path]] = []
    for directory_entry in game_directory.iterdir():
        if not directory_entry.is_dir():
            continue
        round_match = ROUND_DIRECTORY_NAME_PATTERN.fullmatch(directory_entry.name)
        if round_match is None:
            continue
        round_number_as_integer = int(round_match.group("round_number"))
        parsed_round_directories.append((round_number_as_integer, directory_entry))

    if not parsed_round_directories:
        return None

    parsed_round_directories.sort(key=lambda pair: pair[0])
    return parsed_round_directories[-1][1]


def list_player_log_files_in_chronological_order(
    round_directory: Path,
) -> list[Path]:
    """
    Return all 'playerlog_YYYYMMDD_HHMMSS_<player_id>.json' files in the
    given round_directory, sorted by the embedded timestamp ascending
    (oldest first). This represents the order in which players took
    their turns this round.

    Parameters
    ----------
    round_directory : Path
        A specific 'round_N' directory.

    Returns
    -------
    list[Path]
        Possibly empty list of player log file paths.

    Raises
    ------
    FileNotFoundError
        If round_directory does not exist.
    NotADirectoryError
        If round_directory is not a directory.
    """
    if not round_directory.exists():
        raise FileNotFoundError(
            f"Round directory does not exist: {round_directory}"
        )
    if not round_directory.is_dir():
        raise NotADirectoryError(
            f"Round path is not a directory: {round_directory}"
        )

    matched_player_log_files: list[Path] = []
    for directory_entry in round_directory.iterdir():
        if not directory_entry.is_file():
            continue
        if PLAYER_LOG_FILENAME_PATTERN.fullmatch(directory_entry.name):
            matched_player_log_files.append(directory_entry)

    # The timestamp is at fixed positions within the filename so a plain
    # lexicographic sort of the filename gives correct chronological order.
    matched_player_log_files.sort(key=lambda file_path: file_path.name)
    return matched_player_log_files


def find_player_pov_map_file_for_player(
    round_directory: Path,
    player_id: str,
) -> Path | None:
    """
    Return the path to the gm_<player_id>_pov_map_<timestamp>.txt file in
    round_directory, or None if no such file exists.

    If multiple POV map files are present for the same player_id (which
    should not normally happen) the lexicographically last one is
    returned, which is also the chronologically last because timestamps
    are zero-padded.

    Parameters
    ----------
    round_directory : Path
        A specific 'round_N' directory.
    player_id : str
        The player identifier used as the second token in the filename
        (for example 'a', 'b', 'c').

    Returns
    -------
    Path | None
        Matching POV map file, or None.
    """
    matching_pov_map_files: list[Path] = []
    for directory_entry in round_directory.iterdir():
        if not directory_entry.is_file():
            continue
        filename_match = PLAYER_POV_MAP_FILENAME_PATTERN.fullmatch(
            directory_entry.name
        )
        if filename_match is None:
            continue
        if filename_match.group("player_id") == player_id:
            matching_pov_map_files.append(directory_entry)

    if not matching_pov_map_files:
        return None

    matching_pov_map_files.sort(key=lambda file_path: file_path.name)
    return matching_pov_map_files[-1]


def find_generic_round_map_file(round_directory: Path) -> Path | None:
    """
    Return the path to the gm_generic_round_dungeon_so_far_<timestamp>.txt
    file in round_directory, or None if no such file exists.

    Parameters
    ----------
    round_directory : Path
        A specific 'round_N' directory.

    Returns
    -------
    Path | None
        Matching generic round map file, or None.
    """
    matching_generic_map_files: list[Path] = []
    for directory_entry in round_directory.iterdir():
        if not directory_entry.is_file():
            continue
        if GENERIC_ROUND_MAP_FILENAME_PATTERN.fullmatch(directory_entry.name):
            matching_generic_map_files.append(directory_entry)

    if not matching_generic_map_files:
        return None

    matching_generic_map_files.sort(key=lambda file_path: file_path.name)
    return matching_generic_map_files[-1]


# ---------------------------------------------------------------------------
# Text and JSON reading helpers
# ---------------------------------------------------------------------------

def read_utf8_text_file_contents(file_path: Path) -> str:
    """
    Read a text file as UTF-8 and return its contents as a string.

    Parameters
    ----------
    file_path : Path
        File to read.

    Returns
    -------
    str
        File contents.

    Raises
    ------
    FileNotFoundError
        If file_path does not exist.
    OSError
        For other read failures (permissions, etc.).
    UnicodeDecodeError
        If the file is not valid UTF-8.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Text file does not exist: {file_path}")
    if not file_path.is_file():
        raise OSError(f"Text path is not a regular file: {file_path}")
    with file_path.open(mode="r", encoding="utf-8") as opened_text_file:
        return opened_text_file.read()


def parse_player_log_json_file(player_log_file_path: Path) -> dict:
    """
    Read and parse a playerlog_*.json file and return only the fields that
    the visual novel viewer is expected to display.

    Selected fields
    ---------------
    The returned dict has the following shape (any missing source fields
    are represented as None so the viewer can render placeholders):

        {
            "log_timestamp"     : str  | None,   # from top-level "timestamp"
            "player_id"         : str  | None,
            "action_type"       : str  | None,
            "move_from_coord"   : list | None,
            "move_to_coord"     : list | None,
            "start_round_vote"  : bool | None,
            "note_share_memo"   : str  | None,
        }

    Fields that begin with 'raw_' in the source JSON are deliberately
    excluded; they are not used in the viewer.

    Parameters
    ----------
    player_log_file_path : Path
        Path to a playerlog_*.json file.

    Returns
    -------
    dict
        Display-only subset of the player log.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    json.JSONDecodeError
        If the file is not valid JSON.
    """
    raw_json_text_contents: str = read_utf8_text_file_contents(
        player_log_file_path
    )
    parsed_player_log_object: dict = json.loads(raw_json_text_contents)

    extracted_data_subobject: dict = parsed_player_log_object.get(
        "extracted_data", {}
    ) or {}
    action_dict_subobject: dict = extracted_data_subobject.get(
        "action_dict", {}
    ) or {}

    display_subset: dict = {
        "log_timestamp": parsed_player_log_object.get("timestamp"),
        "player_id": parsed_player_log_object.get("player_id"),
        "action_type": action_dict_subobject.get("action_type"),
        "move_from_coord": action_dict_subobject.get("move_from_coord"),
        "move_to_coord": action_dict_subobject.get("move_to_coord"),
        "start_round_vote": extracted_data_subobject.get("start_round_vote"),
        "note_share_memo": extracted_data_subobject.get("note_share_memo"),
    }
    return display_subset


# ---------------------------------------------------------------------------
# Top-level payload assembly
# ---------------------------------------------------------------------------

def find_all_round_directories_in_sorted_order(game_directory: Path) -> list[Path]:
    """
    Return all 'round_N' subdirectories of game_directory sorted by N
    ascending (round_1 first, round_10 after round_9, etc).

    The sort key is the parsed integer N, not the directory name string,
    so that natural numeric order is preserved regardless of zero-padding.

    Parameters
    ----------
    game_directory : Path
        A specific 'game_YYYYMMDD_HHMMSS' directory.

    Returns
    -------
    list[Path]
        Possibly empty list of round directory paths in round-number order.

    Raises
    ------
    FileNotFoundError
        If game_directory does not exist.
    NotADirectoryError
        If game_directory is not a directory.
    """
    if not game_directory.exists():
        raise FileNotFoundError(
            f"Game directory does not exist: {game_directory}"
        )
    if not game_directory.is_dir():
        raise NotADirectoryError(
            f"Game path is not a directory: {game_directory}"
        )

    parsed_round_directories: list[tuple[int, Path]] = []
    for directory_entry in game_directory.iterdir():
        if not directory_entry.is_dir():
            continue
        round_name_match = ROUND_DIRECTORY_NAME_PATTERN.fullmatch(
            directory_entry.name
        )
        if round_name_match is None:
            continue
        round_number_as_integer = int(round_name_match.group("round_number"))
        parsed_round_directories.append((round_number_as_integer, directory_entry))

    parsed_round_directories.sort(key=lambda number_and_path: number_and_path[0])
    return [directory_path for _, directory_path in parsed_round_directories]


def build_all_rounds_data_payload(logs_root_directory: Path) -> dict:
    """
    Construct the JSON-serializable payload containing every round of the
    most recent game, so that the browser viewer can iterate across the
    entire game history and advance frame-by-frame as new rounds appear.

    Payload shape
    -------------
        {
            "game_directory_name"         : str | None,
            "player_id_to_element_mapping": dict[str, str],
            "all_rounds_in_sorted_order"  : [
                {
                    "round_directory_name"              : str,
                    "generic_round_map_text"            : str | None,
                    "player_turns_in_chronological_order": [
                        {
                            "log_timestamp"   : str  | None,
                            "player_id"       : str  | None,
                            "action_type"     : str  | None,
                            "move_from_coord" : list | None,
                            "move_to_coord"   : list | None,
                            "start_round_vote": bool | None,
                            "note_share_memo" : str  | None,
                            "pov_map_text"    : str  | None,
                            "element"         : str  | None,
                            "avatar_image_url": str  | None,
                        },
                        ...
                    ],
                },
                ...   (one entry per round, sorted round_1 first)
            ],
        }

    The payload includes ALL rounds found, not just the latest. The
    browser client builds a flat ordered list of "frames" from this
    structure — one frame for the generic map at the start of each round
    plus one frame per player turn — and advances through that frame list
    one step per polling cycle.

    If no game directory exists, game_directory_name is None and
    all_rounds_in_sorted_order is an empty list so the client schema is
    always stable.

    Avatar selection
    ----------------
    Avatar URLs are element-based (see parse_player_id_to_element_mapping
    _from_start_state). The mapping is read once per request from
    <game_directory>/start_state.json and applied to every round in the
    payload.

    Parameters
    ----------
    logs_root_directory : Path
        The configured logs root directory.

    Returns
    -------
    dict
        Complete payload ready for JSON serialization.
    """
    payload_being_built: dict = {
        "game_directory_name": None,
        "player_id_to_element_mapping": {},
        "all_rounds_in_sorted_order": [],
    }

    latest_game_directory_path = find_latest_game_directory(logs_root_directory)
    if latest_game_directory_path is None:
        return payload_being_built
    payload_being_built["game_directory_name"] = latest_game_directory_path.name

    # Element mapping — read once, applied to every round.
    player_id_to_element_mapping: dict[str, str] = {}
    start_state_file_path = find_start_state_file_in_game_directory(
        latest_game_directory_path
    )
    if start_state_file_path is not None:
        try:
            player_id_to_element_mapping = (
                parse_player_id_to_element_mapping_from_start_state(
                    start_state_file_path
                )
            )
        except (json.JSONDecodeError, KeyError, OSError) as start_state_error:
            sys.stderr.write(
                f"[vn-browser] Could not parse start_state.json at "
                f"{start_state_file_path}: {start_state_error!r}\n"
                f"{traceback.format_exc()}"
            )
    payload_being_built["player_id_to_element_mapping"] = (
        player_id_to_element_mapping
    )

    all_round_directory_paths = find_all_round_directories_in_sorted_order(
        latest_game_directory_path
    )

    assembled_all_rounds_list: list[dict] = []
    for single_round_directory_path in all_round_directory_paths:
        single_round_payload = _build_single_round_payload(
            round_directory=single_round_directory_path,
            player_id_to_element_mapping=player_id_to_element_mapping,
        )
        assembled_all_rounds_list.append(single_round_payload)

    payload_being_built["all_rounds_in_sorted_order"] = assembled_all_rounds_list
    return payload_being_built


def _build_single_round_payload(
    round_directory: Path,
    player_id_to_element_mapping: dict[str, str],
) -> dict:
    """
    Build the data payload for a single round directory.

    This is a private helper called once per round by
    build_all_rounds_data_payload. It is separated so that the per-round
    logic is readable and testable independently.

    Parameters
    ----------
    round_directory : Path
        A specific 'round_N' directory.
    player_id_to_element_mapping : dict[str, str]
        Mapping from player_id (e.g. 'a') to element (e.g. 'ice'),
        already parsed from start_state.json at the game level.

    Returns
    -------
    dict
        Single-round payload with keys 'round_directory_name',
        'generic_round_map_text', and
        'player_turns_in_chronological_order'.
    """
    single_round_payload: dict = {
        "round_directory_name": round_directory.name,
        "generic_round_map_text": None,
        "player_turns_in_chronological_order": [],
    }

    generic_map_file = find_generic_round_map_file(round_directory)
    if generic_map_file is not None:
        single_round_payload["generic_round_map_text"] = (
            read_utf8_text_file_contents(generic_map_file)
        )

    player_log_files_in_order = list_player_log_files_in_chronological_order(
        round_directory
    )
    assembled_player_turn_entries: list[dict] = []
    for single_player_log_file in player_log_files_in_order:
        parsed_display_subset = parse_player_log_json_file(single_player_log_file)
        player_id_from_log = parsed_display_subset.get("player_id")

        pov_map_text: str | None = None
        if player_id_from_log is not None:
            pov_map_file = find_player_pov_map_file_for_player(
                round_directory, player_id_from_log
            )
            if pov_map_file is not None:
                pov_map_text = read_utf8_text_file_contents(pov_map_file)

        element_for_this_player: str | None = None
        avatar_image_url: str | None = None
        if player_id_from_log is not None:
            element_for_this_player = player_id_to_element_mapping.get(
                player_id_from_log
            )
            if element_for_this_player is not None:
                avatar_image_url = (
                    f"/vn_images/element_avatars/"
                    f"{element_for_this_player}_avatar.png"
                )

        turn_entry = dict(parsed_display_subset)
        turn_entry["pov_map_text"] = pov_map_text
        turn_entry["element"] = element_for_this_player
        turn_entry["avatar_image_url"] = avatar_image_url
        assembled_player_turn_entries.append(turn_entry)

    single_round_payload["player_turns_in_chronological_order"] = (
        assembled_player_turn_entries
    )
    return single_round_payload


# ---------------------------------------------------------------------------
# Static file serving (with path-traversal protection)
# ---------------------------------------------------------------------------

def resolve_safe_path_under_root(
    static_root_directory: Path,
    request_relative_path: str,
) -> Path:
    """
    Resolve request_relative_path against static_root_directory and verify
    that the resolved absolute path is contained within static_root_directory.

    This prevents requests like '../../etc/passwd' from escaping the
    configured static root.

    Parameters
    ----------
    static_root_directory : Path
        The configured root directory under which static files are served.
        Must already exist.
    request_relative_path : str
        The decoded URL path component, with the route prefix already
        stripped, for example 'vn.css' or 'element_avatars/water_avatar.png'.

    Returns
    -------
    Path
        Absolute resolved path that is guaranteed to lie under
        static_root_directory.

    Raises
    ------
    PermissionError
        If the resolved path escapes static_root_directory.
    FileNotFoundError
        If static_root_directory does not exist.
    """
    if not static_root_directory.exists():
        raise FileNotFoundError(
            f"Static root directory does not exist: {static_root_directory}"
        )

    static_root_absolute = static_root_directory.resolve(strict=True)
    # Strip any leading slash so Path treats it as relative.
    sanitized_relative_path_string = request_relative_path.lstrip("/")
    candidate_absolute_path = (
        (static_root_absolute / sanitized_relative_path_string).resolve()
    )

    # Path.is_relative_to requires Python 3.9+; the project rules direct
    # us to modern Python features, so this is acceptable.
    if not candidate_absolute_path.is_relative_to(static_root_absolute):
        raise PermissionError(
            "Refusing to serve a path outside the configured static root: "
            f"requested='{request_relative_path}', "
            f"resolved='{candidate_absolute_path}', "
            f"root='{static_root_absolute}'"
        )
    return candidate_absolute_path


# ---------------------------------------------------------------------------
# HTTP request handler
# ---------------------------------------------------------------------------

class VisualNovelBrowserTCPServer(socketserver.TCPServer):
    """
    TCPServer subclass with allow_reuse_address set to True.

    allow_reuse_address instructs the OS to release the TCP port
    immediately when the server closes, rather than holding it in
    TIME_WAIT state for up to 60 seconds. Without this, re-launching
    the server shortly after Ctrl+C raises 'Address already in use'.

    This is the only reason this subclass exists. All other behaviour
    is inherited unchanged from socketserver.TCPServer.
    """
    allow_reuse_address = True

class VisualNovelBrowserRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler for the Visual Novel Browser server.

    This class is the only class in the module. It exists solely because
    the standard library's http.server expects a handler class. All real
    work is performed by module-level pure functions; the methods here
    only parse the URL and dispatch.

    Routes
    ------
        GET /                              -> web/index.html
        GET /web/<path>                    -> web/<path>     (CSS, JS, etc.)
        GET /vn_images/<path>              -> vn_images/<path>
        GET /api/latest_round              -> JSON payload of latest round
        GET /healthcheck                   -> plain-text 'ok'

    Configuration injection
    -----------------------
    The handler reads its filesystem roots from class-level attributes
    that are set by `run_server` before starting the server. This avoids
    the need for a custom factory and keeps the handler signature
    compatible with http.server.
    """

    # Class-level attributes injected by run_server before serving.
    configured_logs_root_directory: Path = Path()
    configured_web_root_directory: Path = Path()
    configured_vn_images_root_directory: Path = Path()

    # ----- logging override -----------------------------------------------
    def log_message(
        self,
        format: str,  # noqa: A002 — name must match BaseHTTPRequestHandler.log_message exactly
        *args: object,
    ) -> None:
        """
        Override the default stderr log so it is single-line and consistent.
        The parameter name 'format' is required to match the base class
        signature (http.server.BaseHTTPRequestHandler.log_message) exactly,
        which Pyright enforces via reportIncompatibleMethodOverride.
        The name shadows the built-in 'format' function within this method
        scope; that is intentional and confined to this one method.
        Production-grade logging is out of scope for v1, but the override
        prevents the noisy default two-line format from BaseHTTPRequestHandler.
        """
        sys.stderr.write(
            "[vn-browser] "
            + (format % args)
            + "\n"
        )

    # ----- HTTP method dispatch ------------------------------------------

    def do_GET(self) -> None:
        """
        Dispatch GET requests to the appropriate handler function based
        on URL path prefix. All exceptions are caught and converted to
        500 responses with a traceback included in the response body so
        that errors are obvious during local development.
        """
        try:
            parsed_request_url = urllib.parse.urlsplit(self.path)
            decoded_url_path = urllib.parse.unquote(parsed_request_url.path)

            if decoded_url_path == "/" or decoded_url_path == "/index.html":
                self.respond_with_static_file(
                    self.configured_web_root_directory,
                    "index.html",
                )
                return

            if decoded_url_path == "/healthcheck":
                self.respond_with_plain_text(200, "ok")
                return

            # if decoded_url_path == "/api/latest_round":
            #     self.respond_with_latest_round_json()
            #     return

            if decoded_url_path == "/api/game_data":
                self.respond_with_all_rounds_json()
                return

            if decoded_url_path.startswith("/web/"):
                self.respond_with_static_file(
                    self.configured_web_root_directory,
                    decoded_url_path[len("/web/"):],
                )
                return

            if decoded_url_path.startswith("/vn_images/"):
                self.respond_with_static_file(
                    self.configured_vn_images_root_directory,
                    decoded_url_path[len("/vn_images/"):],
                )
                return

            # No matching route.
            self.respond_with_plain_text(
                404,
                f"No route matches the requested path: {decoded_url_path}",
            )

        except Exception:  # noqa: BLE001 - we deliberately catch everything
            # Surface the full traceback in both the server log and the
            # HTTP response body so that local debugging is direct.
            full_traceback_text = traceback.format_exc()
            sys.stderr.write(full_traceback_text)
            try:
                self.respond_with_plain_text(
                    500,
                    "Internal server error while handling request:\n"
                    + full_traceback_text,
                )
            except Exception:  # noqa: BLE001
                # If even sending the error response fails, log and move on;
                # the connection will be closed by the framework.
                sys.stderr.write(traceback.format_exc())

    # ----- response helpers ----------------------------------------------

    def respond_with_plain_text(
        self,
        http_status_code: int,
        plain_text_body: str,
    ) -> None:
        """
        Send a UTF-8 plain-text HTTP response with the given status code
        and body.
        """
        encoded_body_bytes = plain_text_body.encode("utf-8")
        self.send_response(http_status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded_body_bytes)))
        self.end_headers()
        self.wfile.write(encoded_body_bytes)

    def respond_with_json_object(
        self,
        http_status_code: int,
        json_serializable_object: dict,
    ) -> None:
        """
        Send a UTF-8 JSON HTTP response with the given status code and body.
        """
        encoded_body_bytes = json.dumps(
            json_serializable_object,
            ensure_ascii=False,
            indent=2,
        ).encode("utf-8")
        self.send_response(http_status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded_body_bytes)))
        # Disable client caching so polling always sees fresh data.
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded_body_bytes)

    def respond_with_static_file(
        self,
        static_root_directory: Path,
        request_relative_path: str,
    ) -> None:
        """
        Serve a single static file from beneath static_root_directory.

        Sends 404 if the file is missing, 403 if the request escapes the
        configured root, and 500 for unexpected I/O errors (with traceback).
        """
        try:
            resolved_file_path = resolve_safe_path_under_root(
                static_root_directory, request_relative_path
            )
        except PermissionError as forbidden_error:
            self.respond_with_plain_text(403, str(forbidden_error))
            return
        except FileNotFoundError as missing_root_error:
            self.respond_with_plain_text(500, str(missing_root_error))
            return

        if not resolved_file_path.exists() or not resolved_file_path.is_file():
            self.respond_with_plain_text(
                404,
                f"Static file not found: /{request_relative_path}",
            )
            return

        # Guess content type from the file extension; default to octet-stream.
        guessed_content_type, _unused_encoding = mimetypes.guess_type(
            resolved_file_path.name
        )
        if guessed_content_type is None:
            guessed_content_type = "application/octet-stream"

        with resolved_file_path.open(mode="rb") as opened_binary_file:
            file_bytes = opened_binary_file.read()

        self.send_response(200)
        self.send_header("Content-Type", guessed_content_type)
        self.send_header("Content-Length", str(len(file_bytes)))
        # Static viewer assets may be cached briefly; logs and JSON are not.
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(file_bytes)

    # def respond_with_latest_round_json(self) -> None:
    #     """
    #     Build and send the latest-round JSON payload. Filesystem errors
    #     are reported as 500 with a clear, specific message.
    #     """
    #     try:
    #         latest_round_payload = build_latest_round_data_payload(
    #             self.configured_logs_root_directory
    #         )
    #     except FileNotFoundError as missing_path_error:
    #         self.respond_with_plain_text(500, str(missing_path_error))
    #         return
    #     except NotADirectoryError as not_directory_error:
    #         self.respond_with_plain_text(500, str(not_directory_error))
    #         return

    #     self.respond_with_json_object(200, latest_round_payload)

    def respond_with_all_rounds_json(self) -> None:
            """
            Build and send the full game payload (all rounds) as JSON.
            Filesystem errors are reported as 500 with a specific message.
            """
            try:
                all_rounds_payload = build_all_rounds_data_payload(
                    self.configured_logs_root_directory
                )
            except (FileNotFoundError, NotADirectoryError) as filesystem_error:
                self.respond_with_plain_text(500, str(filesystem_error))
                return

            self.respond_with_json_object(200, all_rounds_payload)
# ---------------------------------------------------------------------------
# Server entry point
# ---------------------------------------------------------------------------

def parse_command_line_arguments(
    command_line_argument_list: list[str],
) -> argparse.Namespace:
    """
    Parse command-line arguments and return the resulting Namespace.

    All paths are required and have no defaults so that no environment-
    specific value is hard-coded into the source.
    """
    argument_parser = argparse.ArgumentParser(
        description=(
            "Visual Novel Browser Server. Serves a browser-based viewer "
            "that polls a logs directory and renders the most recent round."
        )
    )
    argument_parser.add_argument(
        "--logs-root-directory",
        required=True,
        type=Path,
        help=(
            "Directory containing one or more 'game_YYYYMMDD_HHMMSS' "
            "subdirectories produced by the game system."
        ),
    )
    argument_parser.add_argument(
        "--web-root-directory",
        required=True,
        type=Path,
        help=(
            "Directory containing the static viewer assets "
            "(index.html, vn.css, vn.js)."
        ),
    )
    argument_parser.add_argument(
        "--vn-images-root-directory",
        required=True,
        type=Path,
        help=(
            "Directory containing avatar images. "
            "Expected layout: element_avatars/."
        ),
    )
    argument_parser.add_argument(
        "--listen-host",
        default="127.0.0.1",
        type=str,
        help=(
            "Network interface to bind. Defaults to 127.0.0.1 (loopback "
            "only). Change explicitly if you intend to expose the server."
        ),
    )
    argument_parser.add_argument(
        "--listen-port",
        required=True,
        type=int,
        help="TCP port to bind, for example 8765.",
    )
    return argument_parser.parse_args(command_line_argument_list)


def run_server(parsed_arguments: argparse.Namespace) -> None:
    """
    Configure the request handler with filesystem roots from
    parsed_arguments and run the HTTP server until interrupted.

    The server is intentionally single-threaded
    (`http.server.HTTPServer`) because the workload is local, low-rate,
    and the filesystem operations are quick. If concurrency becomes
    necessary, swap in `socketserver.ThreadingTCPServer` here.
    """
    # Validate roots up-front so misconfiguration fails immediately rather
    # than on the first request.
    for root_label, root_path in (
        ("logs root", parsed_arguments.logs_root_directory),
        ("web root", parsed_arguments.web_root_directory),
        ("vn-images root", parsed_arguments.vn_images_root_directory),
    ):
        if not root_path.exists():
            raise FileNotFoundError(
                f"Configured {root_label} does not exist: {root_path}"
            )
        if not root_path.is_dir():
            raise NotADirectoryError(
                f"Configured {root_label} is not a directory: {root_path}"
            )

    VisualNovelBrowserRequestHandler.configured_logs_root_directory = (
        parsed_arguments.logs_root_directory
    )
    VisualNovelBrowserRequestHandler.configured_web_root_directory = (
        parsed_arguments.web_root_directory
    )
    VisualNovelBrowserRequestHandler.configured_vn_images_root_directory = (
        parsed_arguments.vn_images_root_directory
    )

    server_bind_address = (
        parsed_arguments.listen_host,
        parsed_arguments.listen_port,
    )

    # with socketserver.TCPServer(
    #     server_bind_address, VisualNovelBrowserRequestHandler
    # ) as running_http_server:
    #     sys.stderr.write(
    #         f"[vn-browser] Serving on http://{server_bind_address[0]}:"
    #         f"{server_bind_address[1]}/  (Ctrl-C to stop)\n"
    #     )
    #     try:
    #         running_http_server.serve_forever()
    #     except KeyboardInterrupt:
    #         sys.stderr.write("[vn-browser] Keyboard interrupt; shutting down.\n")

    # Use VisualNovelBrowserTCPServer (not plain TCPServer) so that
    # allow_reuse_address takes effect and the port is freed immediately
    # on shutdown.
    with VisualNovelBrowserTCPServer(
        server_bind_address, VisualNovelBrowserRequestHandler
    ) as running_http_server:
        sys.stderr.write(
            f"[vn-browser] Serving on http://{server_bind_address[0]}:"
            f"{server_bind_address[1]}/  (Ctrl-C to stop)\n"
        )
        try:
            running_http_server.serve_forever()
        except KeyboardInterrupt:
            sys.stderr.write("\n[vn-browser] Ctrl-C received; shutting down.\n")
        finally:
            # shutdown() signals serve_forever() to stop its loop and
            # waits for the current request (if any) to finish cleanly.
            # server_close() then releases the socket and the port.
            running_http_server.shutdown()
            running_http_server.server_close()
            sys.stderr.write("[vn-browser] Port released. Exited cleanly.\n")


def main(command_line_argument_list: list[str]) -> int:
    """
    Program entry point. Returns a process exit code:
        0 = clean shutdown
        2 = configuration / filesystem error (clearly reported on stderr)
        1 = unexpected error (full traceback on stderr)
    """
    try:
        parsed_arguments = parse_command_line_arguments(command_line_argument_list)
        run_server(parsed_arguments)
        return 0
    except (FileNotFoundError, NotADirectoryError) as configuration_error:
        sys.stderr.write(
            f"[vn-browser] Configuration error: {configuration_error}\n"
        )
        return 2
    except Exception:  # noqa: BLE001
        sys.stderr.write("[vn-browser] Unexpected error:\n")
        sys.stderr.write(traceback.format_exc())
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
