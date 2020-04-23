import src.utils as utils

class EyeDetector:
    def __init__(self):
        self.__topOffsetProportion = .25
        self.__sideOffsetProportion = .13
        self.__widthProportion = .30
        self.__heightProportion = .25

    def getEyes(self, face):
        leftEye = self.__getEyeBoundingBox(face, True)
        rightEye = self.__getEyeBoundingBox(face, False)
        return (leftEye, rightEye)

    def __getEyeBoundingBox(self, face, isLeft):
        (faceX, faceY, faceWidth, faceHeight) = face
        eyeWidth = faceWidth * self.__widthProportion
        eyeHeight = faceHeight * self.__heightProportion
        eyeY = faceY + faceHeight * self.__topOffsetProportion

        if isLeft:
            eyeX = faceX + faceWidth * self.__sideOffsetProportion
        else:
            eyeX = faceX + faceWidth * (1 - self.__sideOffsetProportion) - eyeWidth

        return (int(eyeX), int(eyeY), int(eyeWidth), int(eyeHeight))
