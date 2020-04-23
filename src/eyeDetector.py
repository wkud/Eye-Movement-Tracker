import src.utils as utils

class EyeDetector:
    def __init__(self):
        self.topOffsetProportion = .25
        self.sideOffsetProportion = .13
        self.widthProportion = .30
        self.heightProportion = .35

    def getEyes(self, face):
        leftEye = self.getEyeBoundingBox(face, True)
        rightEye = self.getEyeBoundingBox(face, False)
        return (leftEye, rightEye)

    def getEyeBoundingBox(self, face, isLeft):
        (faceX, faceY, faceWidth, faceHeight) = utils.rectToBoundedBox(face)
        eyeWidth = faceWidth * self.widthProportion
        eyeHeight = faceHeight * self.heightProportion
        eyeY = faceY + faceHeight * self.topOffsetProportion

        if isLeft:
            eyeX = faceX + faceWidth * self.sideOffsetProportion
        else:
            eyeX = faceX + faceWidth * (1-self.sideOffsetProportion)

        return (eyeX, eyeY, eyeWidth, eyeHeight)
