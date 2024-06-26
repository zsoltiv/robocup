import dc
from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO
from time import sleep
# kepfeldolgozas
#from skimage.measure import compare_ssim as ssim
from skimage.metrics import structural_similarity as ssim
from numpy import average as np_average

# custom modulok
from camera import Camera
from image import color_distance_percent, match_percent

red = 11
green = 9
blue = 10
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
GPIO.output(blue, GPIO.LOW)


with ControllerResource() as joystick:
    print("Found a joystick and connected")
    servo_imported = False
    # kamera
    camera = Camera()

    while joystick.connected:
        joystick.check_presses()

        left_y = joystick['ly']
        right_y = joystick['ry']

        if joystick.presses.start and not servo_imported:
            import servo
            servo.start_position()
            servo_imported = True

        if servo_imported:
            #Servo kar alapja:
            #if right_x < -0.75 and servo.alap > 0:
            #    servo.alap = servo.alap - 0.05
            #    servo.alap_rotation()
            #
            #if right_x > 0.75 and servo.alap < 180:
            #    servo.alap = servo.alap + 0.05
            #    servo.alap_rotation()


            #Servo kar rész0:
            if left_y < -0.75 and servo.resz0 > 0:
                servo.resz0 = servo.resz0 - 0.05
                servo.resz0_rotation()

            if left_y > 0.75 and servo.resz0 < 180:
                servo.resz0 = servo.resz0 + 0.05
                servo.resz0_rotation()

            #Servo kar rész1:
            if right_y < -0.75 and servo.resz1 > 0:
                servo.resz1 = servo.resz1 - 0.05
                servo.resz1_rotation()

            if right_y > 0.75 and servo.resz1 < 180:
                servo.resz1 = servo.resz1 + 0.05
                servo.resz1_rotation()


            #Servo kar rész2:
            #if left_x < -0.75 and servo.resz2 > 0:
            #    servo.resz2 = servo.resz2 - 0.05
            #    servo.resz2_rotation()
            #
            #if left_x > 0.75 and servo.resz2 < 180:
            #    servo.resz2 = servo.resz2 + 0.05
            #    servo.resz2_rotation()


            #Servo kar manipulátora
            right_bumper = joystick['r1']
            left_bumper = joystick['l1']

            if right_bumper is not None and servo.manipulator > 0:
                servo.manipulator -= 0.05
                servo.manipulator_rotation()

            if left_bumper is not None and servo.manipulator < 100:
                servo.manipulator += 0.05
                servo.manipulator_rotation()


            #Servo kar alapja
            right_trigger = joystick['r2']
            left_trigger = joystick['l2']

            if right_trigger is not None and servo.alap > 0:
                servo.alap -= 0.05
                servo.alap_rotation()

            if left_trigger is not None and servo.alap < 180:
                servo.alap += 0.05
                servo.alap_rotation()


        #Camera
        if joystick.presses.select:
            camera.picture(display_=False)
            print(len(camera.images))
            if len(camera.images) == 2:
                match = ssim(camera.images[0][0], camera.images[1][0]) * 100
                print(f'Ennyire hasonlóak a képek: {match}')
                #if match >= 90:
                #    print('egyeznek')
                #else:
                #    print('nem egyeznek')
                color_match = np_average(color_distance_percent(camera.images[0][1], camera.images[1][1]))
                print(f'ennyire egyeznek a színek: {color_match}')
                #if color_match >= 90:
                #    print('egyeznek')
                #else:
                #    print('nem egyeznek')
                if match >= 90 and color_match >= 90:
                    print(f'egy és ugyanaz')
                    GPIO.output(green, GPIO.HIGH)
                    sleep(2)
                    GPIO.output(green, GPIO.LOW)
                else:
                    print(f'ez nem talált haverda')
                    GPIO.output(red, GPIO.HIGH)
                    sleep(2)
                    GPIO.output(red, GPIO.LOW)


        #DC motor controlling:
        if joystick.presses.square:
            print("Speed is set to 100")
            dc.speed = 100
        if joystick.presses.circle:
            print("Speed is set to 50")
            dc.speed = 50


        if joystick.presses.dup:
            print("Forward")
            dc.forward()
            dc.motor_controlling()
        if joystick.releases.dup:
            print("Stop")
            dc.motors_off()

        if joystick.presses.ddown:
            print("Backward")
            dc.backward()
            dc.motor_controlling()
        if joystick.releases.ddown:
            print("Stop")
            dc.motors_off()


        if joystick.presses.dright:
            print("Right")
            dc.right()
            dc.motor_controlling()
        if joystick.releases.dright:
            print("Stop")
            dc.motors_off()


        if joystick.presses.dleft:
            print("Left")
            dc.left()
            dc.motor_controlling()
        if joystick.releases.dleft:
            print("Stop")
            dc.motors_off()
