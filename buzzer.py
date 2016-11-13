'''
Authors: Michael Friedman
Created: 11/12/16

Description: Represents the buzzer. Supports operations for playing
different notes.
'''

from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from pitch import Pitch

class Buzzer:
    
    # Public constants
    # TODO: Add constants for the note frequencies
    
    
    
    '''
    Creates a new instance of a Buzzer object
    
    Args:
        channel_out: int indicating output channel (pin) on the Pi
    '''
    def __init__(self, channel_out):
        self._channel_out = channel_out
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._channel_out, GPIO.OUT)
    
    
    '''
    Plays a note.
    
    Args:
        pitch: character in ABCDEFG
        accidental: '#' for sharp, 'b' for flat, '?' for natural
        octave: integer from 0 to 7
        beats: float number of beats
        tempo: integer tempo
    '''
    def play(self, pitch, accidental, octave, beats, tempo):
        pwm = GPIO.PWM(self._channel_out, Pitch(pitch, accidental, octave).freq())
        pwm.start(50)
        sleep(beats * (60.0 / tempo))
        pwm.stop()
