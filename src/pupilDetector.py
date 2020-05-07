from __future__ import division
from queue import *
import cv2 as cv
import numpy as np
from math import sqrt
from src.utils import K_WEIGHT_DIVISOR, K_GRADIENT_THRESHOLD, K_WEIGHT_BLUR_SIZE, K_THRESHOLD_VALUE, K_ENABLE_WEIGHT, K_POST_PROCESSING

class PupilDetector:
    def findEyeCenterr(self, image, eye):
        eyeRegion = image[eye[1] + 2: eye[1] + eye[3] + -2, eye[0] + 2: eye[0] + eye[2] - 2]
        eyeWEB = self.cutEyebrows(eyeRegion)
        pupilRegion = self.processBlob(eyeWEB)
        return eyeWEB, self.__detector.detect(pupilRegion)

    def testCenters(self, x, y, weight, gx, gy, arr):
        rows, cols = np.shape(arr)
        for cy in range(rows):
            for cx in range(cols):
                if x == cx and y == cy:
                    continue
                dx = x - cx
                dy = y - cy

                magnitude = sqrt((dx * dx) + (dy * dy))
                dx = dx / magnitude
                dy = dy / magnitude
                dot_product = dx * gx + dy * gy
                dot_product = max(0.0, dot_product)
                if K_ENABLE_WEIGHT == True:
                    arr[cy][cx] += dot_product * dot_product * (weight[cy][cx] / K_WEIGHT_DIVISOR)
                else:
                    arr[cy][cx] += dot_product * dot_product
        return arr

    def computeThreshold(self, mags_mat, std_dev_factor):
        mean_magn_grad, std_magn_grad = cv.meanStdDev(mags_mat)
        rows, cols = np.shape(mags_mat)
        stddev = std_magn_grad[0] / sqrt(rows * cols)
        return std_dev_factor * stddev + mean_magn_grad[0]

    def matrixMagnitude(self, gradX, gradY):
        rows, cols = np.shape(gradX)
        magArr = np.zeros((rows, cols))
        for y in range(rows):
            for x in range(cols):
                magnitude = sqrt((gradX[y][x] * gradX[y][x]) + (gradY[y][x] * gradY[y][x]))
                magArr[y][x] = magnitude
        return magArr

    def matrixXGradient(self, mat):
        rows, cols = mat.shape
        out = np.zeros((rows, cols), dtype='float64')
        mat = mat.astype(float)
        for y in range(rows):
            out[y][0] = mat[y][1] - mat[y][0]
            for x in range(1, cols - 1):
                out[y][x] = (mat[y][x + 1] - mat[y][x - 1]) / 2.0
            out[y][cols - 1] = (mat[y][cols - 1] - mat[y][cols - 2])
        return out

    def flood_should_push_point(self, dir, mat):
        px, py = dir
        rows, cols = np.shape(mat)
        if px >= 0 and px < cols and py >= 0 and py < rows:
            return True
        else:
            return False

    def flood_kill_edges(self, mat):
        rows, cols = np.shape(mat)
        cv.rectangle(mat, (0, 0), (cols, rows), 255)
        mask = np.ones((rows, cols), dtype=np.uint8)
        mask = mask * 255
        to_do = Queue()
        to_do.put((0, 0))
        while to_do.qsize() > 0:
            px, py = to_do.get()
            if mat[py][px] == 0:
                continue
            right = (px + 1, py)
            if self.flood_should_push_point(right, mat):
                to_do.put(right)
            left = (px - 1, py)
            if self.flood_should_push_point(left, mat):
                to_do.put(left)
            down = (px, py + 1)
            if self.flood_should_push_point(down, mat):
                to_do.put(down)
            top = (px, py - 1)
            if self.flood_should_push_point(top, mat):
                to_do.put(top)
            mat[py][px] = 0.0
            mask[py][px] = 0
        return mask

    def findEyeCenter(self, image, eye):
        (ex, ey, ew, eh) = eye
        eyeRegion = image[ey + 2: ey + eh + -2, ex + 2: ex + ew - 2]
        eyeRegion = cv.pyrDown(eyeRegion)
        rows, cols = np.shape(eyeRegion)
        #cv.imshow('eyeRegion', eyeRegion)
        #cv.waitKey(0)
        gradX = self.matrixXGradient(eyeRegion)
        #cv.imshow('eyeRegion', gradX)
        #cv.waitKey(0)
        gradY = np.transpose(self.matrixXGradient(np.transpose(eyeRegion)))
        #cv.imshow('eyeRegion', gradY)
        #cv.waitKey(0)
        matrixMag = self.matrixMagnitude(gradX, gradY)
        #cv.imshow('eyeRegion', matrixMag)
        #cv.waitKey(0)
        threshold = self.computeThreshold(matrixMag, K_GRADIENT_THRESHOLD)

        for y in range(rows):
            for x in range(cols):
                if matrixMag[y][x] > threshold:
                    gradX[y][x] = gradX[y][x] / matrixMag[y][x]
                    gradY[y][x] = gradX[y][x] / matrixMag[y][x]
                else:
                    gradX[y][x] = 0.0
                    gradY[y][x] = 0.0

        weight = cv.GaussianBlur(eyeRegion, (K_WEIGHT_BLUR_SIZE, K_WEIGHT_BLUR_SIZE), 0, 0)
        weight_arr = np.asarray(weight)
        weight_rows, weight_cols = np.shape(weight_arr)

        for y in range(rows):
            for x in range(weight_cols):
                weight_arr[y][x] = 255 - weight_arr[y][x]
        out_sum = np.zeros((rows, cols))

        for y in range(weight_rows):
            for x in range(weight_cols):
                gX = gradX[y][x]
                gY = gradY[y][x]
                if gX == 0.0 and gY == 0.0:
                    continue
                self.testCenters(x, y, weight_arr, gX, gY, out_sum)

        num_gradients = weight_rows * weight_cols
        out = out_sum.astype(np.float32) * (1 / num_gradients)
        _, max_val, _, max_p = cv.minMaxLoc(out)
        if K_POST_PROCESSING == True:
            flood_thresh = max_val * K_THRESHOLD_VALUE
            retval, flood_clone = cv.threshold(out, flood_thresh, 0.0, cv.THRESH_TOZERO)
            mask = self.flood_kill_edges(flood_clone)
            _, max_val, _, max_p = cv.minMaxLoc(out, mask)
        x, y = max_p
        x = x * 2 + ex
        y = y * 2 + ey
        return eyeRegion, x ,y

