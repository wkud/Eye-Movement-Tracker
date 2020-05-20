import cv2 as cv
import argparse as arg
from src.cameraHandler import CameraHandler
from src.screenHandler import ScreenHandler
from src.faceDetector import FaceDetector
from src.eyesDetector import EyesDetector
from src.pupilDetector import PupilDetector
from src.utils import nothing
from src.pupilToScreenMapper import PupilToScreenMapper

ap = arg.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
args = vars(ap.parse_args())

camera = CameraHandler()
faceDetector = FaceDetector()
eyesDetector = EyesDetector(args['shape_predictor'])
screen = ScreenHandler()
pupilDetector = PupilDetector()
mapper = PupilToScreenMapper()

cv.namedWindow('frame')
cv.createTrackbar('threshold', 'frame', 0, 255, nothing)
cv.setTrackbarPos('threshold', 'frame', 55)

while True:
    image = camera.getFrame()
    grayFrame = camera.frameToGray(image)
    faceRect, faceCoords = faceDetector.getFace(grayFrame)
    if faceRect is not None:
        screen.markFace(image, faceCoords)
        eyesCoords = eyesDetector.getEyes(grayFrame, faceRect)
        screen.markEye(image, eyesCoords)
        if len(eyesCoords) > 0:
            threshold = cv.getTrackbarPos('threshold', 'frame')
            eyesArray = eyesDetector.splitEyesArray(eyesCoords)
            for eye in eyesArray:
                eyeBox = eyesDetector.calcEyeBoundingBox(eye)
                pupil = pupilDetector.findEyeCenter(grayFrame, eyeBox, threshold)
                if pupil is not None:
                    x, y = pupil
                    screen.markPupil(image, (int(x), int(y)))
                    screenPupilPosition = mapper.convertToScreenPosition(eyeBox, pupil)
                    print(screenPupilPosition)

    screen.displayFrame('frame', image)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()
screen.closeWindows()
