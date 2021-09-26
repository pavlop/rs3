import logging
import os
import time

from processors.god_processor import GodProcessor
from processors.mine_processor import MineProcessor
from processors.mouse_processor import MouseProcessor
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
  god = GodProcessor(world, mine_processor=MineProcessor(world), mouse_processor=MouseProcessor(world))
  god.run_thread()

  world.queue.put(Tasks.PROCESS_MINE)

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
