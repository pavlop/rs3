import unittest
import pyautogui


from src.screen.screenshoter import InitMarkup

class TestMapProvider(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(TestMapProvider, self).__init__(*args, **kwargs)
    test_screen = pyautogui.screenshot('../resources/test/example_full_screenshot.png')
    self.screenshoter = InitMarkup(screen = test_screen)


  def test_constructor(self):
    self.assertEqual(self.screenshoter.full_screen, '')

if __name__ == '__main__':
  unittest.main()


  # def test_path_to_directions_going_down(self):
  #   img_rgb1 = cv2.imread('test_data/map_trying_go_171_103.png')
  #   img_rgb2 = cv2.imread('test_data/map_wrong_path.png')
  #   img_rgb3 = cv2.imread('test_data/map_wrong_path2.png')
  #   img_rgb4 = cv2.imread('test_data/map_wrong_path3.png')
  #   img_rgb5 = cv2.imread('test_data/example_map2.png')
  #   img_rgb6 = cv2.imread('test_data/example_map1.png')
  #   print(self.m.locate_player(img_rgb1))
  #   print(self.m.locate_player(img_rgb2))
  #   print(self.m.locate_player(img_rgb3))
  #   print(self.m.locate_player(img_rgb4))
  #   print(self.m.locate_player(img_rgb5))
  #   print(self.m.locate_player(img_rgb6))


# create FakeProvider calss
# call mehod


# path = [(98, 99), (99, 99), (100, 99), (101, 99), (102, 99), (103, 99), (104, 99), (105, 99), (106, 99), (107, 99),
#         (108, 99), (109, 99), (110, 99), (111, 99), (112, 99), (113, 99), (114, 99), (115, 99), (116, 99),
#         (117, 99), (118, 99), (119, 99), (120, 99), (121, 99), (122, 99), (123, 99), (124, 99), (125, 99),
#         (126, 99), (127, 98)]
# directions = PathFinder.to_directions_with_time(PathFinder.path_to_directions(path))
# dir, time_sec = directions[0]
# self.assertEqual(Direction.DOWN, dir)
