import unittest

from src.resources.images_map import IMAGE_MAP
from src.resources.images_map import ScreenPart
from src.screen.screenshoter import InitMarkup


class TestMapProvider(unittest.TestCase):

  # Constructor
  def __init__(self, *args, **kwargs):
    super(TestMapProvider, self).__init__(*args, **kwargs)

  def test_identify_inventory_1(self):
    # Create fake screen
    fake_screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN1]
    screenshoter = InitMarkup(screen=fake_screen)
    screenshoter.identify_inventory_tab()

  def test_identify_inventory_2(self):
    # Create fake screen
    fake_screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN2]
    screenshoter = InitMarkup(screen=fake_screen)
    screenshoter.identify_inventory_tab()

  def test_identify_inventory_3(self):
    # Create fake screen
    fake_screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN3]
    screenshoter = InitMarkup(screen=fake_screen)
    screenshoter.identify_inventory_tab()


if __name__ == '__main__':
  unittest.main()
