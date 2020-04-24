import cv2 as cv
from src.cameraHandler import CameraHandler
from src.screenHandler import ScreenHandler
from src.faceDetector import FaceDetector

camera = CameraHandler()
faceDetector = FaceDetector()
screen = ScreenHandler()

while True:
    lowResFrame = camera.getLowResolutionFrame()

    grayFrame = camera.frameToGray(lowResFrame)
    face = faceDetector.getFace(grayFrame)
    if face != None:
        screen.markFace(lowResFrame, face)
    screen.displayFrame('Kamera', lowResFrame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()
screen.closeWindows()