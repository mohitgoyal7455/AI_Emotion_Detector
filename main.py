import cv2
from emotion_detector import detect_emotion
from avatar import draw_avatar
from emotion_logger import log_emotion
import time

cap = cv2.VideoCapture(0)

prev_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    emotion = detect_emotion(frame)

    log_emotion(emotion)

    frame = draw_avatar(frame, emotion)

    cv2.putText(frame,
                f"Emotion: {emotion}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    curr_time = time.time()
    fps = 1/(curr_time-prev_time) if prev_time!=0 else 0
    prev_time = curr_time

    cv2.putText(frame,
                f"FPS: {int(fps)}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,0),
                2)

    cv2.putText(frame,
                "Press Q to quit",
                (20,450),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2)

    cv2.imshow("AI Emotion Assistant", frame)

    key = cv2.waitKey(1)

    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()