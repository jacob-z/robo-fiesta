from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3, 440)
pwm.start(50)

sleep(3)

    
GPIO.cleanup()
