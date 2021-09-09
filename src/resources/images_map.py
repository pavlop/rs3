from enum import Enum
from os.path import dirname
from pathlib import Path

import cv2

project_root = Path(dirname(dirname(__file__)))


class ScreenPart(Enum):
  # UI elements
  ICON_BACKPACK_TAB = 1
  ICON_VIEW_YOUR_WEALTH_INVENTORY = 2
  LAYOUT_RIGHT_BOTTOM_ICON = 3
  ICON_ACTON_BAR_TOP_CORNER = 4
  ICON_ALL_CHATS = 5
  BUTTON_BEGIN_PROJECT = 6
  TELEPORT_MINIMAP_ICON = 7

  # World objects 100
  MINING_LABEL_ANY = 101
  ATTACK_LABEL = 102

  # Test objects 1000
  TEST_SCREENSHOT_FULL_SCREEN1 = 1001
  TEST_SCREENSHOT_FULL_SCREEN2 = 1002
  TEST_SCREENSHOT_FULL_SCREEN3 = 1003
  TEST_SCREENSHOT_FULL_SCREEN4 = 1004
  TEST_TWO_MARKERS_SMALL = 1005
  TEST_MARKERS_TOP_ORANGE = 1006
  TEST_MARKERS_BOTTOM_RED = 1007
  TEST_SCREENSHOT_FULL_SCREEN_MINE = 1009
  TEST_MINIMAP_FIRST_TOWN = 1021

  # Map related images (world map + minimap)
  BANK_MINIMAP_LABEL = 10003
  BANK_LABEL = 10004
  FIRST_TOWN_TELEPORT_ICON = 10005

IMAGE_FILES_MAP = {
  ScreenPart.ICON_ACTON_BAR_TOP_CORNER: 'resources/menu/icon_acton_bar_top_corner.bmp',
  ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON: 'resources/menu/layout_right_bottom_icon.png',
  ScreenPart.ICON_VIEW_YOUR_WEALTH_INVENTORY: 'resources/menu/icon_view_your_wealth_inventory.png',
  ScreenPart.ICON_BACKPACK_TAB: 'resources/menu/icon_backpack_tab.bmp',
  ScreenPart.ICON_ALL_CHATS: 'resources/menu/icon_all_chats.png',
  ScreenPart.BUTTON_BEGIN_PROJECT: 'resources/menu/button_begin_project.png',
  ScreenPart.ATTACK_LABEL: 'resources/labels/attack_label.png',
  ScreenPart.MINING_LABEL_ANY: 'resources/labels/mining_any_2.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN1: 'resources/test/full_screenshot_1.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN2: 'resources/test/full_screenshot_2.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN3: 'resources/test/full_screenshot_3.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4: 'resources/test/full_screenshot_4.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE: 'resources/test/full_screenshot_mine.png',
  ScreenPart.TEST_TWO_MARKERS_SMALL: 'resources/test/test_two_markers_small.png',
  ScreenPart.TEST_MARKERS_TOP_ORANGE: 'resources/test/test_marker_small_orange.png',
  ScreenPart.TEST_MARKERS_BOTTOM_RED: 'resources/test/test_marker_small_red.png',
  ScreenPart.TEST_MINIMAP_FIRST_TOWN: 'resources/test/minimap_first_town_test.png',
  ScreenPart.BANK_MINIMAP_LABEL: 'resources/labels/bank_minimap_label.png',
  ScreenPart.FIRST_TOWN_TELEPORT_ICON: 'resources/labels/first_town_teleport_icon.png',
  ScreenPart.TELEPORT_MINIMAP_ICON: 'resources/labels/teleport_minimap_icon.png',
  ScreenPart.BANK_LABEL: 'resources/labels/bank_label.png',
}

# Convert string paths to absolute paths
IMAGE_FILES_MAP_RESOLVED = {key: (project_root / path).as_posix() for key, path in IMAGE_FILES_MAP.items()}

# Values are PIL.Image.Image
IMAGE_MAP = {key: cv2.imread(IMAGE_FILES_MAP_RESOLVED[key]) for key in IMAGE_FILES_MAP_RESOLVED.keys()}

# Check all images are loaded
for e in ScreenPart:
  if IMAGE_MAP[e] is None:
    print("IMAGE NOT LOADED!!!!!", e)
