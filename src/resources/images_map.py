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
  TEST_SCREENSHOT_FULL_SCREEN = 6


IMAGE_FILES_MAP = {
  ScreenPart.MINING_LABEL_GOLD_ROCK: 'resources/label/mining_adamantine_rock.png',
  ScreenPart.ICON_BACKPACK_TAB: 'resources/menu/icon_backpack_tab.bmp',
  ScreenPart.TEST_SCREENSHOT_FULL_SCREEN: 'resources/test/example_full_screenshot.png',
}

# Convert string paths to absolute paths
IMAGE_FILES_MAP_RESOLVED = {key: (project_root / path).as_posix() for key, path in IMAGE_FILES_MAP.items()}

# Values are PIL.Image.Image
IMAGE_MAP = {
  ScreenPart.MINING_LABEL_GOLD_ROCK: cv2.imread(IMAGE_FILES_MAP_RESOLVED[ScreenPart.MINING_LABEL_GOLD_ROCK], 0),
  ScreenPart.ICON_BACKPACK_TAB: cv2.imread(IMAGE_FILES_MAP_RESOLVED[ScreenPart.ICON_BACKPACK_TAB], 0),
}
