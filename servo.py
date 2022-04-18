from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)
for i in range(4):
    kit.servo[i].set_pulse_width_range(550, 2500)

manipulator = 0
resz1 = 0
resz0 = 0
alap = 0
#csuklo = 0
#resz2 = 0

def start_position():
    manipulator = 90
    resz1 = 90
    resz0 = 90
    alap = 90
    #csuklo = 90
    #resz2 = 90

    kit.servo[3].angle = manipulator
    kit.servo[2].angle = resz1
    kit.servo[1].angle = resz0
    kit.servo[0].angle = alap
    #kit.servo[1].angle = csuklo
    #kit.servo[2].angle = resz2


def manipulator_rotation():
    if 0 < manipulator < 180:
        kit.servo[3].angle = manipulator

#def csuklo_rotation():
#    if 0 <= csuklo <= 180:
#        kit.servo[1].angle = csuklo

#def resz2_rotation():
#    if 0 <= resz2 <= 180:
#        kit.servo[2].angle = resz2

def resz1_rotation():
    if 0 < resz1 < 180:
        kit.servo[2].angle = resz1

def resz0_rotation():
    if 0 < resz0 < 180:
        kit.servo[1].angle = resz0

def alap_rotation():
    if 0 < alap < 180:
        kit.servo[0].angle = alap

