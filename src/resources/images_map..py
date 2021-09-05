from enum import Enum
import cv2 as cv

class ScreenPart(Enum):
  MINING_LABEL_ANY_ROCK = 1
  MINING_LABEL_GOLD_ROCK = 2
  MINING_LABEL_ADAMANTINE_ROCK = 3
  ICON_BACKPACK_TAB = 4
  ICON_INVENTORY_TUNA = 5

IMAGE_FILE_MAP = {
  ScreenPart.MINING_LABEL_GOLD_ROCK: 'resources/label/mining_adamantine_rock.png',
  ScreenPart.ICON_BACKPACK_TAB: '/resources/menus/icon_backpack_tab.bmp',
}

# Values are PIL.Image.Image
IMAGE_MAP = {
  ScreenPart.MINING_LABEL_GOLD_ROCK: cv.imread(IMAGE_FILE_MAP[ScreenPart.MINING_LABEL_GOLD_ROCK], 0),
  ScreenPart.ICON_BACKPACK_TAB: cv.imread(IMAGE_FILE_MAP[ScreenPart.ICON_BACKPACK_TAB], 0),
}
