import cv2
from deepface import DeepFace

def detect_emotion(frame):

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        emotion = result[0]['dominant_emotion']

        if emotion == "happy":
            return "happy"

        elif emotion == "sad":
            return "sad-face"

        elif emotion == "angry":
            return "angry"

        else:
            return "neutral"

    except:
        return "neutral"