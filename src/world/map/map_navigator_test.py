import unittest
from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import RectangularArea, area_of_picture, take_screenshot, identify_inventory_tab, \
  show_image_with_rectangle, inventory_slot_1
from utils.screen_utils import area_between_pictures
from utils.screen_utils import resize_area_keep_center
import pyautogui
import time


class MapNavigatorTest(unittest.TestCase):

  def testDemoMinimap(self):
    time.sleep(2)
    screen = take_screenshot()
    bank_label = IMAGE_MAP[ScreenPart.BANK_MINIMAP_LABEL]
    center = area_of_picture(screen, bank_label).middle_x+5, area_of_picture(screen, bank_label).middle_y+5
    pyautogui.click(center)

    # show_image_with_rectangle(screen, area_of_picture(screen, bank_label))


if __name__ == '__main__':
  unittest.main()
