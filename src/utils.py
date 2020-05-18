import cv2 as cv
import numpy as np

def rectToBoundingBox(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def shapeToNp(shape):
	coords = np.zeros((68, 2), dtype=int)
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords

def markFaceOnImage(image, box, color):
    (x, y, w, h) = box
    cv.rectangle(image, (x, y), (x + w, y + h), color, 2)

def markEyesOnImage(image, coords, color):
    for (x, y) in coords:
        cv.circle(image, (x, y), 1, color, -1)

def markPupilOnImage(image, eyeCoords, color):
    cv.circle(image, eyeCoords, 5, color)

def nothing(x):
    pass



