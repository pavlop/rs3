from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import RectangularArea, area_between_pictures


def identify_inventory_tab(screen) -> RectangularArea:
  icon_backpack_img = IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB]
  icon_view_your_wealth_inventory = IMAGE_MAP[ScreenPart.ICON_VIEW_YOUR_WEALTH_INVENTORY]

  area = area_between_pictures(screen, icon_backpack_img, icon_view_your_wealth_inventory)

  if area is None:
    print("Inventory tab is absent")
  else:
    print("Inventory tab found")

    icon_size_rows, icon_size_cols = icon_backpack_img.shape[:2]

    inventory_width = 2 * (icon_size_rows + area.bottom_x - area.top_x) + 20
    inventory_height = area.bottom_y - area.top_y

    inventory_start_x = area.top_x - 10
    inventory_start_y = area.top_y + icon_size_rows

    return RectangularArea(inventory_start_x, inventory_start_y, inventory_start_x + inventory_width,
                           inventory_start_y + inventory_height)


def inventory_slot_1(inventory: RectangularArea) -> RectangularArea:
  icon_backpack_img = IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB]
  height, width = icon_backpack_img.shape[:2]
  height += 15
  width += 15
  return RectangularArea(inventory.top_x, inventory.top_y, inventory.top_x + height,
                         inventory.top_y + width)
