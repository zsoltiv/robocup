from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 768)
camera.color_effects = (128, 128)
camera.start_preview()
sleep(3)
rgb = PiRGBArray(camera)
