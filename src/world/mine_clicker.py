import threading
import time

import pyautogui

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import MyLogger, RectangularArea, area_of_picture, show_image_with_rectangle
from world.world_state import WorldState


class MineClicker(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.area = world.world_area
    self.my_logger = MyLogger()

  @staticmethod
  def mouse_position_on_mine(screen, search_area) -> (int, int):
    search_screen = screen[search_area.top_y:search_area.bottom_y, search_area.top_x:search_area.bottom_x]
    area_result = area_of_picture(search_screen, IMAGE_MAP[ScreenPart.MINING_LABEL_ANY])
    if area_result is None:
      return None
    mouse_position_x = search_area.top_x + int(area_result.middle_x + 50)
    mouse_position_y = search_area.top_y + int(area_result.middle_y - 35)
    return mouse_position_x, mouse_position_y

  def check_mine_label(self) -> RectangularArea:
    if self.world.screen is None:
      return None
    search_screen = self.world.screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]
    area_result = area_of_picture(search_screen, IMAGE_MAP[ScreenPart.MINING_LABEL_ANY])
    return area_result

  def keep_clicking_mine(self, delta_check_sec=0.05):
    counter = 0

    while True:
      if self.world.need_mouse_move:
        time.sleep(delta_check_sec)
        # was_waiting = True
      else:
        counter += 1

        # Check again that label is visible
        # mine_coords = self.mouse_position_on_mine(self.world.screen, self.world.full_area)
        mine_coords = pyautogui.position()

        if mine_coords is None:
          self.my_logger.log("Tried to mine, but label is missing")
          show_image_with_rectangle(self.world.screen, self.world.full_area)
        else:
          self.my_logger.log("Starting Mining near label:" + str(mine_coords))
          # start mining
          pyautogui.click(mine_coords)
          time.sleep(5)
          # click on inventory 1st slot every 5 iterations
          if counter % 5 == 0:
            pyautogui.click(x=self.world.inventory_slot_1.middle_x, y=self.world.inventory_slot_1.middle_y)
            time.sleep(0.2)
        self.world.need_mouse_move = True

  def run_thread(self, delta_check_sec):
    mine_clicker_thread = threading.Thread(target=self.keep_clicking_mine, args=(delta_check_sec,))
    mine_clicker_thread.start()
