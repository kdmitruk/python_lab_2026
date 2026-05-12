import cv2

def zad1():
    img = cv2.imread("/tmp/img.webp")
    cv2.imshow("", img)
    cv2.waitKey()

if __name__ == '__main__':
    zad1()