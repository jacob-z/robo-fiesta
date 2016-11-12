from vehicle import Vehicle
import time

vehicle = Vehicle(24, 18, 0)

vehicle.right_motor.start()
vehicle.left_motor.start()

time.sleep(3)

vehicle.right_motor.stop()
vehicle.left_motor.stop()

vehicle.destroy()
