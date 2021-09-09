import unittest


class WorldInteractorTest(unittest.TestCase):

  def testMoveMouseInAreaDemo(self):
    pass
    # screen = IMAGE_MAP[ScreenPart.TEST_SCREENSHOT_FULL_SCREEN4]
    # top = IMAGE_MAP[ScreenPart.ICON_ACTON_BAR_TOP_CORNER]
    # bottom = IMAGE_MAP[ScreenPart.LAYOUT_RIGHT_BOTTOM_ICON]
    # area = area_between_pictures(screen, top, bottom)
    #
    # # Main objects
    # checker = LabelChecker(screen, IMAGE_MAP[ScreenPart.ICON_BACKPACK_TAB], area)
    # interactor = WorldInteractor()
    #
    # # Thread that updates screenshots
    # interactor_updater = WorldInteractorUpdater(interactor)
    # screenshoter_thread = threading.Thread(target=interactor_updater.keep_updating, args=())
    # logging.info("Main    : before running screenshoter_thread")
    # screenshoter_thread.start()
    #
    # # Thread that moves mouse
    # checker_thread = threading.Thread(target=interactor.move_mouse_in_area_until_checker, args=(checker,))
    # logging.info("Main    : before running checker_thread")
    # checker_thread.start()
    #
    # logging.info("Main    : wait for the thread to finish")
    # # x.join()
    # logging.info("Main    : all done")


if __name__ == '__main__':
  unittest.main()
