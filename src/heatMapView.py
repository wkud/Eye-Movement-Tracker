import numpy as np
import cv2 as cv
import src.utils as utils


class HeatMapView:
    def __init__(self):
        self.FRAMES_PER_IMAGE_UPDATE = 1  # how many frames need to be skipped to update image
        self.SCALE_FACTOR = 3  # = screen size / array or image size; how many times is screen bigger than an image (heat map)
        self.MARK_RADIUS = 50  # size of circle around screenPupilPoint, which will be mark as seen
        self.START_HUE = 270  # blue
        screenWidth, screenHeight = utils.getMonitorSize()
        self.size = (
            int(screenWidth / self.SCALE_FACTOR),
            int(screenHeight / self.SCALE_FACTOR))  # size of image and counter array
        self.sampleCount = 0
        self.frameCounter = 0

        # array that counts how many times user looked at a given point
        self.heatCounter = np.zeros(self.size)
        self.newPoints = []  # points added since last image update (array of tuples in format (x, y))

        # start color = [0, 0, 1] in hsv -> light desaturated red => white
        self.image = np.zeros((self.size[1], self.size[0], 3),
                              dtype=np.float32)  # dimensions are swapped here (width <-> height) due to openCV image drawing method
        self.image[:, :, 1] = 0  # saturation (start with gray)
        self.image[:, :, 2] = 1  # value

    def addPoint(self, screenPoint):
        width, height = self.size
        x, y = screenPoint
        x, y = int(x / self.SCALE_FACTOR), int(y / self.SCALE_FACTOR)  # scale down to match heat map resolution

        self.sampleCount += 1
        self.newPoints.append((x, y))  # add point, so it will we drawn on image

        def increaseHeat(x, y):
            self.heatCounter[x, y] += 1

        self.__invokeForEachPixelInCircle(x, y, self.MARK_RADIUS, increaseHeat)

        if self.sampleCount % self.FRAMES_PER_IMAGE_UPDATE == 0:  # call update function every self.FRAMES_PER_IMAGE_UPDATE
            self.updateImage()
            self.newPoints = []  # reset list

    def __invokeForEachPixelInCircle(self, centerX, centerY, radius, callback):
        width, height = self.size

        for offsetX in range(-radius, radius):
            for offsetY in range(-radius, radius):
                if offsetX * offsetX + offsetY * offsetY <= radius * radius:  # is x,y in a circle?
                    x, y = centerX + offsetX, centerY + offsetY
                    if 0 <= x < width and 0 <= y < height:  # is x,y in bounds of array?
                        callback(x, y)

    def updateImage(self):  # create quick to make image of last few points
        for (x, y) in self.newPoints:
            self.__invokeForEachPixelInCircle(x, y, self.MARK_RADIUS, self.__updatePixel)

        bgr = cv.cvtColor(self.image, cv.COLOR_HSV2BGR)
        cv.imshow('generate', bgr)

    def __updatePixel(self, x, y):
        heat = self.heatCounter[x, y]
        if 0 < heat <= self.START_HUE:
            # starts with self.START_HUE and decreases to 0 (red)
            self.image[y, x, 0] = max(self.START_HUE - heat, 0)
            self.image[y, x, 1] = 1  # if heat > 0: saturation = 1
        elif self.START_HUE < heat:  # if hue has decreased to 0 (red), start decreasing value (towards black)
            offsetHeat = heat - self.START_HUE  # offset heat counter by threshold needed to get here
            self.image[y, x, 2] = max(1 - offsetHeat / 250, 0)  # red -> black
            self.image[y, x, 1] = 1  # if heat > 0: saturation = 1

    def getSummaryImage(self):  # create image of every point gathered during runtime
        pass
