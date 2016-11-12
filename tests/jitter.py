from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
pwm1 = GPIO.PWM(18, 100)
pwm2 = GPIO.PWM(24, 100)

pwm1.start(2)
pwm2.start(2)

time.sleep(0.1)

pwm1.stop(2)
pwm2.stop(2)

GPIO.cleanup()
