import cv2
import matplotlib.pyplot as plt

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

    ret, frame = cap.read()
    cv2.imwrite("/tmp/frame.png", frame)


if __name__ == '__main__':
    zad2()