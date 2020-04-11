import cv2 as cv

class CameraHandler:
    def __init__(self):
        self._cam = cv.VideoCapture(0)

    def getFrame(self):
        return self._cam.read()

    def frameToGray(self, frame):
        return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    def displayFrame(self, title, frame):
        cv.imshow(title, frame)

    def endRecording(self):
        self._cam.release()
        cv.destroyAllWindows()