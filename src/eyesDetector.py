import cv2 as cv
import  src.utils as utils

class EyesDetector:
    def __init__(self):
        self.cascade = cv.CascadeClassifier('resources/haarcascade_eye.xml')

    def getEyes(self, grayFrame, face):
        (fx, fy, fw, fh) = face
        upperHalfHeight = int(fh/2)
        grayFace = utils.sliceImage(grayFrame, (fx, fy, fw, upperHalfHeight))

        eyes = self.cascade.detectMultiScale(grayFace)
        for eye in eyes: # eyes coordinates (x, y) are (while shouldn't be) relative to face origin (x,y)
            eye[0] += fx
            eye[1] += fy
        return eyes
