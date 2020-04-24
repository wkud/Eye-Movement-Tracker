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

        eyes = eyesDetector.getEyes(grayFrame, face)
        for eye in eyes:
            eye[0] += face[0] # eyes coordinates (x, y) are relative to face origin (x,y)
            eye[1] += face[1]
            screen.markEye(lowResFrame, eye)

    screen.displayFrame('Kamera', lowResFrame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()
screen.closeWindows()