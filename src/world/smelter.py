import threading
import time

import pyautogui

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import MyLogger, area_of_picture, show_image_with_rectangle, take_screenshot
from world.world_state import WorldState


class Smelter(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.my_logger = MyLogger()

  def smith_iteration(self):
    time.sleep(1)
    deposit_materials_button = area_of_picture(take_screenshot(), IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS],
                                               threshold=0.7)
    if deposit_materials_button is None:
      self.my_logger.log("deposit_materials_button not found")
      # show_image_with_rectangle(IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS], None)
    else:
      pyautogui.click(x=deposit_materials_button.middle_x, y=deposit_materials_button.middle_y)
      time.sleep(2)

    begin_project_button = area_of_picture(self.world.screen, IMAGE_MAP[ScreenPart.BUTTON_BEGIN_PROJECT], threshold=0.7)
    if begin_project_button is None:
      self.my_logger.log("begin_project_button not found")
      show_image_with_rectangle(self.world.screen, None)

    pyautogui.click(x=begin_project_button.middle_x, y=begin_project_button.middle_y)
    self.my_logger.log("clicked on begin_project_button" + str(begin_project_button))

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
