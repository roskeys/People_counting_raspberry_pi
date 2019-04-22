#! coding utf-8
import pyrebase
import argparse
import cv2
import time
import numpy as np
from head import HeadCounter

counter = HeadCounter(0.999998, "./models/model.h5")
url = "https://dw-1d-group.firebaseio.com/"
apiKey = "AIzaSyDOtjcPwSgjyzH37QWdsZwH6tL6WgYwOlQ"
authDomain = "https://dw-1d-group.firebaseapp.com"
storageBucket = "gs://dw-1d-group.appspot.com/"

config = {"apiKey": apiKey, "databaseURL": url,"authDomain":authDomain,"storageBucket":storageBucket}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def upload(people):
    db.child("people").set(people)

def upload_picture(picture,t):
    db.child("picture").set(picture)
    db.child("time").set(t)

def test(path="./test/0.png"):
    img = cv2.imread(path)
    people = counter.count(img)
    upload(people)
    print(people)


def count_people():
    cap = cv2.VideoCapture(0)
    while True:
        if cap.isOpened():
            ret,frame = cap.read()
            people = counter.count(frame)
            upload(people)
            print(people)
        else:
            cap.open(0)
def send():
    cap = cv2.VideoCapture(0)
    while True:
        if cap.isOpened():
            ret,frame = cap.read()
            t= time.asctime(time.localtime(time.time()))
            upload_picture(np.array(frame),t)
            print("[INFO] Uploaded picture to firebase,{0}".format(t))
            time.sleep(10)
        else:
            cap.open(0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c","--camera",help="index of camera")
    ap.add_argument("-l","--local",help="local pictures")
    ap.add_argument("-r","--remote",help="push to the desktop to do computation")
    args = vars(ap.parse_args())

    if args["camera"] is not None and args["local"] is None and args["remote"] is None:
        print("[INFO] using camera")
        count_people()
    elif args["camera"] is None and args["local"] is not None and args["remote"] is None:
        print("[INFO] using local image")
        test(args["local"])
    elif args["camera"] is None and args["local"] is None and args["remote"] is not None:
        print("[INFO] Using desktop to do computation!")
        send()
    else:
        print("[INFO] Error please enter again!")

main()
