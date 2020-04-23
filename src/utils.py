import cv2 as cv

def rectToBoundingBox(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def markBoundingBoxOnImage(image, box, color):
    (x, y, w, h) = box
    cv.rectangle(image, (x, y), (x + w, y + h), color, 2)
