import cv2
import matplotlib.pyplot as plt
import numpy as np
from viewer import *

def zad1():
    img = cv2.imread("/tmp/img.webp")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = hsv[:, :, 0] + 50 % 180
    hsv[:, :, 0] = h
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    #plt.imshow(img)
    #plt.show()
    cv2.imshow("", img)
    cv2.waitKey()

def zad2():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

def zad3():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    cv2.namedWindow("frame")
    brightness = 0
    cv2.createTrackbar("brightness", "frame", 256, 512, lambda value: None)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        brightness = cv2.getTrackbarPos("brightness", "frame")
        brightness -= 256
        frame = np.clip(frame.astype(np.int16)+brightness, 0, 255).astype(np.uint8)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    zad1()
    #viewer = HSVViewer()
    #viewer.run()
