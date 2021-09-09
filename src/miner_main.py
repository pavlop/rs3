import logging
import os
import sys
import threading
import time

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import MyLogger
from world.mine_clicker import MineClicker
from world.sceen_area_checker import ScreenAreaChecker
from world.world_mouse_mover import WorldMouseMover
from world.world_state import WorldState


def main():
  my_logger = MyLogger()

  # Take first screenshot
  world = WorldState()
  world.update_screen()
  world.update_game_area_with_corners(IMAGE_MAP[ScreenPart.ICON_ALL_CHATS],
                                      IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON])
  # Area is the whole screen
  # area = area_of_picture(world_state.screen, world_state.screen)

  # Thread 1: Screen Updater
  my_logger.log("Main: start updating world")
  world_state_delta_sec = 0.1
  world_state_thread = threading.Thread(target=world.keep_updating_screen, args=(world_state_delta_sec,))
  world_state_thread.start()

  # Thread 2: Track Label
  my_logger.log("Main: start tracking label")
  label_checker_delta_sec = 0.05
  target_label = IMAGE_MAP[ScreenPart.MINING_LABEL_ANY]
  label_checker = ScreenAreaChecker(world, target_label, world.full_area)
  label_checker_thread = threading.Thread(target=label_checker.keep_checking_label, args=(label_checker_delta_sec,))
  label_checker_thread.start()

  # Thread 3: Mouse mover
  my_logger.log("Main: mouse mover")
  mouse_move_sec = 0.5
  mouse_mover = WorldMouseMover(world)
  mouse_mover_thread = threading.Thread(target=mouse_mover.keep_moving_mouse_in_area, args=(mouse_move_sec,))
  mouse_mover_thread.start()

  # Thread 4: MineClicker
  my_logger.log("Main: mine clicker")
  mine_clicker = MineClicker(world)
  mine_clicker_thread = threading.Thread(target=mine_clicker.keep_clicking_mine, args=(0.05,))
  mine_clicker_thread.start()

  # Main Thread: Quit Program
  # sleep 20 min
  time.sleep(20*60)
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
