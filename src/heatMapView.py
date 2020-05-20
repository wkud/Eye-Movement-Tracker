import numpy as np
import cv2 as cv
import src.utils as utils


class HeatMapView:
    def __init__(self):
        self.FRAMES_PER_IMAGE_UPDATE = 100 # how many frames need to be skipped to update image
        screenWidth, screenHeight = utils.getMonitorSize()
        self.screenSize = (screenWidth, screenHeight)
        self.sampleCount = 0
        self.frameCounter = 0

        # array that counts how many times user looked at a given point
        self.heatCounter = np.zeros([screenWidth, screenHeight])
        
    def addPoint(self, screenPoint):
        width, height = self.screenSize
        x, y = screenPoint
        x, y = int(x), int(y)
        x, y = min(x,  width-1), min(y, height-1) # make sure, that x, y indices aren't greater than size of array
        self.heatCounter[x, y] += 1
        self.sampleCount += 1

        if self.sampleCount % self.FRAMES_PER_IMAGE_UPDATE == 0: # this is one of 100 frames; do update
            self.updatePreviewImage()

    def updatePreviewImage(self):  # create quick to make image of last few points
        width, height = self.screenSize
        self.image = np.zeros([height, width, 4])  # image in hsva format
        for y in range(height):
            for x in range(width):
                hsva = np.ones([4])
                # hsva[0] *= self.heatCounter[x,y]/255.0 # hue
                # hsva[3] *= self.heatCounter[x,y]/255.0 # alpha
                self.image[y, x, :] = hsva
        cv.imshow('hejka', self.image)
        cv.waitKey(0)

    def getSummaryImage(self):  # create image of every point gathered during runtime
        pass
