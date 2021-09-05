import PIL
import cv2 as cv
import numpy
import numpy as np
import pyautogui
from src.resources import images_map

"""
Identify Areas of the game
"""
class InitMarkup(object):
  def __init__(self, screen: PIL.Image.Image):
    if screen:
      self.full_screen = self.screen
    else:
      self.full_screen = pyautogui.screenshot()  # returns a Pillow/PIL Image object, and saves it to a file

  # def identify_inventory_button(self):
  #   windowLocation = pyautogui.locateOnScreen('data/teleport_icon.png')

  # Box(left=1416, top=562, width=50, height=41)
  # self.game_screen_location = Box(left=0, top=0, width=500, height=500)

  # Returns (left, top, width, height)
  # windowLocation = pyautogui.locateOnScreen('data/teleport_icon.png')

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
