#### rpg_visual_novel_ui

# Instructions:

### For Google Colab:
The visual-novel will be a re-play of a finished game.
1. Run run_v2_5_bot_iterator() in colab (in the cloud)
2. a zipped_*.zip file archive will be created (if run finishes)
3. download that
4. unzip
5. point to that /logs/ file in the code below (or move it and point there)
6. run visual_novel_browser_server.py
7. open browser to url shown in terminal

### For real-time game data:
1. You will need to run locally, setting up a python environment for
the google or anthropic pip packages.
2. Your environment variables such as api-keys should be stored in a .env or .config file \
   and loaded with a package such as dot-env
   Do not hard-code your api keys into a python file (.py or .ipynb)
3. Use jupyter notebooks or a .py file to run code.
4. Run run_v2_5_bot_iterator()
5. point to where /logs/ is
6. run visual_novel_browser_server.py
7. open browser to url shown in terminal


# to run from terminal:
```bash
python visual_novel_browser_server.py \
    --logs-root-directory ./logs \
    --web-root-directory ./web \
    --vn-images-root-directory ./vn_images \
    --listen-port 8765
```

# e.g. using full paths
```bash
python /home/abc/code/ai_rpg_arena/rpg_visual_novel_ui/visual_novel_browser_server.py \
    --logs-root-directory /home/abc/code/ai_rpg_arena/logs \
    --web-root-directory /home/abc/code/ai_rpg_arena/rpg_visual_novel_ui/web \
    --vn-images-root-directory /home/abc/code/ai_rpg_arena/rpg_visual_novel_ui/vn_images \
    --listen-port 8765
```

# e.g. using local paths paths from cwd /ai_rpg_arena/
```bash
python rpg_visual_novel_ui/visual_novel_browser_server.py \
    --logs-root-directory logs \
    --web-root-directory rpg_visual_novel_ui/web \
    --vn-images-root-directory rpg_visual_novel_ui/vn_images \
    --listen-port 8765
```

# Sample Tree
```text
$ tree
.
├── logs
│   └── game_20260429_152512
│       ├── round_1
│       │   ├── gm_a_pov_map_20260429_152514562.txt
│       │   ├── gm_b_pov_map_20260429_152516542.txt
│       │   ├── gm_c_pov_map_20260429_152521953.txt
│       │   ├── gm_d_pov_map_20260429_152524031.txt
│       │   ├── gm_e_pov_map_20260429_152525805.txt
│       │   ├── gm_generic_round_dungeon_so_far_20260429_152512.txt
│       │   ├── playerlog_20260429_152514_a.json
│       │   ├── playerlog_20260429_152516_b.json
│       │   ├── playerlog_20260429_152521_c.json
│       │   ├── playerlog_20260429_152524_d.json
│       │   └── playerlog_20260429_152525_e.json
│       ├── round_2
│       │   ├── gm_a_pov_map_20260429_152529267.txt
│       │   ├── gm_b_pov_map_20260429_152532171.txt
│       │   ├── gm_c_pov_map_20260429_152534460.txt
│       │   ├── gm_d_pov_map_20260429_152536703.txt
│       │   ├── gm_e_pov_map_20260429_152539103.txt
│       │   ├── gm_generic_round_dungeon_so_far_20260429_152525.txt
│       │   ├── playerlog_20260429_152529_a.json
│       │   ├── playerlog_20260429_152532_b.json
│       │   ├── playerlog_20260429_152534_c.json
│       │   ├── playerlog_20260429_152536_d.json
│       │   └── playerlog_20260429_152539_e.json
│       ├── round_3
│       │   ├── gm_a_pov_map_20260429_152544731.txt
│       │   ├── gm_b_pov_map_20260429_152547261.txt
│       │   ├── gm_c_pov_map_20260429_152549086.txt
│       │   ├── gm_d_pov_map_20260429_152551654.txt
│       │   ├── gm_e_pov_map_20260429_152554574.txt
│       │   ├── gm_generic_round_dungeon_so_far_20260429_152539.txt
│       │   ├── playerlog_20260429_152544_a.json
│       │   ├── playerlog_20260429_152547_b.json
│       │   ├── playerlog_20260429_152549_c.json
│       │   ├── playerlog_20260429_152551_d.json
│       │   └── playerlog_20260429_152554_e.json
│       ├── round_4
│       │   ├── gm_a_pov_map_20260429_152556656.txt
│       │   ├── gm_b_pov_map_20260429_152559173.txt
│       │   ├── gm_c_pov_map_20260429_152603215.txt
│       │   ├── gm_d_pov_map_20260429_152605202.txt
│       │   ├── gm_e_pov_map_20260429_152607310.txt
│       │   ├── gm_generic_round_dungeon_so_far_20260429_152554.txt
│       │   ├── playerlog_20260429_152556_a.json
│       │   ├── playerlog_20260429_152559_b.json
│       │   ├── playerlog_20260429_152603_c.json
│       │   ├── playerlog_20260429_152605_d.json
│       │   └── playerlog_20260429_152607_e.json
│       └── start_state.json
└── rpg_visual_novel_ui
    ├── README.md
    ├── visual_novel_browser_server.py
    ├── vn_images
    │   └── element_avatars
    │       ├── fire_avatar.png
    │       ├── forest_avatar.png
    │       ├── ice_avatar.png
    │       ├── void_avatar.png
    │       └── water_avatar.png
    └── web
        ├── index.html
        ├── vn.css
        └── vn.js

11 directories, 55 files
```
