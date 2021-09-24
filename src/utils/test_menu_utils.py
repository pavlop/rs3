import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.menu_utils import inventory_slots_empty
from utils.screen_utils import show_image_with_rectangle


class TestMenuUtils(unittest.TestCase):

  # def testResizeVisualization(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
  #   top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
  #   bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
  #   area = area_between_pictures(screen, top, bottom)
  #   draw_rectangle(screen, resize_area_keep_center(area, 0.3))

  # def testDemoFistSlotInventory(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE]
  #   inventory = identify_inventory_tab(screen)
  #   first_slot = inventory_slot_1(inventory)
  #   show_image_with_rectangle(screen, first_slot)

  # def testDemoInventoryArea(self):
  #   screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE]
  #   inventory = identify_inventory_tab(screen)
  #   show_image_with_rectangle(screen, inventory)

  def testDemoInventorySlots(self):
    screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN_MINE]
    # screen = IMAGE_MAP[ScreenPart.TEST_INVENTORY_WOOD]
    empty_slot = inventory_slots_empty(screen)
    show_image_with_rectangle(screen, empty_slot)


if __name__ == '__main__':
  unittest.main()
