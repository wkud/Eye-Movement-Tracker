import cv2 as cv
from src.cameraHandler import CameraHandler
from src.screenHandler import ScreenHandler
from src.faceDetector import FaceDetector
from src.eyesDetector import EyesDetector
from src.pupilDetector import PupilDetector

camera = CameraHandler()
faceDetector = FaceDetector()
eyesDetector = EyesDetector()
screen = ScreenHandler()
pupilDetector = PupilDetector()

while True:
    image = camera.getFrame()
    grayFrame = camera.frameToGray(image)
    faces = faceDetector.getFace(grayFrame)
    if faces != None:
        for face in faces:
            screen.markFace(image, face)
            eyes = eyesDetector.getEyes(face)

            for eye in eyes:
                screen.markEye(image, eye)
                eyeRegion, x, y = pupilDetector.findEyeCenter(grayFrame, eye)
                screen.markPupil(image, (x, y))

    screen.displayFrame('frame', image)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()
screen.closeWindows()
'''

image = cv.imread('resources/face1.jpeg')
grayFrame = camera.frameToGray(image)
faces = faceDetector.getFace(grayFrame)
screen.markFace(image, faces[0])
eyes = eyesDetector.getEyes(faces[0])

for eye in eyes:
    screen.markEye(image, eye)
    eyeRegion, x, y = pupilDetector.findEyeCenter(grayFrame, eye)
    screen.markPupil(eyeRegion, (x, y))
    cv.imshow('face', eyeRegion)
    cv.waitKey(0)
'''