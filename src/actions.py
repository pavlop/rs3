import time
import random
import pyautogui

class Actions (object):

  def next_target(self):
    pyautogui.hotkey('`')

  def attack_skill(self, char):
    pyautogui.hotkey(char)

  def sleep_random_sec(self, min_sec, max_sec):
    time.sleep(float(random.randrange(min_sec*10, max_sec*10))/10)

  def kill_next_target (self, sec_per_monster):
    self.next_target()
    self.sleep_random_sec(0, 0.1)
    self.next_target()
    self.sleep_random_sec(0, 1)
    self.attack_skill('1')
    self.attack_skill('2')
    self.sleep_random_sec(sec_per_monster, sec_per_monster+3)

# pyautogui.keyDown('d')
# a = actor.Actor()
# time.sleep(2.1)
# pyautogui.keyUp('d')
