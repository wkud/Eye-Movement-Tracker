import cv2 as cv

#constants
K_WEIGHT_DIVISOR = 1.0
K_GRADIENT_THRESHOLD = 50.0
K_WEIGHT_BLUR_SIZE = 5
K_THRESHOLD_VALUE = 0.97
K_ENABLE_WEIGHT = True
K_POST_PROCESSING = True

faceScaleFactor = 1.3
faceMinNeighbors = 5
faceMinSize = 180

def rectToBoundingBox(rect):
    x = rect[0]
    y = rect[1]
    w = rect[2]
    h = rect[3]
    return (x, y, w, h)

def markBoundingBoxOnImage(image, box, color):
    (x, y, w, h) = box
    cv.rectangle(image, (x, y), (x + w, y + h), color, 2)

def markPupilOnImage(image, eyeCoords, color):
    cv.circle(image, eyeCoords, 5, color)

def sliceImage(image, box):
    (x, y, width, height) = box
    return image[y:y+height, x:x+width]

def resizeImage(image, targetWidth, targetHeight, keepAspect = False):
    if keepAspect:
        (height, width) = image.shape[0:1]
        scale = targetWidth * 1.0 / width
        dimensions = (width * scale, height * scale)
    else:
        dimensions = (targetWidth, targetHeight)

    resized = cv.resize(image, dimensions, interpolation=cv.INTER_AREA)
    return resized




