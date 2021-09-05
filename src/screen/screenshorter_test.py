import unittest

import pyautogui

from src.screen.screenshoter import InitMarkup


class TestMapProvider(unittest.TestCase):

  # Constructor
  def __init__(self, *args, **kwargs):
    super(TestMapProvider, self).__init__(*args, **kwargs)

  def test_1(self):
    # Create fake screen
    test_screen = pyautogui.screenshot('../resources/test/example_full_screenshot.png')
    screenshoter = InitMarkup(screen=test_screen)
    # self.assertEqual(self.screenshoter.full_screen, '')
    screenshoter.identify_inventory_tab()


if __name__ == '__main__':
  unittest.main()
