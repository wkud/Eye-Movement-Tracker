import cv2 as cv
import src.utils as utils

class ScreenHandler:
    def __init__(self):
        self.__faceMarkColor = (0, 255, 0)
        self.__eyeMarkColor = (0, 255, 255)

    def displayFrame(self, title, frame):
        cv.imshow(title, frame)

    def closeWindows(self):
        cv.destroyAllWindows()

    def markFace(self, image, face):
        if face != None:
            utils.markBoundingBoxOnImage(image, face, self.__faceMarkColor)

    def markEye(self, image, eye):
        if eye != None:
            utils.markBoundingBoxOnImage(image, eye, self.__eyeMarkColor)