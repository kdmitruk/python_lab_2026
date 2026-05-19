import cv2.dnn
import numpy as np


def main():
    net = cv2.dnn.readNet("coco/model.pbtxt", "coco/weights.pb")

    # img = cv2.imread("/tmp/img.jpg")

    file = open("coco/labels.txt", "r")
    labels = file.read().split("\n")



    confidence_threshold = 0.4

    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(img, scalefactor=1 / 127.5, mean=(127.5, 127.5, 127.5), swapRB=True,
                                     size=(320, 320), crop=False)
        net.setInput(blob)
        detection = net.forward()

        for i, roi in enumerate(detection[0, 0, :, : ]):
            confidence = roi[2]
            if confidence > confidence_threshold:
                label = labels[int(roi[1])-1]
                box = roi[3:7] * np.array([w, h, w, h])
                box = box.astype(np.uint16)

                cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
                cv2.putText(img, label, (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("", img)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    main()