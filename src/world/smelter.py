import os
import threading
import time

import pyautogui

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import MyLogger, RectangularArea, area_of_picture, show_image_with_rectangle, take_screenshot
from world.world_state import WorldState


class Smelter(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.my_logger = MyLogger()

  def smith_iteration(self):
    time.sleep(2)
    deposit_materials_button = area_of_picture(self.world.screen, IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS])
    # if deposit_materials_button is None:
    #   os._exit(1)
    # show_image_with_rectangle(self.world.screen, None)
    # show_image_with_rectangle(IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS], None)

    pyautogui.click(x=deposit_materials_button.middle_x, y=deposit_materials_button.middle_y)
    time.sleep(2)

    begin_project_button = area_of_picture(self.world.screen, IMAGE_MAP[ScreenPart.BUTTON_BEGIN_PROJECT])
    pyautogui.click(x=begin_project_button.middle_x, y=begin_project_button.middle_y)
    self.my_logger.log("Cliecked on begin_project_button" + str(begin_project_button))
    time.sleep(2)


  def keep_smithing(self, project_sec=120):
    while True:
      if self.world.need_mouse_move:
        time.sleep(0.05)
      else:
        self.my_logger.log("Smithing start project")
        furnace_coords = pyautogui.position()
        pyautogui.click(furnace_coords)
        time.sleep(0.2)
        self.smith_iteration()
        time.sleep(project_sec)
        self.world.need_mouse_move = True


  def run_thread(self, project_sec):
    mine_clicker_thread = threading.Thread(target=self.keep_smithing, args=(project_sec,))
    mine_clicker_thread.start()
