import dlib

class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def getFace(self, grayFrame):
        faces = self.detector(grayFrame, 1)
        return faces[0]
