import cv2

PROTO_FILE = "/home/student/Pobrane/pose_deploy.prototxt"
WEIGHTS_FILE = "/home/student/Pobrane/pose_iter_102000.caffemodel"

N_POINTS = 22
HAND_PAIRS = [
    (0, 1), (1, 2), (2, 3), (3, 4),       # kciuk
    (0, 5), (5, 6), (6, 7), (7, 8),       # wskazujący
    (0, 9), (9, 10), (10, 11), (11, 12),  # środkowy
    (0, 13), (13, 14), (14, 15), (15, 16),# serdeczny
    (0, 17), (17, 18), (18, 19), (19, 20) # mały
]

THRESHOLD = 0.1
IN_WIDTH, IN_HEIGHT = 368, 368

def load_network():
    return cv2.dnn.readNetFromCaffe(PROTO_FILE, WEIGHTS_FILE)

def process_frame(frame, net):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0/255,
                                 size=(IN_WIDTH, IN_HEIGHT),
                                 mean=(0,0,0),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    output = net.forward()

    H, W = output.shape[2], output.shape[3]
    points = [None] * N_POINTS

    for i in range(N_POINTS):
        prob_map = output[0, i, :, :]
        _, conf, _, loc = cv2.minMaxLoc(prob_map)
        x = int((w * loc[0]) / W)
        y = int((h * loc[1]) / H)
        if conf > THRESHOLD:
            points[i] = (x, y)

    for i, p in enumerate(points):
        if p is not None:
            cv2.circle(frame, p, 4, (0, 255, 0), thickness=-1)

    for pair in HAND_PAIRS:
        a, b = pair
        if points[a] and points[b]:
            cv2.line(frame, points[a], points[b], (255, 0, 255), 2)

    return frame

def main():
    net = load_network()

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("pose", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        frame = process_frame(frame, net)
        cv2.imshow("pose", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()