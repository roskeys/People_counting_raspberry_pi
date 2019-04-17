from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential, load_model
from keras.optimizers import Adam
import os
import cv2
import pickle
import numpy as np
np.random.seed(1337)
os.environ["KERAS_BACKEND"] = "tensorflow"


class HeadCounter():
    def __init__(self, threshhold, model_path):
        self.threshhold = threshhold
        self.model = load_model(model_path)

    def count(self, img):
        right = 150
        fraction, marks = [],[]
        while right < img.shape[1]:
            down = 150
            while down < img.shape[0]:
                cut = img[down-150:down, right-150:right]
                cut = cv2.resize(cut, (64, 64))
                fraction.append(cut)
                down += 50
            right += 50
        marks = self.model.predict(np.array(fraction).astype(np.float32)/255.0)
        count = 0
        for mark in marks:
            if mark > self.threshhold:
                count += 1
        return count
