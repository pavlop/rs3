import pyautogui

from screen.screen_utils import RectangularArea


class WorldInteractor(object):

  def move_mouse_in_area(self, area: RectangularArea):
    pyautogui.moveTo(x=area.top_x, y=area.top_y, duration=0.1, tween=linear)

