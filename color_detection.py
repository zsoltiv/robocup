import RPi.GPIO as GPIO
from time import time, sleep

# gondolom konstans, ennyi pulset kell bekerni
CYCLES = 10

def read_color(_color):
    #start = time()
    #for _ in range(CYCLES):
    #    print(_)
    #    GPIO.wait_for_edge(_color, GPIO.BOTH)
    #duration = time() - start
    #return CYCLES / duration
    while True:
        print(GPIO.input(_color))
        sleep(.2)
    

def szinkod(_s2, _s3, _color):
    print('clear')
    GPIO.output(_s2, GPIO.HIGH)
    GPIO.output(_s3, GPIO.LOW)
    clear = read_color(_color)
    sleep(.5)
    print('red')
    GPIO.output(_s2, GPIO.LOW)
    GPIO.output(_s3, GPIO.LOW)
    #red = read_color(_color)
    sleep(.5)
    print('blue')
    GPIO.output(_s2, GPIO.LOW)
    GPIO.output(_s3, GPIO.HIGH)
    blue = read_color(_color)
    sleep(.5)
    print('green')
    GPIO.output(_s2, GPIO.HIGH)
    GPIO.output(_s3, GPIO.HIGH)
    green = read_color(_color)
    sleep(.5)
    print(f'R: {red} G: {green} B: {blue}')


# ezek allitjak melyik szint kerjuk le
s2 = 10
s3 = 8

# a TCS3200-n OUT pin
color = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(s2, GPIO.OUT)
GPIO.setup(s3, GPIO.OUT)
GPIO.setup(color, GPIO.IN) #pull_up_down=GPIO.PUD_UP)

try:
    while True:
        sleep(1)
        szinkod(s2, s3, color)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
