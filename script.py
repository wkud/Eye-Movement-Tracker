import cv2 as cv
from src.cameraHandler import CameraHandler
from src.screenHandler import ScreenHandler
from src.faceDetector import FaceDetector
from src.eyeDetector import EyeDetector

camera = CameraHandler()
faceDetector = FaceDetector()
eyeDetector = EyeDetector()
screen = ScreenHandler()

while True:
    lowResFrame = camera.getLowResolutionFrame()

    grayFrame = camera.frameToGray(lowResFrame)
    face = faceDetector.getFace(grayFrame)
    if face != None:
        (leftEye, rightEye) = eyeDetector.getEyes(face)

        screen.markFace(lowResFrame, face)
        screen.markEye(lowResFrame, leftEye)
        screen.markEye(lowResFrame, rightEye)
    screen.displayFrame('Kamera', lowResFrame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()
screen.closeWindows()