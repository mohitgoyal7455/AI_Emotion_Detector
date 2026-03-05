import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():

    data = pd.read_csv("data/emotion_log.csv", header=None)

    emotions = data[1]

    emotions.value_counts().plot(kind="bar")

    plt.title("Emotion Distribution")

    plt.show()