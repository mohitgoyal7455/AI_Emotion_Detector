import cv2

avatars = {
    "happy": cv2.imread("animations/happy.png"),
    "sad": cv2.imread("animations/sad.png"),
    "angry": cv2.imread("animations/angry.png"),
    "neutral": cv2.imread("animations/neutral.png")
}

def draw_avatar(frame, emotion):

    if emotion in avatars and avatars[emotion] is not None:

        avatar = cv2.resize(avatars[emotion], (120,120))

        h, w, _ = frame.shape

        frame[10:130, w-130:w-10] = avatar

    return frame