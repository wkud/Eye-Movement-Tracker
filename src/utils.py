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




