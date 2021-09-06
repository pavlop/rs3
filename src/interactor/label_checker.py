import PIL
import cv2
from PIL import Image

from utils.screen_utils import RectangularArea


class LabelChecker(object):
  def __init__(self, mutable_screen: PIL.Image.Image, label: PIL.Image.Image, area: RectangularArea):
    self.mutable_screen = mutable_screen
    self.area = area
    self.label = label

  def check(self):
    search_area = self.mutable_screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]
    # print("search_area=",search_area)
    label_found = cv2.matchTemplate(search_area, self.label, cv2.TM_SQDIFF_NORMED)
    _, _, locaton, _ = cv2.minMaxLoc(label_found)
    # top_x, top_y = locaton
    return locaton
