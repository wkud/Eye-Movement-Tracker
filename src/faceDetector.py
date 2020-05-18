import dlib
from src.utils import rectToBoundingBox

class FaceDetector:
    def __init__(self):
       self.__detector = dlib.get_frontal_face_detector()

    def getFace(self, grayFrame):
        faces = self.__detector(grayFrame, 0)
        if faces:
            return faces[0], rectToBoundingBox(faces[0])
        return None, None
