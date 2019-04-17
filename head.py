from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential,load_model
import pickle
import os
import cv2
import numpy as np
np.random.seed(1337)
os.environ["KERAS_BACKEND"] = "tensorflow"


class HeadCounter():
    def __init__(self,threshhold,model_path):
        self.threshhold = threshhold
        self.model = load_model(model_path)

    def count(self,img_path):
        img = cv2.imread(img_path)
        marks = []
        right = 150
        fraction = []
        while right < 1920:
            down = 150
            while down < 1080:
                cut = img[down-150:down,right-150:right]
                cut = cv2.resize(cut,(64,64))
                fraction.append(cut)
                down += 50
            right += 50
        marks = self.model.predict(np.array(fraction).astype(np.float32)/255.0)
        count = 0
        for mark in marks:
            if mark > self.threshhold:
                count += 1
        return count
if __name__ == "__main__":
    counter = HeadCounter(0.999998,"./models/model.h5")
    people = counter.count("./test/0.png")
    print(people)