import dlib
import src.utils as utils

class FaceDetector:
    def __init__(self):
        self.__detector = dlib.get_frontal_face_detector()

    def getFace(self, grayFrame):
        faces = self.__detector(grayFrame, 1)
        if len(faces) == 0:
            return None

        faceAsBox = utils.rectToBoundingBox(faces[0])
        return faceAsBox
