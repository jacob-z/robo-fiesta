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
import threading

class Buzzer:
    
    '''
    Creates a new instance of a Buzzer object
    
    Args:
        channel_out: int indicating output channel (pin) on the Pi
    '''
    def __init__(self, channel_out):
        self._channel_out = channel_out
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._channel_out, GPIO.OUT)
        self._is_playing = False
    
    
    '''
    Plays a note.
    
    Args:
        pitch: Pitch object for the pitch to play
        beats: float number of beats
        tempo: integer tempo
    '''
    def play_note(self, pitch, beats, tempo):
        freq = pitch.freq()
        if freq != -1:
            pwm = GPIO.PWM(self._channel_out, pitch.freq())
            pwm.start(50)
        sleep(beats * (60.0 / tempo))
        if freq != -1:
            pwm.stop()
        
        
    '''
    Helper method for play_song()
    
    Process for playing a song
    '''
    def _play(self, filename):
        f = open(filename, 'r')
        
        line_num = 1
        for line in f:
            if not self._is_playing:
                break
            
            # Get tempo
            if (line_num == 1):    
                tempo = int(line)
            
            # Play song
            if (len(line) != 0 and line_num > 1):
                [pitch, accidental, octave, beats] = line.split()
                self.play_note(Pitch(pitch, accidental, int(octave)), float(beats), tempo)
            line_num += 1
            sleep(0.01)
        self._is_playing = False
        
        
    '''
    Plays a song from a file.
    
    Args:
        filename: string name of the file from which to play the song
    '''
    def play_song(self, filename):
        self._is_playing = True
#        threading.Thread(target=self._play, args=(filename,)).start()
        self._play(filename)        
    
    '''
    Force stops the song
    '''
    def stop_song(self):
        self._is_playing = False
        
        
    '''
    Returns True if the buzzer is playing a song, False if not
    '''
    @property
    def is_playing(self):
        return self._is_playing
