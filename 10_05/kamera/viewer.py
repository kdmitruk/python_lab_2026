import cv2
import numpy as np


class Viewer:
    COUNT = 512
    def  __init__(self):
        cv2.namedWindow("frame")
        cv2.createTrackbar("value", "frame", Viewer.COUNT//2, Viewer.COUNT, lambda value: None)
        self.cap = cv2.VideoCapture(0)
    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            modifier = self.getTrackbarPos()
            frame = self.processFrame(frame, modifier)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break

    def getTrackbarPos(self):
        return cv2.getTrackbarPos("value", "frame")

    def processFrame(self, frame, modifier):
        return frame
class BrightnessViewer(Viewer):
    def getTrackbarPos(self):
        return super().getTrackbarPos() - 256
    def processFrame(self, frame, modifier):
        return np.clip(frame.astype(np.int16)+modifier, 0, 255).astype(np.uint8)

class BlurViewer(Viewer):
    def getTrackbarPos(self):
        return super().getTrackbarPos()*2+1
    def processFrame(self, frame, modifier):
        return cv2.GaussianBlur(frame, (modifier,modifier), 0)