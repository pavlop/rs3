import PIL
import cv2
from PIL import Image


class RectangularArea(object):
    def __init__(self, top_x: int, top_y: int, bottom_x: int, bottom_y: int):
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x
        self.bottom_y = bottom_y

        self.height = bottom_x - top_x
        self.width = bottom_y - top_y

    def __eq__(self, other):
        # return True
        if isinstance(other, self.__class__):
            # return self.top_x == other.top_x
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())


def area_between_pictures(screen: PIL.Image.Image, top_corner_img: PIL.Image.Image,
                          bottom_corner_img: PIL.Image.Image) -> RectangularArea:
    top_found = cv2.matchTemplate(screen, top_corner_img, cv2.TM_SQDIFF_NORMED)
    bottom_found = cv2.matchTemplate(screen, bottom_corner_img, cv2.TM_SQDIFF_NORMED)

    # Coordinates of top picturematchTemplate
    _, _, locaton, _ = cv2.minMaxLoc(top_found)
    top_x, top_y = locaton

    # Coordinates of bottom picture
    _, _, locaton, _ = cv2.minMaxLoc(bottom_found)
    bottom_x, bottom_y = locaton

    # Size of bottom picture should be included.
    bottom_img_height, bottom_img_width = bottom_corner_img.shape[:2]

    return RectangularArea(top_x, top_y, bottom_x + bottom_img_height, bottom_y + bottom_img_width)


def draw_rectangle(screen: PIL.Image.Image, area: RectangularArea):
    cv2.rectangle(img=screen, pt1=(area.top_x, area.top_y), pt2=(area.bottom_x, area.bottom_y), color=(50, 200, 50),
                  thickness=2)
    # Display the original image with the rectangle around the match.
    cv2.imshow('output', screen)
    # The image is only displayed if we call this
    cv2.waitKey(0)


# Reduces size of a square, keeps the center as is.
def resize_area_keep_center(area: RectangularArea, resize_coefficient: float) -> RectangularArea:
    new_height = int(area.height*resize_coefficient)
    new_width = int(area.width*resize_coefficient)

    height_delta = area.height - new_height
    width_delta = area.width - new_width

    top_x = int(area.top_x +height_delta/2)
    top_y = int(area.top_y + width_delta/2)
    bottom_x = int(area.bottom_x - height_delta/2)
    bottom_y = int(area.bottom_y - width_delta/2)
    return RectangularArea(top_x, top_y, bottom_x, bottom_y)

def area_of_picture(screen: PIL.Image.Image, label: PIL.Image.Image) -> RectangularArea:
    label_found = cv2.matchTemplate(screen, label, cv2.TM_SQDIFF_NORMED)
    _, _, locaton, _ = cv2.minMaxLoc(label_found)
    top_x, top_y = locaton
    # Size of bottom picture should be included.
    label_height, label_width = label.shape[:2]
    return RectangularArea(top_x, top_y, top_x + label_width, top_y + label_height)