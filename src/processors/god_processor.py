import threading
import time

from processors.anvil_processor import AnvilProcessor
from processors.forge_processor import ForgeProcessor
from processors.mine_processor import MineProcessor
from processors.mouse_processor import MouseProcessor
from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import click_current
from world.sceen_area_checker import ScreenAreaChecker
from world.tasks import Tasks
from world.world_state import WorldState


class GodProcessor(object):
  def __init__(self, world: WorldState = None, forge_processor: ForgeProcessor = None,
               anvil_processor: AnvilProcessor = None,
               mouse_processor: MouseProcessor = None, mine_processor: MineProcessor = None):
    self.world = world
    self.forge_processor = forge_processor
    self.anvil_processor = anvil_processor
    self.mouse_processor = mouse_processor
    self.mine_processor = mine_processor

  def continuous_check(self):
    while True:
      task = self.world.queue.get(block=True)

      if task == Tasks.CLICK_CURRENT:
        click_current()
        pass

      if str(task).startswith("MOVE_MOUSE_UNTIL_"):
        # Process Moving
        if task == Tasks.MOVE_MOUSE_UNTIL_ANVIL:
          label = IMAGE_MAP[ScreenPart.SMITH_LABEL]
        elif task == Tasks.MOVE_MOUSE_UNTIL_FORGE:
          label = IMAGE_MAP[ScreenPart.HEAT_LABEL]
        elif task == Tasks.MOVE_MOUSE_UNTIL_MINE:
          label = IMAGE_MAP[ScreenPart.MINING_LABEL_ANY]
        else:
          print("ERROR: No label found for task:", str(task))
        label_checker = ScreenAreaChecker(self.world, label, self.world.full_area)
        self.mouse_processor.move_mouse_until(label_checker.check)

      if task == Tasks.PROCESS_ANVIL:
        self.anvil_processor.process()
      if task == Tasks.PROCESS_FORGE:
        self.forge_processor.process()
      if task == Tasks.PROCESS_MINE:
        self.mine_processor.process()

      if task == Tasks.WAIT_10_SEC:
        print("Sleeping for 10 sec ...")
        time.sleep(10)
      if task == Tasks.WAIT_20_SEC:
        time.sleep(20)
        print("Sleeping for 20 sec ...")
      if task == Tasks.WAIT_30_SEC:
        time.sleep(30)
        print("Sleeping for 30 sec ...")

  def run_thread(self):
    mouse_mover_thread = threading.Thread(target=self.continuous_check, args=())
    mouse_mover_thread.start()
