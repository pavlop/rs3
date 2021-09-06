import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from src.screen.screen_utils import RectangularArea
from src.screen.screen_utils import area_between_pictures
from src.screen.screen_utils import draw_rectangle
from src.screen.screen_utils import resize_area_keep_center


class TestMapProvider(unittest.TestCase):

  # Constructor
  # def __init__(self, *args, **kwargs):
  #   super(TestMapProvider, self).__init__(*args, **kwargs)

  def testRectangularArea(self):
    screen = IMAGE_MAP[ScreenPart.TEST_TWO_MARKERS_SMALL]
    top = IMAGE_MAP[ScreenPart.TEST_MARKERS_SMALL_ORANGE]
    bottom = IMAGE_MAP[ScreenPart.TEST_MARKERS_SMALL_RED]
    area = area_between_pictures(screen, top, bottom)
    expected_area = RectangularArea(1, 2, 237, 205)
    self.assertEqual(expected_area, area)

  def testResize(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    area = area_between_pictures(screen, top, bottom)
    area = resize_area_keep_center(area, 0.5)
    # draw_rectangle(screen, area)


if __name__ == '__main__':
  unittest.main()
