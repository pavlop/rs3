import unittest

from interactor.world_interactor import WorldInteractor
from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from src.screen.screen_utils import RectangularArea
from src.screen.screen_utils import area_between_pictures
from src.screen.screen_utils import draw_rectangle
from src.screen.screen_utils import resize_area_keep_center


class WorldInteractorTest(unittest.TestCase):

  def testMoveMouseInArea(self):

    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    area = area_between_pictures(screen, top, bottom)
    area = resize_area_keep_center(area, 0.5)
    WorldInteractor.move_mouse_in_area(area=area, length_sec=10)
    draw_rectangle(screen, area)


if __name__ == '__main__':
  unittest.main()
