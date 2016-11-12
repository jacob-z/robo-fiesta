'''
Authors: Michael Friedman
Created: 11/12/16

Description: Represents a motor on our vehicle. Interacts with the
hardware and provides a simple interface for clients to use.
'''

from Tkinter import *
import RPi.GPIO as GPIO
import time
from motor import Motor

class Motor:
	
	FORWARD = True
	BACKWARD = not FORWARD
	
	'''
	Creates a new instance of a Motor object
	
	Args:
		channel_out: int indicating output channel (pin) on the Pi
		flipped: (optional) boolean indicating whether or not the
			direction is reversed
	'''
	def __init__(self, channel_out, flipped=False):
		self._reversed = flipped
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(channel_out, GPIO.OUT)
		self._pwm = GPIO.PWM(channel_out, 100)
		self._pwm.start(5)
	
	'''
	Spins motor at an optionally specified (relative) speed
	
	Args:
		speed: int from 1 to 5 indicating speed
		direction: boolean indicating forward or backward motion
	'''
	def start(self, speed=1, direction=Motor.FORWARD):
		while True:
			for dc in range(0, 101, 5):
				self._pwm.ChangeDutyCycle(dc)
				time.sleep(0.1)

	
