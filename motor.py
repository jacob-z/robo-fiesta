'''
Authors: Michael Friedman
Created: 11/12/16

Description: Represents a motor on our vehicle. Interacts with the
hardware and provides a simple interface for clients to use.
'''

from Tkinter import *
import RPi.GPIO as GPIO
import time

class Motor:
	
	# Public constants
	FORWARD = True
	BACKWARD = False
	
	# Public constants
	_DC_BACKWARD = 99
	_DC_FORWARD = 6
	
	'''
	Creates a new instance of a Motor object
	
	Args:
		channel_out: int indicating output channel (pin) on the Pi
		flipped: (optional) boolean indicating whether or not the
			direction is reversed
	'''
	def __init__(self, channel_out, flipped=False):
		self._flipped = flipped
		self._is_started = False
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(channel_out, GPIO.OUT)
		self._pwm = GPIO.PWM(channel_out, 100)
		
	
	'''
	Helper method for _rotate()
	
	Executes one forward motion cycle.
	'''
	def _rotate_forward(self, speed):
		# TODO: Use speed somehow
		self._pwm.ChangeDutyCycle(Motor._DC_FORWARD)
			
			
	'''
	Helper method for _rotate()
	
	Executes one forward motion cycle.
	'''
	def _rotate_backward(self, speed):
		# TODO: Use speed somehow
		self._pwm.ChangeDutyCycle(Motor._DC_BACKWARD)
			
	
	'''
	Spins motor at an optionally specified (relative) speed
	
	Args:
		speed: int from 1 to 5 indicating speed
		direction: boolean indicating forward or backward motion
	'''
	def start(self, speed=1, direction=FORWARD):
		if self._is_started:
			raise Exception('Motor already started. Must check with is_started() before calling start()')
		
		self._pwm.start(0)
		self._is_started = True
		if direction == Motor.FORWARD:
			if self._flipped:
				self._rotate_backward(speed)
			else:
				self._rotate_forward(speed)
		else:
			if self._flipped:
				self._rotate_forward(speed)
			else:
				self._rotate_backward(speed)


	'''
	Stops spinning the motor
	'''
	def stop(self):
		self._pwm.stop()
		self._is_started = False
		
	
	'''
	Returns True if the motor has been started - i.e. if start() was
	called without a corresponding call to stop()
	'''
	def is_started(self):
		return self._is_started
		
