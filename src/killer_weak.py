import time

from src import actions


class KillerWeak(object):
  # constructor
  def __init__(self, sec_per_monster: int, rest_after: int) -> None:
    self.sec_per_monster = sec_per_monster
    self.iterations = 1000
    self.rest_after = rest_after
    self.actions = actions.Actions()

  def start(self) -> None:
    for i in range(1, self.iterations):
      print("Killer iteration:", i)
      self.actions.kill_next_target(self.sec_per_monster)
      self.actions.kill_next_target(self.sec_per_monster)
      self.actions.kill_next_target(self.sec_per_monster)
      time.sleep(self.sec_per_monster)
