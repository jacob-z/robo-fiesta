from Tkinter import *
import RPi.GPIO as GPIO
import time
import math

def activate_channel(pin):
	GPIO.setup(pin, GPIO.OUT)
	return GPIO.PWM(pin, 100)

def update(angle):
	duty = float(angle) / 10.0 + 2.5
	pwm.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm1 = GPIO.PWM(18, 100)
pwm1.start(5)

GPIO.setup(24, GPIO.OUT)
pwm2 = GPIO.PWM(24, 100)
pwm2.start(5)

for dc in range(0, 101, 5):
	pwm1.ChangeDutyCycle(dc)
	pwm2.ChangeDutyCycle(dc)
	time.sleep(0.1)
	
for dc in range(100, -1, -5):
	pwm1.ChangeDutyCycle(dc)
	pwm2.ChangeDutyCycle(dc)
	time.sleep(0.1)

pwm1.stop(5)
pwm2.stop(5)
GPIO.cleanup()
