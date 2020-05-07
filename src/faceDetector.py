import dlib
from src.utils import rectToBoundingBox, faceMinSize as fMin, faceMinNeighbors as fNeigh, faceScaleFactor as fScale
import cv2 as cv

class FaceDetector:
    def __init__(self):
       self.__detector = cv.CascadeClassifier('resources/haarcascade_frontalface_alt.xml')

    def getFace(self, grayFrame):
        faces = self.__detector.detectMultiScale(grayFrame, fScale, fNeigh, minSize=(fMin, fMin))
        if len(faces) != 0:
            faces = [faces[0]]
            for face in faces:
                rectToBoundingBox(face)
            return faces
        return None
