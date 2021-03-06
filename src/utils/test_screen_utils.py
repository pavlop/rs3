import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.menu_utils import identify_inventory_tab
from utils.screen_utils import RectangularArea, area_of_picture, take_screenshot, \
  show_image_with_rectangle, crop, area_of_picture_within_area
from utils.screen_utils import area_between_pictures
from utils.screen_utils import resize_area_keep_center


class TestMapProvider(unittest.TestCase):

  def testRectangularArea(self):
    area = RectangularArea(100, 100, 200, 200)
    self.assertEqual(area.middle_x, 150)
    self.assertEqual(area.middle_y, 150)

  def testAreaOfPicture(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    top_corner = IMAGE_MAP[ScreenPart.TEST_MARKERS_TOP_ORANGE]
    expected_area = RectangularArea(1, 2, 25, 26)
    self.assertEqual(expected_area, area_of_picture(screen, top_corner))

  def testAreaOfPicture(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    top_corner = IMAGE_MAP[ScreenPart.TEST_MARKERS_BOTTOM_RED]
    expected_area = RectangularArea(213, 181, 237, 205)
    self.assertEqual(expected_area, area_of_picture(screen, top_corner))

  def testAreaOfPictureAbsent(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    missing_img = IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB]
    self.assertEqual(None, area_of_picture(screen, missing_img))

  def testAreaForRealScreenshot(self):
    screen = take_screenshot()
    self.assertIsNotNone(area_of_picture(screen, screen))

  def testRectangularAreaTwoPictures(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    top = IMAGE_MAP[ScreenPart.TEST_MARKERS_TOP_ORANGE]
    bottom = IMAGE_MAP[ScreenPart.TEST_MARKERS_BOTTOM_RED]
    area = area_between_pictures(screen, top, bottom)
    expected_area = RectangularArea(1, 2, 237, 205)
    self.assertEqual(expected_area, area)

  def testResizeToSame(self):
    area = RectangularArea(top_x=0, top_y=0, bottom_x=100, bottom_y=100)
    self.assertEqual(resize_area_keep_center(area, 1.0), area)

  def testResizeToHalf(self):
    area = RectangularArea(top_x=0, top_y=0, bottom_x=100, bottom_y=100)
    expected_area = RectangularArea(top_x=25, top_y=25, bottom_x=75, bottom_y=75)
    self.assertEqual(resize_area_keep_center(area, 0.5), expected_area)

  # def testResizeVisualization(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
  #   top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
  #   bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
  #   area = area_between_pictures(screen, top, bottom)
  #   draw_rectangle(screen, resize_area_keep_center(area, 0.3))

  # def testDemoCrop(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
  #   area = RectangularArea(top_x=0, top_y=0, bottom_x=1000, bottom_y=300)
  #   cropped = crop(screen, area)
  #   show_image_with_rectangle(screen, None)
  #   show_image_with_rectangle(cropped, None)

  def testDemoFindWithin(self):
    screen = IMAGE_MAP[ScreenPart.TEST_INVENTORY_WOOD]
    empty_cell = IMAGE_MAP[ScreenPart.EMPTY_INVENTORY_CELL]
    inventory = identify_inventory_tab(screen)
    cropped = crop(screen, inventory)
    res = area_of_picture_within_area(screen, empty_cell, inventory, threshold=0.01)

    # show_image_with_rectangle(screen, None)
    show_image_with_rectangle(cropped, res)


if __name__ == '__main__':
  unittest.main()
