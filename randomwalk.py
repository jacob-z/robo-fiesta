'''
Authors: Michael Friedman
Created: 11/12/16

Description: Randomly moves the vehicle left, right, or forward.
'''

import sys
import random
from vehicle import Vehicle
from time import sleep
from motor import Motor


'''
Executes random walk

Args:
    T: number of time steps (in turns)
'''
def main(T):
    # Setup
    channel_left_motor = 24
    channel_right_motor = 18
    channel_photo_resistor = 0
    vehicle = Vehicle(channel_left_motor, channel_right_motor, channel_photo_resistor)
    
    # Main loop
    motors = [vehicle.left_motor, vehicle.right_motor]
    t = 0
    while t < T:
        r = random.randint(0, 2)
        print r
        if r == 0:
            vehicle.turn(Vehicle.LEFT)
        elif r == 1:
            vehicle.turn(Vehicle.RIGHT)
            
        vehicle.move(Vehicle.FORWARD)
        sleep(2)
        t += 1
        
    vehicle.stop()
    vehicle.destroy()
            
    
if __name__ == '__main__':
    main(int(sys.argv[1]))
