'''
Authors: Michael Friedman
Created: 11/12/16

Description: Randomly moves the vehicle left, right, or forward.
'''

import sys
import random
from vehicle import Vehicle
from time import sleep

'''
Turns the vehicle left
'''
def turn_left(vehicle):
    vehicle.left_motor.stop()
    if not vehicle.right_motor.is_started():
        vehicle.right_motor.start()
    sleep(2)
   
    
'''
Turns the vehicle right
'''
def turn_right(vehicle):
    vehicle.right_motor.stop()
    if not vehicle.left_motor.is_started():
        vehicle.left_motor.start()
    sleep(2)
    

'''
Moves the vehicle forward
'''
def move_forward(vehicle):
    motors = [vehicle.left_motor, vehicle.right_motor]
    for motor in motors:
        if not motor.is_started():
            motor.start()


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
            turn_left(vehicle)
        elif r == 1:
            turn_right(vehicle)
            
        move_forward(vehicle)
        sleep(2)
        t += 1
        
    for motor in motors:
        motor.stop()
    vehicle.destroy()
            
    
if __name__ == '__main__':
    main(int(sys.argv[1]))
