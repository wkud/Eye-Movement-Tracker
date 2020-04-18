import cv2 as cv
import numpy as np

eyeTopP = 15
eyeSideP = 13
eyeHeightP = 30
eyeWidthP = 35

def rectToBB(face):
    x = face.left()
    y = face.top()
    w = face.right() - x
    h = face.bottom() - y
    return (x, y, w, h)

def shapeToNp(shape, dtype="int"):
	coords = np.zeros((shape.num_parts, 2), dtype=dtype)
	for i in range(0, shape.num_parts):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords

def markFace(frame, gray, faces, predictor):
    facesCoords = []
    for (i, face) in enumerate(faces):

        shape = predictor(gray, face)
        for i in range(shape.num_parts):
            if i >= 36 and i <= 47:
                x = shape.part(i).x
                y = shape.part(i).y
                cv.circle(frame, (x, y), 1, (0, 0, 255), -1)

        (x, y, w, h) = rectToBB(face)
        facesCoords.append((x, y, w, h))
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)