import cv2 as cv

def rectToBB(face):
    x = face.left()
    y = face.top()
    w = face.right() - x
    h = face.bottom() - y
    return (x, y, w, h)

def markFace(image, faces):
    if len(faces) > 0:
        (x, y, w, h) = rectToBB(faces[0])
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)