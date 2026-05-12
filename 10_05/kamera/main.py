import cv2
import matplotlib.pyplot as plt

def zad1():
    img = cv2.imread("/tmp/img.webp")
    plt.imshow(img)
    plt.show()
    #cv2.imshow("", img)
    #cv2.waitKey()

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


if __name__ == '__main__':
    zad2()