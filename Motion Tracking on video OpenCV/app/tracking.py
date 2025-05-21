
import cv2
import numpy as np

def process_video(input_path, output_path="output.mp4", display_callback=None):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    ret, frame = cap.read()
    if not ret:
        cap.release()
        return False, "Cannot read the video file."

    height, width = frame.shape[:2]
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

    fast = cv2.FastFeatureDetector_create()
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_kp = fast.detect(prev_gray, None)
    prev_kp, prev_des = orb.compute(prev_gray, prev_kp)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp = fast.detect(gray, None)
        kp, des = orb.compute(gray, kp)

        if prev_des is not None and des is not None:
            matches = bf.match(prev_des, des)
            matches = sorted(matches, key=lambda x: x.distance)[:50]

            for m in matches:
                pt1 = tuple(np.round(prev_kp[m.queryIdx].pt).astype(int))
                pt2 = tuple(np.round(kp[m.trainIdx].pt).astype(int))
                frame = cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

        out.write(frame)

        if display_callback:
            display_callback(frame)

        prev_gray = gray
        prev_kp = kp
        prev_des = des

    cap.release()
    out.release()
    return True, output_path
