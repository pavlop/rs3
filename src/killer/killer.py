import time

from killer import actions


class KillerScript(object):
  # constructor
  def __init__(self, sec_per_monster: int, rest_after_n_iterations=3, rest_sec=15) -> None:
    self.sec_per_monster = sec_per_monster
    self.iterations = 200
    self.rest_after_n_iterations = rest_after_n_iterations
    self.sec_to_rest = rest_sec
    self.actions = actions.KillActions()

  def start(self) -> None:
    start_time = time.time()
    for i in range(0, self.iterations):
      for j in range(0, self.rest_after_n_iterations):
        print("Killer iteration:", i, "time:", round(time.time() - start_time, 1))
        self.actions.kill_next_target(self.sec_per_monster)
      print("Resting to heal for ", self.sec_to_rest)
      time.sleep(self.sec_to_rest)
