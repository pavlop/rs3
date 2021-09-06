import random
import time
from typing import Callable

import pyautogui

from utils.screen_utils import RectangularArea


class WorldInteractor(object):

  def move_mouse_in_area(area: RectangularArea, length_sec: float):
    wait_sec = 0.5
    move_sec = 0.2
    cur_time_sec = 0.0
    while cur_time_sec <= length_sec:
      cur_time_sec += move_sec + wait_sec
      new_x = area.top_x + random.randrange(0, area.width)
      new_y = area.top_y + random.randrange(0, area.height)
      time.sleep(wait_sec)
      pyautogui.moveTo(x=new_x, y=new_y, duration=move_sec, tween=pyautogui.easeInOutQuad)

  def move_mouse_in_are_until(self, func: Callable):
    pass
