#! coding utf-8
from libdw import pyrebase
import argparse
import cv2
import time
import numpy as np
from head import HeadCounter
import threading
import time

# initialize the counter and also initialize the firebase
counter = HeadCounter(0.999998, "./models/model.h5")
url = "https://dw-1d-kivy.firebaseio.com"
apikey = "AIzaSyADs22Rdhef_5w28Y4oOvx0Aat1NiKCl5U"

config = {"apiKey": apikey, "databaseURL": url}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# the upload function will change the values of number of people stored in the real time database
def upload(people):
    db.child("Number of Ppl").set(people)

# the test function get the number of people from a local picture and count the number of people inside and upload it to firebase
def test(path="./test/0.png"):
    img = cv2.imread(path)
    people = counter.count(img)
    upload(people)
    print(people)

# use opencv to take picture of the lift and recognize it using the cuntion count()
def count_people():
    cap = cv2.VideoCapture(0)
    while True:
        # check if the camera is open
        if cap.isOpened():
            ret, frame = cap.read()
            people = counter.count(frame)
            upload(people)
            print(people)
        else:
            cap.open(0)


def main():
    # set two kinds of mode one is recognizing local image, another is taking pictures and count the people inside
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--camera", help="index of camera")
    ap.add_argument("-l", "--local", help="local pictures")
    args = vars(ap.parse_args())

    if args["camera"] is not None and args["local"] is None:
        # using the camera to take picture and count the number of people
        print("[INFO] using camera")
        count_people()
    elif args["camera"] is None and args["local"] is not None:
        # using local image and count the number of people
        print("[INFO] using local image")
        test(args["local"])
    else:
        # error case
        print("[INFO] Error please enter again!")
main()
