import threading
import time

from processors.anvil_processor import AnvilProcessor
from processors.forge_processor import ForgeProcessor
from processors.mouse_processor import MouseProcessor
from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import click_current
from world.sceen_area_checker import ScreenAreaChecker
from world.tasks import Tasks
from world.world_state import WorldState


class GodProcessor(object):
  def __init__(self, world: WorldState, forge_processor: ForgeProcessor, anvil_processor: AnvilProcessor,
               mouse_processor: MouseProcessor):
    self.world = world
    self.forge_processor = forge_processor
    self.anvil_processor = anvil_processor
    self.mouse_processor = mouse_processor

  def continuous_check(self):
    while True:
      task = self.world.queue.get(block=True)

      if task == Tasks.CLICK_CURRENT:
        click_current()
        pass

      if task == Tasks.MOVE_MOUSE_UNTIL_ANVIL or task == Tasks.MOVE_MOUSE_UNTIL_FORGE:
        # Process Moving
        if task == Tasks.MOVE_MOUSE_UNTIL_ANVIL:
          label = IMAGE_MAP[ScreenPart.SMITH_LABEL]
        elif task == Tasks.MOVE_MOUSE_UNTIL_FORGE:
          label = IMAGE_MAP[ScreenPart.HEAT_LABEL]
        label_checker = ScreenAreaChecker(self.world, label, self.world.full_area)
        self.mouse_processor.move_mouse_until(label_checker.check)
        # self.mouse_processor.move_center()
        # do_until(self.mouse_processor.move_mouse_nearby_in_area, label_checker.check)

      if task == Tasks.PROCESS_ANVIL:
        self.anvil_processor.process()
      if task == Tasks.PROCESS_FORGE:
        self.forge_processor.process()

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
