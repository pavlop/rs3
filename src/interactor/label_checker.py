import PIL
from PIL import Image


class LabelChecker(object):
  def __init__(self, mutable_screen: PIL.Image.Image, label: PIL.Image.Image):
    self.mutable_screen = mutable_screen
    self.label = label

  def __call__(self, arg1, arg2):
    pass
