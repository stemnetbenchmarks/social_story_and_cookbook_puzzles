/*
 * Visual Novel Browser client, version 3.
 *
 * Difference from version 2
 * -------------------------
 *   - The single polling interval has been split into two intervals
 *     with separate responsibilities:
 *
 *       fetch_and_store_game_data_once()
 *           Runs every POLL_INTERVAL_MILLISECONDS. Only re-fetches
 *           /api/game_data and stores the result. Does NOT change
 *           the displayed frame index, EXCEPT when a new game is
 *           detected (game_directory_name changed), in which case
 *           the index is reset to 0. This interval keeps running
 *           even while auto-advance is paused, so resuming is
 *           instantaneous.
 *
 *       auto_advance_one_frame_if_possible()
 *           Runs every AUTO_ADVANCE_INTERVAL_MILLISECONDS. Only
 *           increments the displayed frame index by 1 if a next
 *           frame exists. This is the interval that pause/resume
 *           toggles via clearInterval / setInterval.
 *
 *   - Three transport buttons in #control_bar are wired:
 *       #prev_button              -> handle_prev_button_click
 *       #pause_or_resume_button   -> handle_pause_or_resume_button_click
 *       #next_button              -> handle_next_button_click
 *
 *     The pause/resume button shares a single DOM element; its label
 *     is updated by update_pause_resume_button_label() to reflect
 *     the current paused/running state.
 *
 *   - handle_next_button_click() is the only button handler that
 *     can issue a network request: when the user is at the end of
 *     the currently-known frame list, it triggers one immediate
 *     fetch and then advances if (and only if) the fresh payload
 *     contains a new frame. This is what makes "manual step forward
 *     while paused" work without having to wait for the next polling
 *     tick.
 *
 * Layout coupling (unchanged from version 2)
 * ------------------------------------------
 * The HTML/CSS provide three horizontal columns inside #main_scene
 * (avatar sidebar, center content panel, map sidebar). Inside the
 * center panel, exactly one of two regions is visible at a time:
 *
 *     #center_map_region       shown on generic_map frames
 *     #center_dialogue_region  shown on player_turn frames
 *
 * Visibility is driven by a CSS class on #main_scene set by
 * apply_frame_kind_class_to_main_scene().
 */

"use strict";

// --------------------------------------------------------------------------
// Configuration
// --------------------------------------------------------------------------

// How often the network is polled for fresh /api/game_data, in ms.
// Polling continues at this rate regardless of pause state.
const POLL_INTERVAL_MILLISECONDS = 7000;

// How often the displayed frame index is incremented while not paused, in ms.
// Kept equal to the poll interval so behaviour matches the previous version.
const AUTO_ADVANCE_INTERVAL_MILLISECONDS = 7000;

// Server endpoint that returns the all-rounds JSON payload.
const GAME_DATA_API_URL = "/api/game_data";

// Button labels for the pause/resume button. Centralised so the rendering
// helper update_pause_resume_button_label() has a single source of truth.
const PAUSE_BUTTON_LABEL_WHILE_RUNNING = "⏸ pause";
const PAUSE_BUTTON_LABEL_WHILE_PAUSED = "▶ resume";

// --------------------------------------------------------------------------
// Module-scoped client state
// --------------------------------------------------------------------------
//
// All client state lives in this single object so it is easy to inspect
// from the browser console and so no function reads hidden globals.
//
//   last_seen_game_directory_name
//       Game directory name from the most recent successful poll, used
//       to detect a new-game transition. When this changes, the frame
//       index is reset to 0 by fetch_and_store_game_data_once().
//
//   currently_displayed_frame_index
//       Integer index into the flat frame list assembled by
//       build_frames_from_all_rounds_payload().
//
//   most_recent_round_payload
//       The most recent JSON payload from /api/game_data, or null if
//       no successful poll has happened yet.
//
//   auto_advance_is_paused
//       True iff the user has paused auto-advance via the transport
//       button. Polling continues regardless.
//
//   auto_advance_interval_handle
//       The handle returned by setInterval() for the auto-advance
//       interval, or null when paused. Used by clearInterval() on pause.

const visual_novel_client_state = {
  last_seen_game_directory_name: null,
  currently_displayed_frame_index: 0,
  most_recent_round_payload: null,
  auto_advance_is_paused: false,
  auto_advance_interval_handle: null,
};

// --------------------------------------------------------------------------
// DOM element references (looked up once at startup)
// --------------------------------------------------------------------------

const dom_main_scene_element = document.getElementById("main_scene");
const dom_avatar_image_element = document.getElementById("avatar_image");
const dom_player_id_label_element = document.getElementById("player_id_label");
const dom_map_sidebar_label_element =
  document.getElementById("map_sidebar_label");

const dom_center_map_text_element = document.getElementById("center_map_text");

const dom_dialogue_header_element = document.getElementById(
  "dialogue_header_line",
);
const dom_action_summary_text_element = document.getElementById(
  "action_summary_text",
);
const dom_note_share_memo_text_element = document.getElementById(
  "note_share_memo_text",
);
const dom_progress_indicator_element =
  document.getElementById("progress_indicator");

const dom_pov_map_text_element = document.getElementById("pov_map_text");

const dom_prev_button_element = document.getElementById("prev_button");
const dom_pause_or_resume_button_element = document.getElementById(
  "pause_or_resume_button",
);
const dom_next_button_element = document.getElementById("next_button");

// --------------------------------------------------------------------------
// Frame assembly
// --------------------------------------------------------------------------

/**
 * Build the flat ordered list of frames to display, from a payload that
 * contains ALL rounds.
 *
 * Frame order
 * -----------
 * For each round in all_rounds_in_sorted_order (round_1 first):
 *   - One "generic_map" frame if generic_round_map_text is present.
 *   - One "player_turn" frame per entry in
 *     player_turns_in_chronological_order.
 *
 * @param {object|null} game_payload
 *     The JSON payload returned by /api/game_data.
 * @returns {Array<object>}
 *     Ordered array of frame description objects with the shape:
 *         {
 *             frame_kind           : "generic_map" | "player_turn",
 *             header_text          : string,
 *             pov_map_text         : string | null,
 *             avatar_image_url     : string | null,
 *             player_id_label      : string | null,
 *             action_summary_text  : string | null,
 *             note_share_memo_text : string | null,
 *         }
 */
function build_frames_from_all_rounds_payload(game_payload) {
  const assembled_frames_list = [];

  if (game_payload === null || game_payload === undefined) {
    return assembled_frames_list;
  }

  const game_directory_name_or_none = game_payload.game_directory_name;
  const all_rounds_list = game_payload.all_rounds_in_sorted_order || [];

  for (const single_round_object of all_rounds_list) {
    const round_name =
      single_round_object.round_directory_name || "(unknown round)";
    const round_label_prefix =
      (game_directory_name_or_none || "(no game)") + " / " + round_name;

    if (single_round_object.generic_round_map_text) {
      assembled_frames_list.push({
        frame_kind: "generic_map",
        header_text: round_label_prefix + "  —  round so far",
        pov_map_text: single_round_object.generic_round_map_text,
        avatar_image_url: null,
        player_id_label: null,
        action_summary_text: null,
        note_share_memo_text: null,
      });
    }

    const player_turns_list =
      single_round_object.player_turns_in_chronological_order || [];
    for (const single_player_turn of player_turns_list) {
      assembled_frames_list.push({
        frame_kind: "player_turn",
        header_text:
          round_label_prefix +
          "  —  player " +
          (single_player_turn.player_id || "?") +
          "  (" +
          (single_player_turn.element || "unknown element") +
          ")  " +
          (single_player_turn.log_timestamp || ""),
        pov_map_text: single_player_turn.pov_map_text,
        avatar_image_url: single_player_turn.avatar_image_url,
        player_id_label: single_player_turn.player_id,
        action_summary_text: format_action_summary_text(single_player_turn),
        note_share_memo_text: single_player_turn.note_share_memo,
      });
    }
  }

  return assembled_frames_list;
}

/**
 * Build a short human-readable summary of the action taken by a player
 * on a single turn. This appears in the upper portion of the middle
 * dialogue region, above the longer note_share_memo text.
 *
 * @param {object} single_player_turn
 * @returns {string}
 */
function format_action_summary_text(single_player_turn) {
  const summary_lines_list = [];

  const element_or_null = single_player_turn.element;
  if (element_or_null) {
    summary_lines_list.push("element: " + element_or_null);
  }

  const move_from_coord_or_null = single_player_turn.move_from_coord;
  const move_to_coord_or_null = single_player_turn.move_to_coord;
  if (move_from_coord_or_null && move_to_coord_or_null) {
    summary_lines_list.push(
      "move: " +
        JSON.stringify(move_from_coord_or_null) +
        "  ->  " +
        JSON.stringify(move_to_coord_or_null),
    );
  }

  const start_round_vote_or_null = single_player_turn.start_round_vote;
  if (
    start_round_vote_or_null !== null &&
    start_round_vote_or_null !== undefined
  ) {
    summary_lines_list.push(
      "start_round_vote: " + String(start_round_vote_or_null),
    );
  }

  return summary_lines_list.join("\n");
}

// --------------------------------------------------------------------------
// Rendering
// --------------------------------------------------------------------------

/**
 * Update the single CSS class on #main_scene that selects which of the
 * two center regions is visible (the wide map vs. the dialogue stack).
 *
 * @param {"generic_map"|"player_turn"} frame_kind_string
 */
function apply_frame_kind_class_to_main_scene(frame_kind_string) {
  dom_main_scene_element.classList.remove(
    "frame_kind_generic_map",
    "frame_kind_player_turn",
  );
  if (frame_kind_string === "generic_map") {
    dom_main_scene_element.classList.add("frame_kind_generic_map");
  } else {
    dom_main_scene_element.classList.add("frame_kind_player_turn");
  }
}

/**
 * Render the frame at the current index of the most recent payload.
 *
 * Frame routing
 * -------------
 *   generic_map frame :
 *     - middle column shows the wide ASCII round-so-far map
 *     - right map sidebar is cleared
 *     - left avatar sidebar is cleared
 *
 *   player_turn frame :
 *     - middle column shows header + action summary + memo
 *     - right map sidebar shows the per-player POV mini-map
 *     - left avatar sidebar shows the player's element-avatar
 *
 * After rendering the scene, transport-button enabled/disabled state
 * is also refreshed (#prev_button is disabled at index 0; #next_button
 * is never disabled because it can fetch fresh data on click).
 */
function render_current_frame() {
  const frames_list = build_frames_from_all_rounds_payload(
    visual_novel_client_state.most_recent_round_payload,
  );

  if (frames_list.length === 0) {
    apply_frame_kind_class_to_main_scene("player_turn");
    dom_avatar_image_element.removeAttribute("src");
    dom_avatar_image_element.setAttribute(
      "alt",
      "(no avatar — waiting for logs)",
    );
    dom_player_id_label_element.textContent = "";
    dom_center_map_text_element.textContent = "";
    dom_pov_map_text_element.textContent = "";
    dom_dialogue_header_element.textContent = "Visual Novel Browser";
    dom_action_summary_text_element.textContent = "";
    dom_note_share_memo_text_element.textContent =
      "Waiting for game logs to appear...";
    dom_progress_indicator_element.textContent = "0 / 0";
    update_transport_button_enabled_state(frames_list.length);
    return;
  }

  // Clamp the index in case the payload shrank for any reason.
  if (
    visual_novel_client_state.currently_displayed_frame_index >=
    frames_list.length
  ) {
    visual_novel_client_state.currently_displayed_frame_index =
      frames_list.length - 1;
  }
  if (visual_novel_client_state.currently_displayed_frame_index < 0) {
    visual_novel_client_state.currently_displayed_frame_index = 0;
  }

  const current_frame_object =
    frames_list[visual_novel_client_state.currently_displayed_frame_index];

  apply_frame_kind_class_to_main_scene(current_frame_object.frame_kind);

  // ---- Left column: avatar -------------------------------------------
  if (current_frame_object.avatar_image_url) {
    dom_avatar_image_element.setAttribute(
      "src",
      current_frame_object.avatar_image_url,
    );
    dom_avatar_image_element.setAttribute(
      "alt",
      "avatar for player " + (current_frame_object.player_id_label || "?"),
    );
  } else {
    dom_avatar_image_element.removeAttribute("src");
    dom_avatar_image_element.setAttribute("alt", "(no avatar for this frame)");
  }
  dom_player_id_label_element.textContent = current_frame_object.player_id_label
    ? "player " + current_frame_object.player_id_label
    : "";

  // ---- Middle column: route by frame_kind ----------------------------
  if (current_frame_object.frame_kind === "generic_map") {
    dom_center_map_text_element.textContent =
      current_frame_object.pov_map_text || "(no map for this frame)";
    dom_dialogue_header_element.textContent = current_frame_object.header_text;
    dom_action_summary_text_element.textContent = "";
    dom_note_share_memo_text_element.textContent = "";
  } else {
    dom_center_map_text_element.textContent = "";
    dom_dialogue_header_element.textContent = current_frame_object.header_text;
    dom_action_summary_text_element.textContent =
      current_frame_object.action_summary_text || "";
    dom_note_share_memo_text_element.textContent =
      current_frame_object.note_share_memo_text || "";
  }

  // ---- Right column: per-player POV mini-map -------------------------
  if (current_frame_object.frame_kind === "player_turn") {
    dom_pov_map_text_element.textContent =
      current_frame_object.pov_map_text || "(no POV map for this turn)";
    dom_map_sidebar_label_element.textContent = "      Dungeon Room Map";
  } else {
    dom_pov_map_text_element.textContent = "";
    dom_map_sidebar_label_element.textContent = ""; // empty on generic_map frames
  }

  // Progress indicator (1-based display).
  dom_progress_indicator_element.textContent =
    visual_novel_client_state.currently_displayed_frame_index +
    1 +
    " / " +
    frames_list.length;

  update_transport_button_enabled_state(frames_list.length);
}

/**
 * Refresh the disabled state of the transport buttons based on the
 * current frame index and the total number of frames.
 *
 * #prev_button : disabled iff currently at frame 0 (or the list is empty).
 * #next_button : never disabled. When the user is at the last known
 *                frame, clicking it triggers an immediate poll to look
 *                for new frames; if none have appeared, the click has
 *                no visible effect, which is the intended behaviour.
 *
 * @param {number} total_number_of_frames
 *     The current length of the frame list.
 */
function update_transport_button_enabled_state(total_number_of_frames) {
  const at_first_frame =
    total_number_of_frames === 0 ||
    visual_novel_client_state.currently_displayed_frame_index <= 0;
  dom_prev_button_element.disabled = at_first_frame;
  // dom_next_button_element is always enabled (see docstring above).
  dom_next_button_element.disabled = false;
}

/**
 * Update the label of #pause_or_resume_button to reflect the current
 * value of visual_novel_client_state.auto_advance_is_paused.
 */
function update_pause_resume_button_label() {
  dom_pause_or_resume_button_element.textContent =
    visual_novel_client_state.auto_advance_is_paused
      ? PAUSE_BUTTON_LABEL_WHILE_PAUSED
      : PAUSE_BUTTON_LABEL_WHILE_RUNNING;
}

// --------------------------------------------------------------------------
// Network: fetch-only (no index advance)
// --------------------------------------------------------------------------

/**
 * Fetch the all-rounds payload from /api/game_data and store it in
 * visual_novel_client_state. Does NOT advance the displayed frame
 * index, with one exception:
 *
 *   - If the game_directory_name in the new payload differs from the
 *     previously-seen one, the frame index is reset to 0. This is a
 *     hard context switch (a new game has started) and must not be
 *     conflated with normal step-by-step advancement.
 *
 * After storing, render_current_frame() is called so any payload
 * changes (new frames, refreshed text, new game) are reflected on
 * screen even when auto-advance is paused.
 *
 * Network or JSON errors are logged to the console and surfaced in
 * the dialogue header. The function never throws to its caller; the
 * polling and button-handler loops continue regardless.
 */
async function fetch_and_store_game_data_once() {
  let fetched_game_payload = null;
  try {
    const fetch_response = await fetch(GAME_DATA_API_URL, {
      cache: "no-store",
    });
    if (!fetch_response.ok) {
      throw new Error(
        "Server returned status " +
          fetch_response.status +
          " for " +
          GAME_DATA_API_URL,
      );
    }
    fetched_game_payload = await fetch_response.json();
  } catch (caught_fetch_error) {
    console.error("[vn-browser] poll failed:", caught_fetch_error);
    dom_dialogue_header_element.textContent =
      "Poll error: " + String(caught_fetch_error);
    return;
  }

  const new_game_directory_name =
    fetched_game_payload.game_directory_name || "(none)";
  if (
    visual_novel_client_state.last_seen_game_directory_name !==
    new_game_directory_name
  ) {
    // New game (or first poll of this session). Reset the index so
    // the viewer starts the new game from frame 0.
    visual_novel_client_state.currently_displayed_frame_index = 0;
  }

  visual_novel_client_state.last_seen_game_directory_name =
    new_game_directory_name;
  visual_novel_client_state.most_recent_round_payload = fetched_game_payload;

  render_current_frame();
}

// --------------------------------------------------------------------------
// Auto-advance (index-only)
// --------------------------------------------------------------------------

/**
 * If a frame exists after the currently-displayed one, advance to it;
 * otherwise do nothing. This is the only function (besides the next
 * button handler) that increments the displayed frame index during
 * normal operation.
 *
 * Intentionally does NOT issue a network request; data freshness is
 * the polling loop's responsibility.
 */
function auto_advance_one_frame_if_possible() {
  const frames_list = build_frames_from_all_rounds_payload(
    visual_novel_client_state.most_recent_round_payload,
  );
  const next_candidate_index =
    visual_novel_client_state.currently_displayed_frame_index + 1;
  if (next_candidate_index < frames_list.length) {
    visual_novel_client_state.currently_displayed_frame_index =
      next_candidate_index;
    render_current_frame();
  }
  // else: at end of currently-known frames; wait for a future poll
  //       to bring more, or for the user to click next.
}

/**
 * Start the auto-advance interval if it is not already running and
 * the auto_advance_is_paused flag is false. Idempotent: calling twice
 * in a row leaves exactly one interval running.
 */
function start_auto_advance_loop() {
  if (visual_novel_client_state.auto_advance_is_paused) {
    return;
  }
  if (visual_novel_client_state.auto_advance_interval_handle !== null) {
    return;
  }
  visual_novel_client_state.auto_advance_interval_handle = setInterval(
    auto_advance_one_frame_if_possible,
    AUTO_ADVANCE_INTERVAL_MILLISECONDS,
  );
}

/**
 * Stop the auto-advance interval if it is currently running. Idempotent.
 */
function stop_auto_advance_loop() {
  if (visual_novel_client_state.auto_advance_interval_handle !== null) {
    clearInterval(visual_novel_client_state.auto_advance_interval_handle);
    visual_novel_client_state.auto_advance_interval_handle = null;
  }
}

// --------------------------------------------------------------------------
// Transport button handlers
// --------------------------------------------------------------------------

/**
 * Handle a click on #prev_button: decrement the displayed frame index
 * by 1, clamped at 0. Re-renders. Never touches the network.
 */
function handle_prev_button_click() {
  if (visual_novel_client_state.currently_displayed_frame_index > 0) {
    visual_novel_client_state.currently_displayed_frame_index -= 1;
    render_current_frame();
  }
  // else: already at frame 0; the button should be disabled in this
  //       state, but defending against stale UI is cheap.
}

/**
 * Handle a click on #pause_or_resume_button: flip auto_advance_is_paused
 * and start or stop the auto-advance interval accordingly. Polling is
 * unaffected.
 */
function handle_pause_or_resume_button_click() {
  if (visual_novel_client_state.auto_advance_is_paused) {
    // Currently paused -> resume.
    visual_novel_client_state.auto_advance_is_paused = false;
    start_auto_advance_loop();
  } else {
    // Currently running -> pause.
    visual_novel_client_state.auto_advance_is_paused = true;
    stop_auto_advance_loop();
  }
  update_pause_resume_button_label();
}

/**
 * Handle a click on #next_button: advance the displayed frame index
 * by 1 if a next frame already exists in the cached payload. If not,
 * trigger one immediate fetch from /api/game_data, then advance if
 * (and only if) the refreshed payload contains a new frame. If still
 * at the end, do nothing.
 *
 * This is the only button handler that issues a network request, and
 * it does so at most once per click. The behaviour is intentional: it
 * lets a paused user step manually into newly-arrived data without
 * waiting for the next polling tick, while keeping a click that finds
 * nothing new from being misinterpreted as "broken".
 */
async function handle_next_button_click() {
  const frames_list_before = build_frames_from_all_rounds_payload(
    visual_novel_client_state.most_recent_round_payload,
  );
  const next_candidate_index_before =
    visual_novel_client_state.currently_displayed_frame_index + 1;

  if (next_candidate_index_before < frames_list_before.length) {
    // A next frame is already cached; just advance.
    visual_novel_client_state.currently_displayed_frame_index =
      next_candidate_index_before;
    render_current_frame();
    return;
  }

  // At the end of cached frames: ask the server if more exist.
  // fetch_and_store_game_data_once() handles its own errors; on
  // failure most_recent_round_payload is unchanged and the second
  // length check below will simply leave the index alone.
  await fetch_and_store_game_data_once();

  const frames_list_after = build_frames_from_all_rounds_payload(
    visual_novel_client_state.most_recent_round_payload,
  );
  const next_candidate_index_after =
    visual_novel_client_state.currently_displayed_frame_index + 1;
  if (next_candidate_index_after < frames_list_after.length) {
    visual_novel_client_state.currently_displayed_frame_index =
      next_candidate_index_after;
    render_current_frame();
  }
  // else: still no new frame; click has no visible effect.
}

// --------------------------------------------------------------------------
// Wiring
// --------------------------------------------------------------------------

/**
 * Attach click listeners to the three transport buttons. Called once
 * at DOMContentLoaded.
 */
function attach_transport_button_event_handlers() {
  dom_prev_button_element.addEventListener("click", handle_prev_button_click);
  dom_pause_or_resume_button_element.addEventListener(
    "click",
    handle_pause_or_resume_button_click,
  );
  dom_next_button_element.addEventListener("click", handle_next_button_click);
}

/**
 * Start the always-on polling interval. The first poll runs
 * immediately so the viewer does not display an empty screen for
 * the full interval at startup.
 */
function start_polling_loop() {
  fetch_and_store_game_data_once();
  setInterval(fetch_and_store_game_data_once, POLL_INTERVAL_MILLISECONDS);
}

// --------------------------------------------------------------------------
// Entry point
// --------------------------------------------------------------------------

window.addEventListener("DOMContentLoaded", function on_dom_content_loaded() {
  update_pause_resume_button_label(); // reflect initial running state
  attach_transport_button_event_handlers();
  render_current_frame(); // show "waiting for logs..." placeholder
  start_polling_loop(); // begin fetching every 7 s
  start_auto_advance_loop(); // begin advancing every 7 s
});
