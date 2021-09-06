from enum import Enum
from os.path import dirname
from pathlib import Path

import cv2

project_root = Path(dirname(dirname(__file__)))


class ScreenPart(Enum):
  # UI elements
  ICON_BACKPACK_TAB = 1
  ICON_INVENTORY_TUNA = 2
  ICON_VIEW_YOUR_WEALTH_INVENTORY = 3
  LAYOUT_RIGHT_BOTTOM_ICON = 4
  ICON_ACTON_BAR_TOP_CORNER = 5

  # World objects 100
  MINING_LABEL_ANY_ROCK = 101
  MINING_LABEL_GOLD_ROCK = 102
  MINING_LABEL_ADAMANTINE_ROCK = 103

  # Test objects 1000
  TEST_SCREENSHOT_FULL_SCREEN1 = 1001
  TEST_SCREENSHOT_FULL_SCREEN2 = 1002
  TEST_SCREENSHOT_FULL_SCREEN3 = 1003
  TEST_SCREENSHOT_FULL_SCREEN4 = 1004
  TEST_TWO_MARKERS_SMALL = 1005
  TEST_MARKERS_SMALL_ORANGE = 1006
  TEST_MARKERS_SMALL_RED = 1007


IMAGE_FILES_MAP = {
  ScreenPart.ICON_ACTON_BAR_TOP_CORNER: 'resources/menu/icon_acton_bar_top_corner.bmp',
  ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON: 'resources/menu/layout_right_bottom_icon.png',
  ScreenPart.ICON_VIEW_YOUR_WEALTH_INVENTORY: 'resources/menu/icon_view_your_wealth_inventory.png',
  ScreenPart.ICON_BACKPACK_TAB: 'resources/menu/icon_backpack_tab.bmp',
  ScreenPart.MINING_LABEL_GOLD_ROCK: 'resources/label/mining_adamantine_rock.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN1: 'resources/test/full_screenshot_1.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN2: 'resources/test/full_screenshot_2.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN3: 'resources/test/full_screenshot_3.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4: 'resources/test/full_screenshot_4.png',
  ScreenPart.TEST_TWO_MARKERS_SMALL: 'resources/test/test_two_markers_small.png',
  ScreenPart.TEST_MARKERS_SMALL_ORANGE: 'resources/test/test_marker_small_orange.png',
  ScreenPart.TEST_MARKERS_SMALL_RED: 'resources/test/test_marker_small_red.png',

}

# Convert string paths to absolute paths
IMAGE_FILES_MAP_RESOLVED = {key: (project_root / path).as_posix() for key, path in IMAGE_FILES_MAP.items()}

# Values are PIL.Image.Image
IMAGE_MAP = {key: cv2.imread(IMAGE_FILES_MAP_RESOLVED[key], 0) for key in IMAGE_FILES_MAP_RESOLVED.keys()}
