from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential
import pickle
import os
import numpy as np
np.random.seed(1337)
os.environ["KERAS_BACKEND"] = "tensorflow"

# loading training data and preprocessing
def load_data():
    file1 = open("train.pickle", "rb")
    file2 = open("test.pickle", "rb")
    (x_train, y_train) = pickle.load(file1)
    (x_test, y_test) = pickle.load(file2)
    x_train = x_train.astype(np.float32)/255.0
    x_test = x_test.astype(np.float32)/255.0
    print(x_train.shape)
    print(x_test.shape)
    return (x_train, y_train, x_test, y_test)


def get_optimizer():
    # define the optimizer
    return Adam(lr=0.002)

# define the model
def classifyer(optimizer):
    model = Sequential()
    # conv layers
    model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3),padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3), padding='same', activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3),padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # fully connected layer
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    # add drop out to prevent over fitting
    model.add(Dropout(0.5))
    # output the prediction using sigmoid function
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss="binary_crossentropy",optimizer=optimizer, metrics=["accuracy"])
    return model


def train(epochs=1, batch_size=128):
    x_train, y_train, x_test, y_test = load_data()
    adam = get_optimizer()
    model = classifyer(adam)
    # feed the model with data
    model.fit(x_train, y_train, nb_epoch=epochs, batch_size=batch_size)
    # evaluate the model
    loss, accuracy = model.evaluate(x_test, y_test)
    model.save('./models/model.h5')
    print("loss=", loss)
    print("accuracy=", accuracy)


if __name__ == '__main__':
    # train the model, run 41 epoches
    train(41, 2048)