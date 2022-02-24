#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


class Motor:
    def __init__(self, plus, minus, enable):
        self.plus = plus
        self.minus = minus
        self.enable = enable

        GPIO.setup(self.plus, GPIO.OUT)
        GPIO.setup(self.minus, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)

    def stop(self):
        GPIO.output(self.plus, GPIO.LOW)
        GPIO.output(self.minus, GPIO.LOW)

    def on(self):
        GPIO.output(self.enable, GPIO.HIGH)

    def off(self):
        GPIO.output(self.enable, GPIO.LOW)

    def forward(self):
        GPIO.output(self.plus, GPIO.HIGH)
        GPIO.output(self.minus, GPIO.LOW)

    def backward(self):
        GPIO.output(self.plus, GPIO.LOW)
        GPIO.output(self.minus, GPIO.HIGH)


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
