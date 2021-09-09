import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import area_between_pictures, area_of_picture, RectangularArea
from utils.screen_utils import resize_area_keep_center
from world.sceen_area_checker import ScreenAreaChecker
from world.world_state import WorldState


class LabelCheckerTest(unittest.TestCase):

  def testFullScreenArea(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE]
    full_area = area_of_picture(screen, screen)
    expected_area = RectangularArea(top_x=0, top_y=0, bottom_x=1665, bottom_y=1329)
    self.assertEqual(full_area, expected_area)

  def testCheckStaticFound(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    area = area_between_pictures(screen, top, bottom)
    static_world = WorldState()
    static_world.update_screen_with_img(screen)
    checker = ScreenAreaChecker(static_world, IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB], area)
    self.assertIsNotNone(checker.check())

  def testCheckStaticNotFound(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    area = area_between_pictures(screen, top, bottom)
    area_small = resize_area_keep_center(area, 0.2)
    static_world = WorldState()
    static_world.update_screen_with_img(screen)
    checker = ScreenAreaChecker(static_world, IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB], area_small)
    self.assertIsNone(checker.check())
    # show_image_with_rectangle(screen, resize_area_keep_center(area, 0.5))

  def testCheckDynamicResults(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    area = area_between_pictures(screen, top, bottom)
    static_world = WorldState()
    static_world.update_screen_with_img(screen)
    checker = ScreenAreaChecker(static_world, IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB], area)

    # Label found on large area
    self.assertIsNotNone(checker.check())

    # Resize area and check again
    area.update(resize_area_keep_center(area, 0.2))
    self.assertIsNone(checker.check())

  def testCheckMining(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE]
    full_area = area_of_picture(screen, screen)
    static_world = WorldState()
    static_world.update_screen_with_img(screen)
    checker = ScreenAreaChecker(static_world, IMAGE_MAP[ScreenPart.MINING_LABEL_ANY], full_area)
    label_found = checker.check()
    self.assertIsNotNone(label_found)
    # print(label_found)
    # show_image_with_rectangle(checker.world.screen, label_found)


if __name__ == '__main__':
  unittest.main()
