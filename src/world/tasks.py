from enum import Enum


class Tasks(Enum):
  CLICK_CURRENT = 0
  MOVE_MOUSE_UNTIL_ANVIL = 1
  MOVE_MOUSE_UNTIL_FORGE = 2
  PROCESS_ANVIL = 3
  PROCESS_FORGE = 4
  WAIT_10_SEC = 5
  WAIT_20_SEC = 6
  WAIT_30_SEC = 7
