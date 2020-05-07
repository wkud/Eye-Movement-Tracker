import cv2 as cv

class CameraHandler:
    def __init__(self):
        self._cam = cv.VideoCapture(0)

    def doNothing(x):
        pass

    def doNothing(x, y):
        pass

    def getFrame(self):
        ret, frame = self._cam.read()
        return frame

    def getLowResolutionFrame(self):
        ret, frame = self._cam.read()
        return cv.pyrDown(frame)

    def frameToGray(self, frame):
        return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    def endRecording(self):
        self._cam.release()
