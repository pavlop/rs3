import PIL
import cv2
import pyautogui

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import RectangularArea
from utils.screen_utils import area_between_pictures

"""
Identify Areas of the game screen.
"""


class InitMarkup(object):
  def __init__(self, screen: PIL.Image.Image):
    if screen is not None:
      self.full_screen = screen
    else:
      self.full_screen = pyautogui.screenshot()  # returns a Pillow/PIL Image object, and saves it to a file

  def identify_inventory_tab(self) -> RectangularArea:
    icon_backpack_img = IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB]
    icon_view_your_wealth_inventory = IMAGE_MAP[ScreenPart.ICON_VIEW_YOUR_WEALTH_INVENTORY]

    icon_backpack_found = cv2.matchTemplate(self.full_screen, icon_backpack_img, cv2.TM_SQDIFF_NORMED)
    icon_wealth_found = cv2.matchTemplate(self.full_screen, icon_view_your_wealth_inventory, cv2.TM_SQDIFF_NORMED)

    if icon_backpack_found is None:
      print("Inventory tab is absent")
    else:
      print("Inventory tab found")
      # We want the minimum squared difference
      _, _, mnLoc, _ = cv2.minMaxLoc(icon_backpack_found)
      backpack_x, backpack_y = mnLoc

      _, _, mnLoc, _ = cv2.minMaxLoc(icon_wealth_found)
      wealth_x, wealth_y = mnLoc

      icon_size_rows, icon_size_cols = icon_backpack_img.shape[:2]

      inventory_width = 2 * (icon_size_rows + wealth_x - backpack_x) + 20
      inventory_height = wealth_y - backpack_y

      inventory_start_x = backpack_x - 10
      inventory_start_y = backpack_y + icon_size_rows

      # Step 3: Draw the rectangle on large_image
      cv2.rectangle(self.full_screen, (inventory_start_x, inventory_start_y),
                    (inventory_start_x + inventory_width, inventory_start_y + inventory_height), (0, 0, 255), 2)

      # Display the original image with the rectangle around the match.
      cv2.imshow('output', self.full_screen)

      # The image is only displayed if we call this
      cv2.waitKey(0)

  def grab_game_screen(self, screen: PIL.Image.Image) -> RectangularArea:
    top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    return area_between_pictures(screen, top, bottom)
