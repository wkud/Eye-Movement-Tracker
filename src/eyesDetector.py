import cv2 as cv
from math import floor

class EyesDetector:
    def getEyes(self, face):
        (fx, fy, fw, fh) = face
        left_c = [int(floor(0.35 * fw)), int(floor(0.4 * fh))]
        right_c = [int(floor(0.68 * fw)), int(floor(0.4 * fh))]

        size = int(floor(0.10 * fw))

        left_x, left_y = [left_c[0] - size, left_c[1] - size]
        right_x, right_y = [right_c[0] - size, right_c[1] - size]
        area = size * 2

        left_eye = (fx + left_x, fy + left_y, area, area)
        right_eye = (fx + right_x, fy + right_y, area, area)
        return [left_eye, right_eye]
