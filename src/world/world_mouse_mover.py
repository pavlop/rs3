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
    self.move_duration = 0.1
    self.my_logger = MyLogger()

  def random_spot(self):
    new_x = self.area.top_x + random.randrange(0, self.area.width)
    new_y = self.area.top_y + random.randrange(0, self.area.height)
    return new_x, new_y

  def random_spot_nearby(self):
    cur_x, cur_y = pyautogui.position()
    new_x = cur_x + 150 - random.randrange(0, 300)
    new_y = cur_y + 150 - random.randrange(0, 300)

    # Make sure in area
    new_x = max(self.area.top_x, new_x)
    new_x = min(self.area.bottom_x, new_x)
    new_y = max(self.area.top_y, new_y)
    new_y = min(self.area.bottom_y, new_y)

    return new_x, new_y

  def move_mouse_in_area(self):
    new_x, new_y = self.random_spot()
    pyautogui.moveTo(x=new_x, y=new_y, duration=self.move_duration, tween=pyautogui.easeInOutQuad)

  def move_mouse_nearby_in_area(self):
    new_x, new_y = self.random_spot_nearby()
    pyautogui.moveTo(x=new_x, y=new_y, duration=self.move_duration, tween=pyautogui.easeInOutQuad)

  def keep_moving_mouse_in_area(self, step_sec=0.3):
    wait_time = step_sec - self.move_duration
    assert wait_time > 0.1, "Wait time should be positive. Increase step_sec."
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
