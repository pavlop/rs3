import pyautogui

from utils.screen_utils import MyLogger
from world.tasks import Tasks
from world.world_state import WorldState


class MineProcessor(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.my_logger = MyLogger()
    self.counter = 0

  def process(self):
    self.my_logger.log("MineProcessor: start")

    # click on inventory 1st slot every 5 iterations
    self.counter += 1
    if self.counter % 5 == 0:
      pyautogui.click(x=self.world.inventory_slot_1.middle_x, y=self.world.inventory_slot_1.middle_y)

    self.world.queue.put(Tasks.MOVE_MOUSE_UNTIL_MINE)
    self.world.queue.put(Tasks.CLICK_CURRENT)
    self.world.queue.put(Tasks.WAIT_10_SEC)
    self.world.queue.put(Tasks.PROCESS_MINE)
