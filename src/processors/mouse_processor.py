import random
import time
from itertools import cycle
from typing import Callable

import pyautogui

from utils.screen_utils import MyLogger
from utils.ui_interaction_utils import do_until
from world.world_state import WorldState


class MouseProcessor(object):
  def __init__(self, world: WorldState):
    self.world = world
    self.area = world.world_area
    self.move_duration = 0.05
    self.my_logger = MyLogger()
    self.deltas = cycle([-100, 100, -200, 200, -300, 300, -400, 400])

  def center_spot(self):
    new_x = self.area.top_x + int(self.area.width / 2)
    new_y = self.area.top_y + int(self.area.height / 2)
    return new_x, new_y

  def horizontal_spot_from_center(self):
    new_x, new_y = self.center_spot()
    new_x = new_x + next(self.deltas)
    # new_x = cur_x + 250 - random.randrange(0, 500)
    # Make sure in area
    if new_x < self.area.top_x or new_x > self.area.bottom_x:
      return self.center_spot()
    return new_x, new_y

  def random_spot_nearby(self):
    cur_x, cur_y = pyautogui.position()
    new_x = cur_x + 100 - random.randrange(0, 200)
    new_y = cur_y + 100 - random.randrange(0, 200)

    # Make sure in area
    if new_x < self.area.top_x or new_x > self.area.bottom_x:
      return self.center_spot()
    if new_y < self.area.top_y or new_y > self.area.bottom_y:
      return self.center_spot()

    return new_x, new_y

  def move_center(self):
    new_x, new_y = self.center_spot()
    pyautogui.moveTo(x=new_x, y=new_y, duration=self.move_duration, tween=pyautogui.easeInOutQuad)

  def move_mouse_nearby_in_area(self, sleep_sec=0.3):
    new_x, new_y = self.horizontal_spot_from_center()
    pyautogui.moveTo(x=new_x, y=new_y, duration=self.move_duration, tween=pyautogui.easeInOutQuad)
    time.sleep(sleep_sec)

  def move_mouse_until(self, predicate: Callable):
    self.move_center()
    do_until(self.move_mouse_nearby_in_area, predicate)
