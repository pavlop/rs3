import time

import PIL
import cv2 as cv
import pyautogui


class MapProvider(object):
  pass
  # def __init__(self):
  #   # self.def
  #   self.first_town_template = cv.imread('data/town.png', 0)
  #   self.last_town_template = cv.imread('data/last_town.png', 0)
  #   self.enemy_template = cv.imread('data/red_enemy.png', 0)
  #   self.player_template = cv.imread('data/player.png', 0)
  #   self.map_selector_template = cv.imread('data/map_selector.png', 0)
  #
  # def get_minimap(self) -> PIL.Image.Image:
  #   # Calling screenshot() will return an Image object (see the Pillow or PIL module documentation for details)
  #   ts = time.time()
  #   img = pyautogui.screenshot(region=(self.minimap_col, self.minimap_row, MINIMAP_X_SIZE, MINIMAP_Y_SIZE))
  #   print('taking screenshot get_minimap, time_sec=', round(time.time() - ts, 4))
  #   return img
