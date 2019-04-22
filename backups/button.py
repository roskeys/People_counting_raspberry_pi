from time import sleep
import pyrebase
import RPi.GPIO as GPIO

url = 'https://dw-1d-kivy.firebaseio.com'  # URL to Firebase database
apikey = '"AIzaSyADs22Rdhef_5w28Y4oOvx0Aat1NiKCl5U"'  # unique token used for authentication

config = {"apiKey": apikey, "databaseURL": url, }

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.

# Green = 0 ,Red = 1
firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.child("1").set('0')
db.child("2").set('0')
db.child("3").set('0')
db.child("4").set('0')
db.child("5").set('0')
db.child("6").set('0')
db.child("7").set('0')
db.child("8").set('0')
db.child("9").set('0')
db.child("10").set('0')
db.child("11").set('0')
db.child("12").set('0')

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)

# Use different GPIO for the buttons.
red, yellow, green, black, blue, orange, red2, yellow2, green2, black2, blue2, orange2 = [12, 16, 17, 18, 19, 20, 21,
                                                                                          22, 23, 24, 25, 26]

# Set GPIO numbers in the list: [12, 16, 20, 21] as OUTPUT

# If one end of the switch is wired to ground and the other to a gpio you need a pull-up on the gpio.
# Then the gpio will read high normally and will read low when the switch is closed.
#
# If one end of the switch is wired to 3V3 and the other to a gpio you need a pull-down on the gpio.
# Then the gpio will read low normally and will read high when the switch is closed.

switch1 = 4  # white
switch2 = 17  # red
switch3 = 22  # yellow
switch4 = 5  # green
switch5 = 13  # blue
switch6 = 26  # black
switch7 = 18  # white
switch8 = 23  # red
switch9 = 24  # yellow
switch10 = 25  # green
switch11 = 16  # blue
switch12 = 21  # black

GPIO.setup(switch1, GPIO.IN, GPIO.PUD_DOWN)  # Floor 1
GPIO.setup(switch2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch5, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch6, GPIO.IN, GPIO.PUD_DOWN)  # Floor 6
GPIO.setup(switch7, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch8, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch9, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch10, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch11, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(switch12, GPIO.IN, GPIO.PUD_DOWN)  # Floor 12

while True:

    if GPIO.input(switch1) == True:
        db.child("1").set("1")
        print("1f pressed")
    elif GPIO.input(switch1) == False:
        db.child("1").set("0")

    if GPIO.input(switch2) == True:
        db.child("2").set("1")
        print("2 pressed")
    elif GPIO.input(switch2) == False:
        db.child("2").set("0")

    if GPIO.input(switch3) == True:
        db.child("3").set("1")
        print("3 pressed")
    elif GPIO.input(switch3) == False:
        db.child("3").set("0")

    if GPIO.input(switch4) == True:
        db.child("4").set("1")
        print("4 pressed")
    elif GPIO.input(switch4) == False:
        db.child("4").set("0")

    if GPIO.input(switch5) == True:
        db.child("5").set("1")
        print("5 pressed")
    elif GPIO.input(switch5) == False:
        db.child("5").set("0")

    if GPIO.input(switch6) == True:
        db.child("6").set("1")
        print("6 pressed")
    elif GPIO.input(switch6) == False:
        db.child("6").set("0")

    if GPIO.input(switch7) == True:
        db.child("7").set("1")
        print("7 pressed")
    elif GPIO.input(switch7) == False:
        db.child("7").set("0")

    if GPIO.input(switch8) == True:
        db.child("8").set("1")
        print("8 pressed")
    elif GPIO.input(switch8) == False:
        db.child("8").set("0")

    if GPIO.input(switch9) == True:
        db.child("9").set("1")
        print("9 pressed")
    elif GPIO.input(switch9) == False:
        db.child("9").set("0")

    if GPIO.input(switch10) == True:
        db.child("10").set("1")
        print("10 pressed")
    elif GPIO.input(switch10) == False:
        db.child("10").set("0")

    if GPIO.input(switch11) == True:
        db.child("11").set("1")
        print("11 pressed")
    elif GPIO.input(switch11) == False:
        db.child("11").set("0")

    if GPIO.input(switch12) == True:
        db.child("12").set("1")
        print("12 pressed")
    elif GPIO.input(switch12) == False:
        db.child("12").set("0")



