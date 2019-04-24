import pyrebase
import RPi.GPIO as GPIO


class Button():
    def __init__(self, url="https://dw-1d-group.firebaseio.com/", apiKey="AIzaSyDOtjcPwSgjyzH37QWdsZwH6tL6WgYwOlQ",
                 authDomain="https://dw-1d-group.firebaseapp.com", storageBucket="gs://dw-1d-group.appspot.com/"):
        # Create a firebase object by specifying the URL of the database and its secret token.
        # The firebase object has functions put and get, that allows user to put data onto
        # the database and also retrieve data from the database.
        self.config = config = {"apiKey": apiKey, "databaseURL": url, "authDomain": authDomain,
                                "storageBucket": storageBucket}
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        for i in range(1, 13):
            self.db.child("{0}".format(i)).set("0")
        # Use the BCM GPIO numbers as the numbering scheme.
        GPIO.setmode(GPIO.BCM)
        self.switch1 = 4  # white
        self.switch2 = 17  # red
        self.switch3 = 22  # yellow
        self.switch4 = 5  # green
        self.switch5 = 13  # blue
        self.switch6 = 26  # black
        self.switch7 = 18  # white
        self.switch8 = 23  # red
        self.switch9 = 24  # yellow
        self.switch10 = 25  # green
        self.switch11 = 16  # blue
        self.switch12 = 21  # black
        GPIO.setup(self.switch1, GPIO.IN, GPIO.PUD_DOWN)  # Floor 1
        GPIO.setup(self.switch2, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch3, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch4, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch5, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch6, GPIO.IN, GPIO.PUD_DOWN)  # Floor 6
        GPIO.setup(self.switch7, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch8, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch9, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch10, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch11, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.switch12, GPIO.IN, GPIO.PUD_DOWN)  # Floor 12

    def pressed(self):
        if GPIO.input(self.switch1) == True:
            self.db.child("1").set("1")
            print("1f pressed")
        elif GPIO.input(self.switch1) == False:
            self.db.child("1").set("0")

        if GPIO.input(self.switch2) == True:
            self.db.child("2").set("1")
            print("2 pressed")
        elif GPIO.input(self.switch2) == False:
            self.db.child("2").set("0")

        if GPIO.input(self.switch3) == True:
            self.db.child("3").set("1")
            print("3 pressed")
        elif GPIO.input(self.switch3) == False:
            self.db.child("3").set("0")

        if GPIO.input(self.switch4) == True:
            self.db.child("4").set("1")
            print("4 pressed")
        elif GPIO.input(self.switch4) == False:
            self.db.child("4").set("0")

        if GPIO.input(self.switch5) == True:
            self.db.child("5").set("1")
            print("5 pressed")
        elif GPIO.input(self.switch5) == False:
            self.db.child("5").set("0")

        if GPIO.input(self.switch6) == True:
            self.db.child("6").set("1")
            print("6 pressed")
        elif GPIO.input(self.switch6) == False:
            self.db.child("6").set("0")

        if GPIO.input(self.switch7) == True:
            self.db.child("7").set("1")
            print("7 pressed")
        elif GPIO.input(self.switch7) == False:
            self.db.child("7").set("0")

        if GPIO.input(self.switch8) == True:
            self.db.child("8").set("1")
            print("8 pressed")
        elif GPIO.input(self.switch8) == False:
            self.db.child("8").set("0")

        if GPIO.input(self.switch9) == True:
            self.db.child("9").set("1")
            print("9 pressed")
        elif GPIO.input(self.switch9) == False:
            self.db.child("9").set("0")

        if GPIO.input(self.switch10) == True:
            self.db.child("10").set("1")
            print("10 pressed")
        elif GPIO.input(self.switch10) == False:
            self.db.child("10").set("0")

        if GPIO.input(self.switch11) == True:
            self.db.child("11").set("1")
            print("11 pressed")
        elif GPIO.input(self.switch11) == False:
            self.db.child("11").set("0")

        if GPIO.input(self.switch12) == True:
            self.db.child("12").set("1")
            print("12 pressed")
        elif GPIO.input(self.switch12) == False:
            self.db.child("12").set("0")
if __name__ == "__main__":
    button = Button()
    while True:
        button.pressed()