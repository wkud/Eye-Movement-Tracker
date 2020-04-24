import cv2 as cv
from src.cameraHandler import CameraHandler
from src.screenHandler import ScreenHandler
from src.faceDetector import FaceDetector
from src.eyesDetector import EyesDetector

camera = CameraHandler()
faceDetector = FaceDetector()
eyesDetector = EyesDetector()
screen = ScreenHandler()

while True:
    lowResFrame = camera.getLowResolutionFrame()

    grayFrame = camera.frameToGray(lowResFrame)
    face = faceDetector.getFace(grayFrame)

    if face != None:
        screen.markFace(lowResFrame, face)

        eyes = eyesDetector.getEyes(grayFrame)
        for eye in eyes:
            screen.markEye(lowResFrame, eye)

    screen.displayFrame('Kamera', lowResFrame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()
screen.closeWindows()