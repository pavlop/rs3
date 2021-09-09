import unittest
from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import RectangularArea, area_of_picture, take_screenshot, identify_inventory_tab, \
  show_image_with_rectangle, inventory_slot_1
from utils.screen_utils import area_between_pictures
from utils.screen_utils import resize_area_keep_center
from utils.ui_interaction_utils import wait_until
import pyautogui
import time


class MapNavigatorTest(unittest.TestCase):
  first_town_icon = IMAGE_MAP[ScreenPart.FIRST_TOWN_TELEPORT_ICON]
  bank_label = IMAGE_MAP[ScreenPart.BANK_MINIMAP_LABEL]
  teleport_icon = IMAGE_MAP[ScreenPart.TELEPORT_MINIMAP_ICON]

  def testGoToBankeer(self):
    time.sleep(2)
    self.navigateToBankeer()

  def isIconVisible(self, icon):
    return area_of_picture(take_screenshot(), icon) is not None

  def teleportTo(self, destination):
    teleport_icon_location = area_of_picture(take_screenshot(), self.teleport_icon).middle_x, area_of_picture(
      take_screenshot(), self.teleport_icon).middle_y
    pyautogui.click(teleport_icon_location)
    wait_until(self.isIconVisible(destination), 1, 0.1)
    first_town_icon_location = area_of_picture(take_screenshot(), destination).middle_x, area_of_picture(
      take_screenshot(), destination).middle_y
    pyautogui.click(first_town_icon_location)
    time.sleep(25)

  def navigateToBankeer(self):
    self.teleportTo(self.first_town_icon)
    bankeer_location_first_town = area_of_picture(take_screenshot(), self.bank_label).middle_x + 5, area_of_picture(
      take_screenshot(), self.bank_label).middle_y + 5
    pyautogui.click(bankeer_location_first_town)


if __name__ == '__main__':
  unittest.main()
