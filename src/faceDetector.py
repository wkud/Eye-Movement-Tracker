import dlib

class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def getFaces(self, grayFrame):
        return self.detector(grayFrame, 1)
