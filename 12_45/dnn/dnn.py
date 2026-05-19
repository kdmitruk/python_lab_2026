import cv2.dnn
import numpy as np


def main():
    net = cv2.dnn.readNet("coco/model.pbtxt", "coco/weights.pb")
    file = open("coco/labels.txt", "r")
    labels = file.read().split("\n")

    img = cv2.imread("/tmp/img.jpg")
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(img, mean=(127.5, 127.5 ,127.5), scalefactor=1/127.5, size=(320, 320), swapRB=True, crop=False)

    net.setInput(blob)
    detection = net.forward()

    threshold = 0.4

    for roi in detection[0, 0, :, :]:
        confidence = roi[2]
        if confidence > threshold:
            label = labels[int(roi[1])]
            box = (roi[3:] * np.array([w, h, w, h])).astype(np.uint16)
            cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
            img = cv2.putText(img, label , (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()