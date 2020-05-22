import src.utils as utils


class PupilToScreenMapper:
    def __init__(self):
        self.screenSize = utils.getMonitorSize()
        percent = 0.2
        self.marginPercent = (percent, -0.2, percent, percent)  # (mt, mb, ml, mr) - margin: top, bottom, left, right

    def __limitPupilRegion(self, eyeBox):  # convert eyeBox to smaller pupilBox (by cutting out the margins)
        (ex, ey, ew, eh) = eyeBox
        (marginPercentTop, marginPercentBottom, marginPercentLeft, marginPercentRight) = self.marginPercent
        mt, mb, ml, mr = eh * marginPercentTop, eh * marginPercentBottom, ew * marginPercentLeft, ew * marginPercentRight  # margins in pixels (not percent)

        prx = ex + ml
        pry = ey + mt
        prw = ew - (ml + mr)
        prh = eh - (mt + mb)
        return (prx, pry, prw, prh)  # pupilRegionBox

    def convertToScreenPosition(self, eyeBox, pupilPos):
        (prx, pry, prw, prh) = self.__limitPupilRegion(eyeBox) # pupil region box (same as eye box but without margins)
        (px, py) = pupilPos

        rpx = px - prx  # Relative Pupil X - pupil position relative to eye coords
        rpy = py - pry

        scaleX = rpx * 1.0 / prw  # (relative) pupilX as percent of whole width
        scaleY = rpy * 1.0 / prh

        sw, sh = self.screenSize
        x = scaleX * sw  # proportinally mapped
        y = scaleY * sh

        screenPosX = min(x, sw - 1)  # make sure, that x, y indices aren't greater than screen size
        screenPosY = min(y, sh - 1)

        return (screenPosX, screenPosY)
