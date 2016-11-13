'''
Authors: Michael Friedman
Created: 11/12/16

Description: Container for the entire vehicle. Can retrieve the
components and manage their connections on the Pi.
'''

from Tkinter import *
import RPi.GPIO as GPIO
from motor import Motor
from buzzer import Buzzer
from time import sleep

class Vehicle:
    
    # Public constants
    FORWARD = Motor.FORWARD
    BACKWARD = Motor.BACKWARD
    LEFT = True
    RIGHT = False
    
    # Private constants
    _IS_NOT_MOVING = 0
    _IS_MOVING_FORWARD = 1
    _IS_MOVING_BACKWARD = 2
    
    '''
    Initializes a vehicle, given the channel for the left/right motors
    and the photo resistor
    '''
    def __init__(self, channel_left, channel_right, channel_buzzer):
        self._left_motor = Motor(channel_left)
        self._right_motor = Motor(channel_right, flipped=True)
        self._buzzer = Buzzer(channel_buzzer)
        self._status = Vehicle._IS_NOT_MOVING
        
    #-------------------------------------------------------------------
    # Getters
    #-------------------------------------------------------------------
    
    @property
    def left_motor(self):
        return self._left_motor
            
    @property
    def right_motor(self):
        return self._right_motor

    @property
    def buzzer(self):
        return self._buzzer
    
    
    #-------------------------------------------------------------------
    # Motion mechanics
    #-------------------------------------------------------------------
    
    '''
    Moves the vehicle in the direction specified. Continues until
    stop() is called
    
    Args:
        direction: boolean indicating direction (takes Vehicle.FORWARD
            or Vehicle.BACKWARD)
    '''
    def move(self, direction):
        if direction == Vehicle.FORWARD:
            self._status = Vehicle._IS_MOVING_FORWARD
        else:
            self._status = Vehicle._IS_MOVING_BACKWARD
        
        motors = [self._left_motor, self._right_motor]
        for motor in motors:
            motor.stop()
            motor.start(direction=direction)
    
    '''
    Turns the vehicle in the specified direction, then restores the
    previous motion.
    
    Args:
        direction: boolean indicating left or right turn (takes
            Vehicle.LEFT or Vehicle.RIGHT)
    '''
    def turn(self, direction):
        # Determine which motor to turn in which direction
        if direction == Vehicle.LEFT:
            motor_forward = self._right_motor
            motor_backward = self._left_motor
        else:
            motor_forward = self._left_motor
            motor_backward = self._right_motor
            
        # Turn
        motor_backward.stop()
        motor_backward.start(direction=Motor.BACKWARD)
        motor_forward.stop()
        motor_forward.start(direction=Motor.FORWARD)
        sleep(2)
        
        # Restore previous motion
        if self._status == Vehicle._IS_MOVING_FORWARD:
            self.move(Vehicle.FORWARD)
        elif self._status == Vehicle._IS_MOVING_BACKWARD:
            self.move(Vehicle.BACKWARD)
        else:
            self.stop()
        
    '''
    Stops the vehicle
    '''
    def stop(self):
        self._status = Vehicle._IS_NOT_MOVING
        motors = [self._left_motor, self._right_motor]
        for motor in motors:
            motor.stop()
            
    #-------------------------------------------------------------------
    # Cleanup
    #-------------------------------------------------------------------

    '''
    Closes connections to all components of the vehicle
    '''
    def destroy(self):
        self.stop()
        GPIO.cleanup()
