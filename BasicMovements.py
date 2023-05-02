from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.takeoff()
sleep(1)
drone.land()
