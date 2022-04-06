import RPi.GPIO as GPIO

def motors_basic_setup():
    GPIO.setup(enable1, GPIO.OUT)
    GPIO.setup(enable2, GPIO.OUT)
    GPIO.setup(enable3, GPIO.OUT)
    GPIO.setup(enable4, GPIO.OUT)

    GPIO.setup(positive1, GPIO.OUT)
    GPIO.setup(negative1, GPIO.OUT)

    GPIO.setup(positive2, GPIO.OUT)
    GPIO.setup(negative2, GPIO.OUT)

    GPIO.setup(positive3, GPIO.OUT)
    GPIO.setup(negative3, GPIO.OUT)

    GPIO.setup(positive4, GPIO.OUT)
    GPIO.setup(negative4, GPIO.OUT)

def motors_off():
    enable1_pwm.ChangeDutyCycle(0)
    enable2_pwm.ChangeDutyCycle(0)
    enable3_pwm.ChangeDutyCycle(0)
    enable4_pwm.ChangeDutyCycle(0)

def forward():
    GPIO.output(positive1, GPIO.HIGH)
    GPIO.output(negative1, GPIO.LOW)

    GPIO.output(positive2, GPIO.HIGH)
    GPIO.output(negative2, GPIO.LOW)

    GPIO.output(positive3, GPIO.HIGH)
    GPIO.output(negative3, GPIO.LOW)

    GPIO.output(positive4, GPIO.HIGH)
    GPIO.output(negative4, GPIO.LOW)

def backward():
    GPIO.output(positive1, GPIO.LOW)
    GPIO.output(negative1, GPIO.HIGH)

    GPIO.output(positive2, GPIO.LOW)
    GPIO.output(negative2, GPIO.HIGH)

    GPIO.output(positive3, GPIO.LOW)
    GPIO.output(negative3, GPIO.HIGH)

    GPIO.output(positive4, GPIO.LOW)
    GPIO.output(negative4, GPIO.HIGH)

def right():
    GPIO.output(positive1, GPIO.HIGH)
    GPIO.output(negative1, GPIO.LOW)

    GPIO.output(positive2, GPIO.LOW)
    GPIO.output(negative2, GPIO.HIGH)

    GPIO.output(positive3, GPIO.LOW)
    GPIO.output(negative3, GPIO.HIGH)

    GPIO.output(positive4, GPIO.HIGH)
    GPIO.output(negative4, GPIO.LOW)

def left():
    GPIO.output(positive1, GPIO.LOW)
    GPIO.output(negative1, GPIO.HIGH)

    GPIO.output(positive2, GPIO.HIGH)
    GPIO.output(negative2, GPIO.LOW)

    GPIO.output(positive3, GPIO.HIGH)
    GPIO.output(negative3, GPIO.LOW)

    GPIO.output(positive4, GPIO.LOW)
    GPIO.output(negative4, GPIO.HIGH)

def motor_controlling():
    enable1_pwm.ChangeDutyCycle(speed)
    enable2_pwm.ChangeDutyCycle(speed)
    enable3_pwm.ChangeDutyCycle(speed)
    enable4_pwm.ChangeDutyCycle(speed)


#Pre-allocated GPIO pins:
#Motor 1 (back left)
enable1 = 5
positive1 = 24
negative1 = 27

#Motor 2 (back right)
enable2 = 17
positive2 = 6
negative2 = 22

#Motor 3 (front right)
enable3 = 12
positive3 = 23
negative3 = 16

#Motor 4 (front left)
enable4 = 25
positive4 = 13
negative4 = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
motors_basic_setup()

enable1_pwm = GPIO.PWM(enable1, 1000)
enable2_pwm = GPIO.PWM(enable2, 2000)
enable3_pwm = GPIO.PWM(enable3, 3000)
enable4_pwm = GPIO.PWM(enable4, 4000)

enable1_pwm.start(0)
enable2_pwm.start(0)
enable3_pwm.start(0)
enable4_pwm.start(0)
speed = 100
