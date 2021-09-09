import random
import time

import pyautogui


class KillActions(object):

  def random_float(self, val):
    float(random.randrange(val * 10000)) / 10000

  def next_target(self):
    pyautogui.hotkey('n')

  def attack_skill(self, char):
    pyautogui.hotkey(char)

  def sleep_random_sec(self, min_sec, max_sec):
    time.sleep(float(random.randrange(min_sec * 100, max_sec * 100)) / 100)

  def kill_next_target(self, sec_per_monster):
    self.next_target()
    self.sleep_random_sec(0, 0.1)
    self.next_target()
    self.sleep_random_sec(0, 1)
    self.attack_skill('1')
    self.attack_skill('2')
    self.sleep_random_sec(sec_per_monster, sec_per_monster + 3)

  # def rotate_map(self):
  #   pyautogui.mouseDown(button='middle')
  #   # pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
  #   # pyautogui.move(0, 50)  # move the mouse down 50 pixels.
  #   pyautogui.move(30, 0, 2)  # move the mouse right 30 pixels over 2 seconds.
  #   pyautogui.move(-30, 0, 2)  # move the mouse left 30 pixels over 2 seconds.
  #   # pyautogui.move(-30, None)  # move the mouse left 30 pixels.
  #   pyautogui.mouseUp(button='middle')

# pyautogui.keyDown('d')
# a = actor.Actor()
# time.sleep(2.1)
# pyautogui.keyUp('d')
