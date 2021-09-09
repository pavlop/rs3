import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import area_of_picture, RectangularArea, show_image_with_rectangle
from world.mine_clicker import MineClicker


class MineClickerTest(unittest.TestCase):

  def testCheckMineLabel(self):
    # Not Found
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN1]
    full_area = area_of_picture(screen, screen)
    self.assertIsNone(MineClicker.mouse_position_on_mine(screen, full_area))

    # Found
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE]
    search_area = RectangularArea(100, 100, 1000, 1000)
    x, y = MineClicker.mouse_position_on_mine(screen, search_area)
    self.assertEqual((x, y), (926, 523))
    #
    mouse_area = RectangularArea(x, y, x, y)
    show_image_with_rectangle(screen, mouse_area)
