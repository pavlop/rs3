from enum import Enum
from os.path import dirname
from pathlib import Path

import cv2

project_root = Path(dirname(dirname(__file__)))


class ScreenPart(Enum):
  MINING_LABEL_ANY_ROCK = 1
  MINING_LABEL_GOLD_ROCK = 2
  MINING_LABEL_ADAMANTINE_ROCK = 3
  ICON_BACKPACK_TAB = 4
  ICON_INVENTORY_TUNA = 5
  ICON_VIEW_YOUR_WEALTH_INVENTORY = 6
  TEST_SCREENSHOT_FULL_SCREEN1 = 7
  TEST_SCREENSHOT_FULL_SCREEN2 = 8
  TEST_SCREENSHOT_FULL_SCREEN3 = 9


IMAGE_FILES_MAP = {
  ScreenPart.MINING_LABEL_GOLD_ROCK: 'resources/label/mining_adamantine_rock.png',
  ScreenPart.ICON_BACKPACK_TAB: 'resources/menu/icon_backpack_tab.bmp',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN1: 'resources/test/full_screenshot_1.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN2: 'resources/test/full_screenshot_2.png',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN3: 'resources/test/full_screenshot_3.png',
  ScreenPart.ICON_VIEW_YOUR_WEALTH_INVENTORY: 'resources/menu/icon_view_your_wealth_inventory.png',
}

# Convert string paths to absolute paths
IMAGE_FILES_MAP_RESOLVED = {key: (project_root / path).as_posix() for key, path in IMAGE_FILES_MAP.items()}

# Values are PIL.Image.Image
IMAGE_MAP = {key: cv2.imread(IMAGE_FILES_MAP_RESOLVED[key], 0) for key in IMAGE_FILES_MAP_RESOLVED.keys()}
