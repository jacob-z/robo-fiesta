# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:47:35 2016

@author: Rachana_B
"""

from vehicle import Vehicle
from buzzer import Buzzer
import sys
from time import sleep

vehicle = Vehicle(24, 18, 2)

f = open(sys.argv[1], 'r')

counter = 1
for line in f:
    # get tempo
    if (counter == 1):    
        tempo = int(line)
    # Loop
    if (len(line) != 0 and counter > 1):
        [pitch, accidental, octave, beats] = line.split()
        vehicle.buzzer.play(pitch, accidental, int(octave), float(beats), tempo)
    counter += 1
    sleep(0.1)
vehicle.destroy()
