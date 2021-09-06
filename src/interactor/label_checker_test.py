import unittest

from interactor.label_checker import LabelChecker
from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import area_between_pictures
from utils.screen_utils import draw_rectangle
from utils.screen_utils import resize_area_keep_center

class LabelCheckerTest(unittest.TestCase):

  # def testCheckStaticFound(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
  #   top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
  #   bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
  #   area = area_between_pictures(screen, top, bottom)
  #
  #   checker = LabelChecker(screen, IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB], area)
  #   print(checker.check())

  def testCheckStaticNotFound(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    area = area_between_pictures(screen, top, bottom)
    area_small = resize_area_keep_center(area, 0.2)

    checker = LabelChecker(screen, IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB], area_small)
    print(checker.check())
    draw_rectangle(screen, resize_area_keep_center(area, 0.3))

if __name__ == '__main__':
  unittest.main()
