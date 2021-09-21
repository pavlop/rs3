import threading
import time

import PIL
import numpy
import pyautogui
from PIL import Image

from utils.screen_utils import area_between_pictures, \
  MyLogger, take_screenshot, resize_area_keep_center, identify_inventory_tab, inventory_slot_1


class WorldState(object):
  def __init__(self):
    self.screen = None
    self.full_area = None
    self.world_area = None
    self.need_mouse_move = True
    self.inventory_area = None
    self.inventory_slot_1 = None
    self.my_logger = MyLogger()

  def update_screen_with_img(self, fake_screen: PIL.Image.Image):
    self.screen = fake_screen

  def update_screen(self):
    self.update_screen_with_img(take_screenshot())

  def update_game_area_with_corners(self, top_corner_img: PIL.Image.Image,
                                    bottom_corner_img: PIL.Image.Image):
    self.full_area = area_between_pictures(self.screen, top_corner_img, bottom_corner_img)
    self.world_area = resize_area_keep_center(self.full_area, 0.5)
    self.inventory_area = identify_inventory_tab(self.screen)
    self.inventory_slot_1 = inventory_slot_1(self.inventory_area)

  def keep_updating_screen(self, update_sec=0.5):
    while True:
      self.my_logger.log_every(100, "Taking screenshot")
      self.screen = take_screenshot()
      time.sleep(update_sec)

  def run_thread(self, delta_sec: int):
    world_state_thread = threading.Thread(target=self.keep_updating_screen, args=(delta_sec,))
    world_state_thread.start()
