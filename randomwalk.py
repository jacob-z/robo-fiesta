'''
Authors: Michael Friedman
Created: 11/12/16

Description: Class implements a random walk. Randomly moves the vehicle
left, right, or forward.
'''

import sys
import random
from vehicle import Vehicle
from time import sleep
import threading


class RandomWalk:
    
    '''
    Initializes the RandomWalk object for a vehicle that plays a song.
    
    Args:
        song_filename: string path to filename containing song to play
    '''
    def __init__(self, song_filename):
        self._song_filename = song_filename
        self._moving = False
        self._vehicle = Vehicle(24, 18, 2)
    
    '''
    Plays the vehicle's song
    '''
    def _play(self):
        self._vehicle.buzzer.play_song(self._song_filename)
        
        
    def _walk(self):
         # Setup
        channel_left_motor = 24
        channel_right_motor = 18
        channel_buzzer = 2
        vehicle = Vehicle(channel_left_motor, channel_right_motor, channel_buzzer)
        
        # Play song
        vehicle.buzzer.play_song(self._song_filename)
        
        # Main loop
        self._moving = True
        while self._moving:
            # Take a random step 
            r = random.randint(0, 6)
            print r
            if r in [0, 1]:
                vehicle.turn(Vehicle.LEFT)
                vehicle.move(Vehicle.FORWARD)
            elif r in [2, 3]:
                vehicle.turn(Vehicle.RIGHT)
                vehicle.move(Vehicle.FORWARD)
            elif r in [4, 5]:
                vehicle.move(Vehicle.FORWARD)
            else:
                vehicle.buzzer.play_song(self._song_filename)
            sleep(2)

            
        # Loop ends when stop() is called
        vehicle.stop()
        vehicle.buzzer.stop_song()
        vehicle.destroy()
        
    '''
    Starts the random walk
    '''
    def start(self):
       threading.Thread(target=self._walk).start()
       
        
    '''
    Stops the random walk
    '''
    def stop(self):
        self._moving = False
    
    
'''
Executes random walk

Args:
    song_filename: filename
'''
def main(song_filename):
    rw = RandomWalk(song_filename)
    rw.start()
    raw_input('Press enter to end walk\n')
    rw.stop()
            
    
if __name__ == '__main__':
    main(sys.argv[1])
    
