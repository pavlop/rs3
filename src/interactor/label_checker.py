import PIL
from PIL import Image

from utils.screen_utils import RectangularArea, area_of_picture


class LabelChecker(object):
  def __init__(self, mutable_screen: PIL.Image.Image, label: PIL.Image.Image, area: RectangularArea):
    self.mutable_screen = mutable_screen
    self.area = area
    self.label = label

  def check(self) -> RectangularArea:
    search_area = self.mutable_screen[self.area.top_y:self.area.bottom_y, self.area.top_x:self.area.bottom_x]
    return area_of_picture(search_area, self.label)
