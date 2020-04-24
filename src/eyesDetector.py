import cv2 as cv

class EyesDetector:
    def __init__(self):
        self.cascade = cv.CascadeClassifier('resources/haarcascade_eye.xml')

    def getEyes(self, grayFrame):
        eyes = self.cascade.detectMultiScale(grayFrame)
        return eyes
