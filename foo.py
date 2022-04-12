from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(550, 2500)
kit.servo[0].angle = 90
#time.sleep(1)
#kit.servo[0].angle = 180

