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

  def testGoToBankeer(self):
    time.sleep(2)
    screen = take_screenshot()
    bank_label = IMAGE_MAP[ScreenPart.BANK_MINIMAP_LABEL]
    teleport_icon = IMAGE_MAP[ScreenPart.TELEPORT_MINIMAP_ICON]
    first_town_icon = IMAGE_MAP[ScreenPart.FIRST_TOWN_TELEPORT_ICON]

    teleport_icon_location = area_of_picture(screen, teleport_icon).middle_x, area_of_picture(screen, teleport_icon).middle_y
    pyautogui.click(teleport_icon_location)
    time.sleep(1)
    screen = take_screenshot()

    first_town_icon_location = area_of_picture(screen, first_town_icon).middle_x, area_of_picture(screen, first_town_icon).middle_y
    pyautogui.click(first_town_icon_location)
    time.sleep(25)
    screen = take_screenshot()

    bankeer_location_first_town = area_of_picture(screen, bank_label).middle_x+5, area_of_picture(screen, bank_label).middle_y+5
    pyautogui.click(bankeer_location_first_town)

    # show_image_with_rectangle(screen, area_of_picture(screen, bank_label))


if __name__ == '__main__':
  unittest.main()
