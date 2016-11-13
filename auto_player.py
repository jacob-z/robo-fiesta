# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:47:35 2016

@author: Rachana_B
"""

from vehicle import Vehicle
from buzzer import Buzzer
import sys
from time import sleep
from pitch import Pitch

vehicle = Vehicle(24, 18, 2)
vehicle.buzzer.play_song(sys.argv[1])
while vehicle.buzzer.is_playing():
    pass
vehicle.destroy()
