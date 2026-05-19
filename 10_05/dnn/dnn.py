import cv2.dnn
import numpy as np


def main():
    net = cv2.dnn.readNet("coco/model.pbtxt", "coco/weights.pb")

    img = cv2.imread("/tmp/img.jpg")
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(img, scalefactor=1/127.5, mean=(127.5, 127.5, 127.5), swapRB=True, size=(320, 320), crop=False)

    file = open("coco/labels.txt", "r")
    labels = file.read().split("\n")

    net.setInput(blob)
    detection = net.forward()

    confidence_threshold = 0.4

    for i, roi in enumerate(detection[0, 0, :, : ]):
        confidence = roi[2]
        if confidence > confidence_threshold:
            label = labels[int(roi[1])]
            box = roi[3:7] * np.array([w, h, w, h])
            box = box.astype(np.uint16)

            cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
            cv2.putText(img, label, (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()