import csv
from datetime import datetime

def log_emotion(emotion):

    with open("data/emotion_log.csv","a",newline="") as file:

        writer = csv.writer(file)

        writer.writerow([datetime.now(), emotion])