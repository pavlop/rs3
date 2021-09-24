import time

import pyautogui

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import MyLogger, area_of_picture, take_screenshot
from utils.ui_interaction_utils import wait_until
from world.tasks import Tasks
from world.world_state import WorldState


class AnvilProcessor(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.my_logger = MyLogger()

  def process(self):
    self.my_logger.log("AnvilProcessor: START")

    def button_finder():
      return area_of_picture(take_screenshot(),
                             IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS]) is not None

    button_found = wait_until(predicate=button_finder, timeout_sec=3.0, poll_rate_sec=0.1)
    deposit_materials_button = area_of_picture(take_screenshot(), IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS])
    begin_project_button = area_of_picture(self.world.screen, IMAGE_MAP[ScreenPart.BUTTON_BEGIN_PROJECT])

    if button_found:
      pyautogui.click(x=deposit_materials_button.middle_x, y=deposit_materials_button.middle_y)
      time.sleep(0.5)
      pyautogui.click(x=begin_project_button.middle_x, y=begin_project_button.middle_y)
      self.my_logger.log("AnvilProcessor: clicked on begin_project_button")
      time.sleep(0.5)
      self.world.queue.put(Tasks.MOVE_MOUSE_UNTIL_ANVIL)
      self.world.queue.put(Tasks.CLICK_CURRENT)
      self.world.queue.put(Tasks.WAIT_10_SEC)
      self.world.queue.put(Tasks.WAIT_30_SEC)

    else:
      self.my_logger.log_every(100, "AnvilProcessor: is not on a menu, waiting")
      time.sleep(10)

    self.world.queue.put(Tasks.MOVE_MOUSE_UNTIL_FORGE)
    self.world.queue.put(Tasks.CLICK_CURRENT)
    self.world.queue.put(Tasks.PROCESS_FORGE)

    self.my_logger.log("AnvilProcessor: END")
