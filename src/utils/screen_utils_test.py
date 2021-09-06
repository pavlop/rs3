import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import RectangularArea, draw_rectangle, area_of_picture
from utils.screen_utils import area_between_pictures
from utils.screen_utils import resize_area_keep_center


class TestMapProvider(unittest.TestCase):

  # Constructor
  # def __init__(self, *args, **kwargs):
  #   super(TestMapProvider, self).__init__(*args, **kwargs)

  def testAreaOfPicture(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    top_corner = IMAGE_MAP[ScreenPart.TEST_MARKERS_SMALL_ORANGE]
    expected_area = RectangularArea(1, 1, 1, 1)
    self.assertEqual(expected_area, area_of_picture(screen, top_corner))

  def testRectangularAreaTwoPictures(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    top = IMAGE_MAP[ScreenPart.TEST_MARKERS_SMALL_ORANGE]
    bottom = IMAGE_MAP[ScreenPart.TEST_MARKERS_SMALL_RED]
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


if __name__ == '__main__':
  unittest.main()
