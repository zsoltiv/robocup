import dc
import servo
from approxeng.input.selectbinder import ControllerResource
# kepfeldolgozas
from skimage.measure import compare_ssim as ssim

# custom modulok
from camera import Camera
from image import color_similarity

with ControllerResource() as joystick:
    print("Found a joystick and connected")
    servo.start_position()
    # kamera
    camera = Camera()


    while joystick.connected:
        joystick.check_presses()
        
        left_x, left_y = joystick['lx', 'ly']
        right_x, right_y = joystick['rx', 'ry']


        if left_x < -0.5 and servo.servo_state > 0:
            servo.servo_state = servo.servo_state - 1
            print(servo.servo_state)
            servo.rotation()
            
        if left_x > 0.5 and servo.servo_state < 180:
            servo.servo_state = servo.servo_state + 1
            print(servo.servo_state)
            servo.rotation()
        
        """
        right_bumper = joystick['r1']
        left_bumper = joystick['l1']

        if left_bumper is not None and servo.servo_state > 0:
            servo.servo_state = servo.servo_state - 1
            print(servo.servo_state)
            servo.rotation()

        if right_bumper is not None and servo.servo_state < 180:
            servo.servo_state = servo.servo_state + 1
            print(servo.servo_state)
            servo.rotation()
        """

        #DC motor controlling:
        if joystick.presses.circle:
            print("Speed is set to 100")
            dc.speed = 100
        if joystick.presses.cross:
            print("Speed is set to 75")
            dc.speed = 75
        if joystick.presses.square:
            print("Speed is set to 50")
            dc.speed = 50
        if joystick.presses.triangle:
            print("Speed is set to 25")
            dc.speed = 25


        if joystick.presses.dup:
            print("Forward")
            dc.forward()
            dc.motor_controlling()
        if joystick.releases.dup:
            print("Stop")
            dc.motors_off()

        if joystick.presses.select:
            camera.picture()
            print(len(camera.images))
            if len(camera.images) == 2:
                print(f'ennyire hasonloak a kepek: {ssim(camera.images[0], camera.images[1])}')


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
