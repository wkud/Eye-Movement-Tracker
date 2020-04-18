import cv2 as cv
import dlib
import numpy as np
import argparse
from src.cameraHandler import CameraHandler
from src.utils import markFace

kernel = [
    1, 2, 1,
    2, 4, 2,
    1, 2, 1
]

kernel = np.asarray(kernel)
kernel = kernel/kernel.sum()

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="Path to facial landmark predictor")
args = vars(ap.parse_args())

camera = CameraHandler()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

while True:
    ret, frame = camera.getFrame()
    frameLR = cv.pyrDown(frame)
    gray = camera.frameToGray(frameLR)
    #gray = cv.filter2D(gray, -1, kernel=kernel)
    faces = detector(gray, 1)
    markFace(frameLR, gray, faces, predictor)
    camera.displayFrame('Kamera', frameLR)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()