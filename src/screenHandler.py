import cv2 as cv
import src.utils as utils

class ScreenHandler:
    def __init__(self):
        self.faceMarkColor = (0, 255, 0)

    def displayFrame(self, title, frame):
        cv.imshow(title, frame)

    def closeWindows(self):
        cv.destroyAllWindows()

    def markFace(self, image, face):
        if face != None:
            (x, y, w, h) = utils.rectToBoundedBox(face)
            cv.rectangle(image, (x, y), (x + w, y + h), self.faceMarkColor, 2)