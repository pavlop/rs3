import threading
import time

import PIL
from PIL import Image

from utils.screen_utils import RectangularArea, area_of_picture, MyLogger
from world.world_state import WorldState


class ScreenAreaChecker(object):
  def __init__(self, world: WorldState, label: PIL.Image.Image, area: RectangularArea):
    self.world = world
    self.area = area
    self.label = label
    self.my_logger = MyLogger()

  def check(self) -> RectangularArea:
    if self.world.screen is None or self.area is None or self.label is None:
      return None
    search_screen = self.world.screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]
    area_result = area_of_picture(search_screen, self.label)
    # show_image_with_rectangle(search_screen, area_result)
    return area_result

  def keep_checking_label(self, update_sec=0.5):
    while True:
      label_found = self.check()
      if label_found is None:
        time.sleep(update_sec)
        continue
      self.my_logger.log_every(100, "label_found: " + str(label_found))
      self.world.need_mouse_move = False

  def run_thread(self, check_delta_sec: int):
    label_checker_thread = threading.Thread(target=self.keep_checking_label, args=(check_delta_sec,))
    label_checker_thread.start()
