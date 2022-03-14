import RPi.GPIO as GPIO
from approxeng.input.selectbinder import ControllerResource

def forward():
	GPIO.output(in1, GPIO.HIGH)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.HIGH)
	GPIO.output(in4, GPIO.LOW)

def backward():
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.HIGH)
	GPIO.output(in3, GPIO.LOW)
	GPIO.output(in4, GPIO.HIGH)

def right():
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.HIGH)
	GPIO.output(in3, GPIO.HIGH)
	GPIO.output(in4, GPIO.LOW)

def left():
	GPIO.output(in1, GPIO.HIGH)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.LOW)
	GPIO.output(in4, GPIO.HIGH)

def motor_controlling():
	motor_ena.ChangeDutyCycle(speed)
	motor_enb.ChangeDutyCycle(speed)


def motor_off():
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.LOW)
	GPIO.output(in4, GPIO.LOW)

def motors_basic_setup():
	GPIO.setup(in1, GPIO.OUT)
	GPIO.setup(in2, GPIO.OUT)
	GPIO.setup(ena, GPIO.OUT)

	GPIO.setup(in3, GPIO.OUT)
	GPIO.setup(in4, GPIO.OUT)
	GPIO.setup(enb, GPIO.OUT)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Motor A controlling's GPIO headers
in1 = 16
in2 = 18
ena = 22

#Motor Bs controlling's GPIO headers
in3 = 11
in4 = 13
enb = 15

motors_basic_setup()

motor_ena = GPIO.PWM(ena, 1000)
motor_enb = GPIO.PWM(enb, 2000)
motor_ena.start(0)
motor_enb.start(0)
speed = 50
