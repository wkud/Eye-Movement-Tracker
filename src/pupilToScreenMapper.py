from screeninfo import get_monitors

class PupilToScreenMapper:
    def __init__(self):
        monitor = get_monitors()[0]
        self.screenSize = (monitor.width, monitor.height)

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
