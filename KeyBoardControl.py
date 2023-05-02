#This keyboard control uses arrows to move the drone to corressponding directions
#Uses A,D to control the angle and W,S to move up and down
#Uses F to take off
#Uses L to land

from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def getKeyBoardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100

    if kp.getKey("LEFT"): #Movements controls
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    elif kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    elif kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    elif kp.getKey("a"):
        yv = speed
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("f"): #Take off
        drone.takeoff()
    if kp.getKey("l"): #Land
        drone.land()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyBoardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
