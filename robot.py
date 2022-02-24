#!/usr/bin/python3

from RPi import GPIO
from time import sleep
# sajat modulok
from motor import Motor

GPIO.setmode(GPIO.BCM)

motor1 = Motor(24, 27, 5)
motor2 = Motor(6, 22, 17)
motor3 = Motor(23, 16, 12)
motor4 = Motor(13, 18, 25)

motor1.on()
motor1.forward()

motor2.on()
motor2.forward()


motor3.on()
motor3.backward()

motor4.on()
motor4.backward()

sleep(5)

motor1.off()
motor2.off()
motor3.off()
motor4.off()

GPIO.cleanup()
