import pyautogui
import random

from screen.screen_utils import RectangularArea


class WorldInteractor(object):

  def move_mouse_in_area(area: RectangularArea, length_sec: float):
    step_sec = 0.5
    cur_time_sec = 0.0
    while cur_time_sec <= length_sec:
      cur_time_sec += step_sec
      new_x = area.top_x + random.randrange(0, area.width)
      new_y = area.top_y + random.randrange(0, area.height)
      pyautogui.moveTo(x=new_x, y=new_y, duration=step_sec, tween=pyautogui.easeInOutQuad)

