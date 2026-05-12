import cv2
import matplotlib.pyplot as plt
import numpy as np

class Viewer:
    def __init__(self, slider_count, slider_default):
        cv2.namedWindow("frame")
        cv2.createTrackbar("slider", "frame", slider_default, slider_count, lambda value: None)
        self.cap = cv2.VideoCapture(0)
        self.slider_count = slider_count

    def run(self):
        while True:
            ret, frame = self.cap.read()
            modifier = self.get_trackbar_pos()
            frame = self.process_frame(frame, modifier)

            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == ord('q'):
                break

    def get_trackbar_pos(self):
        return cv2.getTrackbarPos("slider", "frame")

    def process_frame(self, frame, modifier):
        return frame

class BrightnessViewer(Viewer):
    def __init__(self):
        super().__init__(511, 255)

    def get_trackbar_pos(self):
        return super().get_trackbar_pos() - self.slider_count//2

    def process_frame(self, frame, modifier):
        return np.clip(frame.astype(np.int16) + modifier, 0, 255).astype(np.uint8)
