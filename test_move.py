'''
Authors: Michael Friedman
Created: 11/12/16

Description: Tests vehicle motion forward for a brief time.
'''

from vehicle import Vehicle
from time import sleep
import sys


'''
Moves the vehicle both forward and backward for a specified period of
time.

Args:
    time: float value for time to move the vehicle forward (in seconds)
'''
def main(time):
    vehicle = Vehicle(24, 18, 0)
    vehicle.move(Vehicle.FORWARD)
    sleep(time)
    vehicle.move(Vehicle.BACKWARD)
    sleep(time)
    vehicle.destroy()

if __name__ == '__main__':
    main(float(sys.argv[1]))
