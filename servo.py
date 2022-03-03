import RPi.GPIO as GPIO
from time import sleep
from adafruit_servokit import ServoKit

GPIO.setmode(GPIO.BCM)

class Arm:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        # TODO: alaphelyzetbe allitani

    def direction(self, angle):
        self.kit.servo[0].angle = angle
        self.kit.servo[1].angle = angle
        self.kit.servo[2].angle = angle
        self.kit.servo[3].angle = angle





kez = Arm()
csuklo = Arm()
izu2 = Arm()
izu3 = Arm()
izu4 = Arm()
forgo = Arm()
also = Arm()

while True:
    for i in range(1, 181):
        kez.direction(i)
        csuklo.direction(i)
        izu2.direction(i)
        izu3.direction(i)

GPIO.cleanup()
