import cv2 as cv
import dlib
from src.cameraHandler import CameraHandler
from src.utils import markFace

camera = CameraHandler()
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = camera.getFrame()
    frameLR = cv.pyrDown(frame)
    gray = camera.frameToGray(frameLR)
    faces = detector(gray, 1)
    markFace(frameLR, faces)
    camera.displayFrame('Kamera', frameLR)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
camera.endRecording()