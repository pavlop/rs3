import threading
import time
from queue import Queue

import PIL
from PIL import Image

from resources.images_map import IMAGE_MAP, ScreenPart
from utils.menu_utils import identify_inventory_tab, inventory_slot_1
from utils.screen_utils import area_between_pictures, \
  MyLogger, take_screenshot, resize_area_keep_center


class WorldState(object):
  def __init__(self):
    self.screen = None
    self.full_area = None
    self.world_area = None
    self.need_mouse_move = True
    self.inventory_area = None
    self.inventory_slot_1 = None
    self.my_logger = MyLogger()
    self.queue = Queue(maxsize=0)

  def init_real_world(self):
    self.update_screen()
    self.update_game_area_with_corners(IMAGE_MAP[ScreenPart.ICON_ALL_CHATS],
                                       IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON])

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
      # queue_str = ' '.join(str(e) for e in self.queue)
      # self.my_logger.log_every(1, "Queue size:" + str(self.queue.qsize()))
      self.screen = take_screenshot()
      time.sleep(update_sec)

  def run_thread(self, delta_sec: float):
    world_state_thread = threading.Thread(target=self.keep_updating_screen, args=(delta_sec,))
    world_state_thread.start()
