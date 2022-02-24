from RPi import GPIO


class Motor:
    def __init__(self, plus, minus, enable):
        self.plus = plus
        self.minus = minus
        # A motozero-n levo chip hasznal egy harmadik pint,
        # ami engedelyezi egy adott motor vezerleset
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
