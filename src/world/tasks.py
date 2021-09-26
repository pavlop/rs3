from enum import Enum


class Tasks(Enum):
  CLICK_CURRENT = 0
  PROCESS_ANVIL = 1
  PROCESS_FORGE = 2
  PROCESS_MINE = 3

  MOVE_MOUSE_UNTIL_ANVIL = 100
  MOVE_MOUSE_UNTIL_FORGE = 101
  MOVE_MOUSE_UNTIL_MINE = 102

  WAIT_10_SEC = 200
  WAIT_20_SEC = 201
  WAIT_30_SEC = 202

  def __str__(self):
    return str(self.name)
