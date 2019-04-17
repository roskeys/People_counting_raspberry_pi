from libdw import pyrebase
import argparse
import cv2
from head import HeadCounter

counter = HeadCounter(0.999998, "./models/model.h5")


def upload(people):
    url = "https://dw-1d-group.firebaseio.com/"
    apiKey = "AIzaSyDOtjcPwSgjyzH37QWdsZwH6tL6WgYwOlQ"
    config = {"apiKey": apiKey, "databaseURL": url}
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child("people").set(people)


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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c","--camera",help="index of camera")
    ap.add_argument("-l","--local",help="local pictures")
    args = vars(ap.parse_args())

    if args["camera"] is not None and args["local"] is None:
        print("[INFO] using camera")
        count_people()
    elif args["camera"] is None and args["local"] is not None:
        print("[INFO] using local image")
        test(args["local"])
    else:
        print("[INFO] Error please enter again!")

main()
