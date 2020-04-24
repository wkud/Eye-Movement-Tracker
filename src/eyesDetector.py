import cv2 as cv
import  src.utils as utils

class EyesDetector:
    def __init__(self):
        self.cascade = cv.CascadeClassifier('resources/haarcascade_eye.xml')

    def getEyes(self, grayFrame, face):
        (x, y, w, h) = face
        upperHalfHeight = int(h/2)
        grayFace = utils.sliceImage(grayFrame, (x, y, w, upperHalfHeight))

        eyes = self.cascade.detectMultiScale(grayFace)
        return eyes
