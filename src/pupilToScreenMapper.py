import src.utils as utils

class PupilToScreenMapper:
    def __init__(self):
        self.screenSize = utils.getMonitorSize();

    def convertToScreenPosition(self, eyeBox, pupilPos):
        (ex, ey, ew, eh) = eyeBox
        (px, py) = pupilPos

        rpx = px - ex # Relative Pupil X - pupil position relative to eye coords
        rpy = py - ey

        scaleX = rpx * 1.0 / ew # (relative) pupilX as percent of whole width
        scaleY = rpy * 1.0 / eh

        sw, sh = self.screenSize
        screenPosX = scaleX * sw # proportinally mapped
        screenPosY = scaleY * sh

        return (screenPosX, screenPosY)
