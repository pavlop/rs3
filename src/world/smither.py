import threading
import time

import pyautogui

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import MyLogger, RectangularArea, area_of_picture, show_image_with_rectangle
from world.world_state import WorldState


class Smither(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.area = world.world_area
    self.my_logger = MyLogger()

  def keep_smithing(self, delta_check_sec=0.05):
    deposit_materials_button = BUTTON_DEPOSIT_ALL_MATERIALS
    begin_project_button = area_of_picture(self.world.screen, IMAGE_MAP[ScreenPart.BUTTON_BEGIN_PROJECT])






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
