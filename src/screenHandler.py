import cv2 as cv
from src.utils import markFaceOnImage, markEyesOnImage, markPupilOnImage

class ScreenHandler:
    def __init__(self):
        self.__faceMarkColor = (0, 255, 0)
        self.__eyeMarkColor = (0, 255, 255)
        self.__pupilMarkColor = (0, 0, 255)

    def displayFrame(self, title, frame):
        cv.imshow(title, frame)

    def closeWindows(self):
        cv.destroyAllWindows()

    def markFace(self, image, face):
        markFaceOnImage(image, face, self.__faceMarkColor)

    def markEye(self, image, eyesCoords):
        markEyesOnImage(image, eyesCoords, self.__eyeMarkColor)

    def markPupil(self, image, eyeCoords):
        markPupilOnImage(image, eyeCoords, self.__pupilMarkColor)