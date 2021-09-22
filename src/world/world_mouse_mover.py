import random
import threading
import time

import pyautogui

from utils.screen_utils import MyLogger
from world.world_state import WorldState


class WorldMouseMover(object):
  def __init__(self, world: WorldState):
    self.world = world
    self.area = world.world_area
    self.move_duration = 0.05
    self.my_logger = MyLogger()

  def center_spot(self):
    new_x = self.area.top_x + int(self.area.width / 2)
    new_y = self.area.top_y + int(self.area.height / 2)
    return new_x, new_y

  def random_spot(self):
    new_x = self.area.top_x + random.randrange(0, self.area.width)
    new_y = self.area.top_y + random.randrange(0, self.area.height)
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

  def move_mouse_in_area(self):
    new_x, new_y = self.center_spot()
    pyautogui.moveTo(x=new_x, y=new_y, duration=self.move_duration, tween=pyautogui.easeInOutQuad)

  def move_mouse_nearby_in_area(self):
    new_x, new_y = self.random_spot_nearby()
    pyautogui.moveTo(x=new_x, y=new_y, duration=self.move_duration, tween=pyautogui.easeInOutQuad)

  def keep_moving_mouse_in_area(self, step_sec=1):
    wait_time = step_sec - self.move_duration
    assert wait_time > 0.0, "Wait time should be positive. Increase step_sec."
    self.move_mouse_in_area()

    was_waiting = True

    while True:
      if self.world.need_mouse_move:
        if was_waiting:
          self.move_mouse_in_area()
          was_waiting = False
        else:
          self.my_logger.log_every(1000, "Moving mouse")
          self.move_mouse_nearby_in_area()
        time.sleep(wait_time)
      else:
        was_waiting = True
        time.sleep(2)

  def run_thread(self, mouse_move_sec):
    mouse_mover_thread = threading.Thread(target=self.keep_moving_mouse_in_area, args=(mouse_move_sec,))
    mouse_mover_thread.start()
