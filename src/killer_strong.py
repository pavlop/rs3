import time
from src import actions

class KillerStrong (object):
  # constructor
  def __init__(self, sec_per_monster):
    self.sec_per_monster = sec_per_monster
    self.iterations = 100
    self.actions = actions.Actions()

  def start(self) :
    for i in range(1, self.iterations):
      print("Start of iteration", i)
      self.actions.kill_next_target(self.sec_per_monster)
