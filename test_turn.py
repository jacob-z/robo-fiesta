'''
Authors: Michael Friedman
Created: 11/12/16

Description: Tests the left and right turning of the vehicle.
'''

from vehicle import Vehicle
from time import sleep

'''
Turns the vehicle both left and right.
'''
def main():
    vehicle = Vehicle(24, 18, 0)
    vehicle.turn(Vehicle.LEFT)
    vehicle.turn(Vehicle.RIGHT)
    vehicle.destroy()
    
if __name__ == '__main__':
    main()
