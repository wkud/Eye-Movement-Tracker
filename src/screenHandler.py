import cv2 as cv
import src.utils as utils

class ScreenHandler:
    def __init__(self):
        pass

    def displayFrame(self, title, frame):
        cv.imshow(title, frame)

    def closeWindows(self):
        cv.destroyAllWindows()

    def markFace(self, image, faces):
        if len(faces) > 0:
            (x, y, w, h) = utils.rectToBoundedBox(faces[0])
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)