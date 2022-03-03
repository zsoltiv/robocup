import RPi.GPIO as GPIO


class Motor:
    def __init__(self, plus, minus, enable):
        GPIO.setup(plus, GPIO.OUT)
        GPIO.setup(minus, GPIO.OUT)
        GPIO.setup(enable, GPIO.OUT)

        self.plus = GPIO.PWM(plus, 100)
        self.minus = GPIO.PWM(minus, 100)
        self.dutycycle = 0

    def stop(self):
        self.plus.stop()

    def on(self, dutycycle):
        self.dutycycle = dutycycle
        self.plus.start(0)
        self.minus.start(0)

        GPIO.output(self.enable, GPIO.HIGH)

    def off(self):
        self.dutycycle = 0
        GPIO.output(self.enable, GPIO.LOW)

    def forward(self):
        self.minus.ChangeDutyCycle(0)
        self.plus.ChangeDutyCycle(self.dutycycle)

    def backward(self):
        self.plus.ChangeDutyCycle(0)
        self.minus.ChangeDutyCycle(self.dutycycle)
