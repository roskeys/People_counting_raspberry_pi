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
        # create a threashold to decide whether it is a head
        self.threshhold = threshhold
        # load the model from a local file
        self.model = load_model(model_path)

    def count(self, img):
        # sliding windows, with each picture 150 * 150
        right = 150
        fraction, marks = [],[]
        # sliding along the long side
        while right < img.shape[1]:
            down = 150
            # sliding along the short side 
            while down < img.shape[0]:
                # slide the window
                cut = img[down-150:down, right-150:right]
                # reshape the video to the one that is accepted by the model
                cut = cv2.resize(cut, (64, 64))
                fraction.append(cut)
                # move down 
                down += 50
            # move right
            right += 50
        # predict a group of pictures we have cut
        marks = self.model.predict(np.array(fraction).astype(np.float32)/255.0)
        count = 0
        for mark in marks:
            # get the number of windows which contains pictures that is larger than the threshold
            if mark > self.threshhold:
                count += 1
        # return the number of people
        return count
