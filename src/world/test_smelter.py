import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import area_of_picture, RectangularArea, show_image_with_rectangle
from world.mine_clicker import MineClicker


class MineClickerTest(unittest.TestCase):

  def testChecButtonsLabel(self):
    #  Found
    screen = IMAGE_MAP[ScreenPart.TEST_FULL_SCREENSHOT_SMELT_INTERFACE]
    button_deposit = area_of_picture(screen, IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS])
    button_begin_project = area_of_picture(screen, IMAGE_MAP[ScreenPart.BUTTON_BEGIN_PROJECT])
    self.assertIsNotNone(button_deposit)
    self.assertIsNotNone(button_begin_project)
    # show_image_with_rectangle(screen, button_deposit)
    # show_image_with_rectangle(screen, button_begin_project)
