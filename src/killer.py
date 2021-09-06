import time

from src import actions


class KillerScript(object):
  # constructor
  def __init__(self, sec_per_monster: int, rest_after_n_iterations: int = 10) -> None:
    self.sec_per_monster = sec_per_monster
    self.iterations = 100
    self.rest_after_n_iterations = rest_after_n_iterations
    self.sec_to_rest = 15
    self.actions = actions.Actions()

  def start(self) -> None:
    start_time = time.time()
    for i in range(0, self.iterations):
      for j in range(0, self.rest_after_n_iterations):
        print("Killer iteration:", i, "time:", round(time.time() - start_time, 1))
        self.actions.kill_next_target(self.sec_per_monster)
      print("Resting to heal")
      time.sleep(self.sec_to_rest)
