import time

import PIL
import pyautogui
from PIL import Image

from utils.screen_utils import RectangularArea, area_of_picture, MyLogger
from world.world_state import WorldState


class LabelChecker(object):
  def __init__(self, world: WorldState, label: PIL.Image.Image, area: RectangularArea):
    self.world = world
    self.area = area
    self.label = label
    self.my_logger = MyLogger()

  def check(self) -> RectangularArea:
    if self.world.screen is None or self.area is None or self.label is None:
      return None
    search_screen = self.world.screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]
    # search_screen = self.mutable_screen.crop(self.area.top_x,  self.area.top_y, self.area.bottom_x, self.area.bottom_y)
    area_result = area_of_picture(search_screen, self.label)
    # show_image_with_rectangle(search_screen, area_result)
    return area_result

  def keep_checking_label(self, update_sec=0.5):

    while True:
      label_found = self.check()
      self.my_logger.log_every(5, "label_found=" + str(label_found))

      if label_found is None:
        time.sleep(update_sec)
        continue

      self.my_logger.log("LABEL FOUND: " + str(label_found))
      self.world.need_mouse_move = False

      # start mining
      pyautogui.click()
      time.sleep(5)

      # Click on inventory
      pyautogui.click(x=self.world.inventory_slot_1.middle_x, y=self.world.inventory_slot_1.middle_y)
      self.world.need_mouse_move = True
