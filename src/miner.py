import logging
import threading
import time

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from utils.screen_utils import MyLogger
from world.label_checker import LabelChecker
from world.world_interactor import WorldMouseMover
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
  label_checker_delta_sec = 0.1
  target_label = IMAGE_MAP[ScreenPart.MINING_LABEL_ANY]
  label_checker = LabelChecker(world, target_label, world.full_area)
  label_checker_thread = threading.Thread(target=label_checker.keep_checking_label, args=(label_checker_delta_sec,))
  label_checker_thread.start()

  # Thread 3: Mouse mover
  my_logger.log("Main: mouse mover")
  mouse_move_sec = 0.5
  mouse_mover = WorldMouseMover(world)
  mouse_mover_thread = threading.Thread(target=mouse_mover.keep_moving_mouse_in_area, args=(mouse_move_sec,))
  mouse_mover_thread.start()

  my_logger.log("Main: Done")

  # # screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
  # screen = numpy.array(pyautogui.screenshot())
  # # screen = take_screenshot()
  # area = area_of_picture(screen, screen)
  # #
  # # top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
  # # bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
  # target_label = IMAGE_MAP[ScreenPart.ATTACK_LABEL]
  # logging.info("Searching for target_label", target_label)
  # # area = area_between_pictures(screen, top, bottom)
  #
  # # Pause
  # show_image_with_rectangle(screen, area)
  #
  #
  # # Main objects
  # checker = LabelChecker(screen, target_label, area)
  # interactor = WorldInteractor()
  #
  # # Thread that updates screenshots
  # interactor_updater = WorldInteractorUpdater(interactor)
  # screenshoter_thread = threading.Thread(target=interactor_updater.keep_updating, args=())
  # logging.info("Main    : before running screenshoter_thread")
  # screenshoter_thread.start()
  #
  # # Thread that moves mouse
  # # time.sleep(1)
  # # checker_thread = threading.Thread(target=interactor.continue_check, args=(checker,))
  # # logging.info("Main    : before running checker_thread")
  # # checker_thread.start()
  # #
  # # logging.info("Main    : wait for the thread to finish")
  # # # x.join()
  # # logging.info("Main    : all done")


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
