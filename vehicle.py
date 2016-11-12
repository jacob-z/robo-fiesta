'''
Authors: Michael Friedman
Created: 11/12/16

Description: Container for the entire vehicle. Can retrieve the
components and manage their connections on the Pi.
'''

from Tkinter import *
import RPi.GPIO as GPIO
from motor import Motor

class Vehicle:
    
    '''
    Initializes a vehicle, given the channel for the left/right motors
    and the photo resistor
    '''
    def __init__(self, channel_left, channel_right, channel_photo_resistor):
        self._left_motor = Motor(channel_left)
        self._right_motor = Motor(channel_right, flipped=True)
        self._photo_resistor = None # TODO: Implement PhotoResistor
        
    
    # Getters
    @property
    def left_motor(self):
        return self._left_motor
            
    @property
    def right_motor(self):
        return self._right_motor

    @property
    def photo_resistor(self):
        return self._photo_resistor

    '''
    Closes connections to all components of the vehicle
    '''
    def destroy(self):
        self._left_motor.stop()
        self._right_motor.stop()
        GPIO.cleanup()
