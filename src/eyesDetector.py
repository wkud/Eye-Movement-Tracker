import numpy as np
from dlib import shape_predictor
from src.utils import shapeToNp

class EyesDetector:
    def __init__(self, shape):
        self.__predictor = shape_predictor(shape)

    def convertFrom12To8(self, eyesCoords):
        newEyesCoords = np.zeros((8, 2), dtype=int)
        idxCounter = 0
        for i in range(0, 12):
            if i == 1 or i == 4 or i == 7 or i == 10:
                newEyesCoords[idxCounter] = (eyesCoords[i] + eyesCoords[i + 1]) / 2
                idxCounter += 1
            elif i == 2 or i == 5 or i == 8 or i == 11:
                continue
            else:
                newEyesCoords[idxCounter] = eyesCoords[i]
                idxCounter += 1
        return newEyesCoords

    def splitEyesArray(self, eyes):
        return [eyes[0 : 4], eyes[4 : 8]]

    def calcEyeBoundingBox(self, eye):
        xCoords = []
        yCoords = []
        for coord in eye:
            xCoords.append(coord[0])
            yCoords.append(coord[1])
        x = min(xCoords)
        y = min(yCoords)
        w = max(xCoords) - x
        h = max(yCoords) - y
        return (x, y, w, h)

    def getEyes(self, grayFrame, face):
        shape = self.__predictor(grayFrame, face)
        shape = shapeToNp(shape)
        convertedShape = self.convertFrom12To8(shape[36 : 48])
        return convertedShape
