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
    def __init__(self):
        self._moving = False
        self._vehicle = Vehicle(24, 18, 2)
    
    '''
    Getter for vehicle
    '''
    @property
    def vehicle(self):
        return self._vehicle

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
        vehicle.buzzer.play_song('ghostbusters.txt')
        
        # Main loop
        self._moving = True
        while self._moving:
            # Take a random step 
            move = random.randint(0, 7)
            song = random.randint(0, 7)
            range_turn_left = range(0, 3)
            range_turn_right= range(3, 6)
            range_move = range(6, 8)
            range_ghostbusters = range(0, 2)
            range_a_unlocked = range(2, 4)
            range_coin = range(4, 6)
            range_starwars = range(6, 7)
            range_callmemaybe = range(7, 8)
            if move in range_turn_left:
                vehicle.turn(Vehicle.LEFT)
            elif move in range_turn_right:
                vehicle.turn(Vehicle.RIGHT)
            else:
                vehicle.move(Vehicle.FORWARD)
            
            if not vehicle.buzzer.is_playing:
                if song in range_ghostbusters:
                    vehicle.buzzer.play_song('ghostbusters.txt')
                elif song in range_a_unlocked:
                    vehicle.buzzer.play_song('a_unlocked.txt')
                elif song in range_coin:
                    vehicle.buzzer.play_song('coin.txt')
                elif song in range_starwars:
                    vehicle.buzzer.play_song('starwars.txt')
                else:
                    vehicle.buzzer.play_song('callmemaybe.txt')
            else:
                sleep(1)
            
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
def main():
    rw = RandomWalk()
    rw.start()
    msg = 'Command? (l/r/x)\n'
    cmd = raw_input(msg)
    while (cmd != 'x'):
        if cmd == 'l':
            rw.vehicle.turn(Vehicle.LEFT)
        elif cmd == 'r':
            rw.vehicle.turn(Vehicle.RIGHT)
        cmd = raw_input(msg)
    rw.stop()
            
    
if __name__ == '__main__':
    main()
    
