import cv2
import matplotlib.pyplot as plt
import numpy as np
from viewer import *


def zad1():
    img = cv2.imread("/tmp/img.webp")
    # cv2.imshow("frame", img)
    # cv2.waitKey(0)

    plt.imshow(img)
    plt.show()

def zad2():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break

def zad3():
    slider_count = 511
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    cv2.namedWindow("frame")
    cv2.createTrackbar("slider", "frame", slider_count//2, slider_count, lambda value: None)

    while True:
        ret, frame = cap.read()
        brightness = cv2.getTrackbarPos("slider", "frame")
        brightness -= slider_count//2
        frame = np.clip(frame.astype(np.int16) + brightness, 0, 255).astype(np.uint8)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    viewer = Viewer(1, 0)
    viewer.run()