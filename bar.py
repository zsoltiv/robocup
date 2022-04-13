import RPi.GPIO as GPIO
import time



s2 = 35
s3 = 37
signal = 38
NUM_CYCLES = 10


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")
  




def loop():
  temp = 1
  while(1):

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    print('start')
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.BOTH)
      print('impulse')
    duration = time.time() - start      #seconds to run for loop
    print('finally over')
    red  = NUM_CYCLES / duration   #in Hz
    print("red value - ",red)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.BOTH)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print("blue value - ",blue)

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.BOTH)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("green value - ",green)
    time.sleep(2)  


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()
    print('set up success')

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
