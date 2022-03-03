import RPi.GPIO as GPIO
from time import sleep

from motor import Motor


def left(m1, m2, m3, m4):
    m1.backward()
    m2.backward()
    m3.forward()
    m4.forward()


GPIO.setmode(GPIO.BCM)

try:
    motor1 = Motor(27, 24, 5)
    motor2 = Motor(6, 22, 17)
    motor3 = Motor(23, 16, 12)
    motor4 = Motor(13, 18, 25)
    
    motor1.on(50)
    motor1.forward()
    
    motor2.on(50)
    motor2.forward()
    
    motor3.on(50)
    motor3.forward()
    
    motor4.on(50)
    motor4.forward()
    
    sleep(10)
    
    motor1.off()
    motor2.off()
    motor3.off()
    motor4.off()
except KeyboardInterrupt:
    print('gaz van haverda')
    GPIO.cleanup()
    # ne hivja le a cleanup()-ot ketszer
    exit(1)

GPIO.cleanup()
