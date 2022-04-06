from adafruit_servokit import ServoKit
from time import sleep

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(550, 2500)
servo_state = 0

def start_position():
    servo_state = 90
    kit.servo[0].angle = servo_state


def rotation():
    if 0 <= servo_state <= 180:
        kit.servo[0].angle = servo_state