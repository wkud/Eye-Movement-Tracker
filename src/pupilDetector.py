import cv2 as cv

class PupilDetector:
    def __init__(self):
        self.__detectorParams = cv.SimpleBlobDetector_Params()
        self.__detectorParams.filterByArea = True
        self.__detectorParams.maxArea = 1500
        self.detector = cv.SimpleBlobDetector_create(self.__detectorParams)

    def findEyeCenter(self, image, eye, threshold):
        (ex, ey, ew, eh) = eye
        eyeRegion = image[ey -10 : ey + eh + 20, ex: ex + ew]
        _, img = cv.threshold(eyeRegion, threshold, 255, cv.THRESH_BINARY)
        img = cv.erode(img, None, iterations=2)
        img = cv.dilate(img, None, iterations=4)
        img = cv.medianBlur(img, 5)
        cv.imshow('img', img)
        keypoints = self.detector.detect(img)
        if len(keypoints) > 0:
            x, y = keypoints[0].pt
            return (x + ex, y + ey - 4)
        return None