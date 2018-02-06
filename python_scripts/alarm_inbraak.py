import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, GPIO.LOW)
time.sleep(.5)
GPIO.output(22, GPIO.HIGH)

time.sleep(10)
GPIO.cleanup()