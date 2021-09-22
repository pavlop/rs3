import logging
import os
import time

from processors.anvil_processor import AnvilProcessor
from processors.forge_processor import ForgeProcessor
from processors.god_processor import GodProcessor
from processors.mouse_processor import MouseProcessor
from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import MyLogger
from world.tasks import Tasks
from world.world_state import WorldState


def main():
  my_logger = MyLogger()

  # Thread 1: Screen Updater
  world = WorldState()
  world.init_real_world()
  world.run_thread(delta_sec=0.1)

  # Processors
  god = GodProcessor(world, ForgeProcessor(world), AnvilProcessor(world), MouseProcessor(world))
  god.run_thread()

  world.queue.put(Tasks.MOVE_MOUSE_UNTIL_ANVIL)
  world.queue.put(Tasks.CLICK_CURRENT)
  world.queue.put(Tasks.PROCESS_ANVIL)


  # Main Thread: Quit Program
  time.sleep(4 * 60 * 60)
  my_logger.log("Main: Done")
  os._exit(1)


if __name__ == "__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO,
                      datefmt="%H:%M:%S")
  print("3...")
  time.sleep(0.5)
  print("2...")
  time.sleep(0.5)
  print("1...")
  time.sleep(0.5)
  print("satrted")
  main()
