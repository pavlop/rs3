from resources.images_map import IMAGE_MAP, ScreenPart
from utils.screen_utils import MyLogger, area_of_picture, take_screenshot
from utils.ui_interaction_utils import wait_until
from world.tasks import Tasks
from world.world_state import WorldState


class ForgeProcessor(object):

  def __init__(self, world: WorldState):
    self.world = world
    self.my_logger = MyLogger()

  def process(self):
    self.my_logger.log("ForgeProcessor: start")

    # Check if creation window is created
    def button_finder():
      return area_of_picture(take_screenshot(),
                             IMAGE_MAP[ScreenPart.BUTTON_DEPOSIT_ALL_MATERIALS]) is not None

    button_found = wait_until(predicate=button_finder, timeout_sec=3.0, poll_rate_sec=0.1)
    if button_found:
      self.world.queue.put(Tasks.PROCESS_ANVIL)
    else:
      self.world.queue.put(Tasks.MOVE_MOUSE_UNTIL_ANVIL)
      self.world.queue.put(Tasks.CLICK_CURRENT)
      self.world.queue.put(Tasks.PROCESS_ANVIL)
