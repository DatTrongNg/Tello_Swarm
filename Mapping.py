from djitellopy import tello
import KeyPressModule as kp
import numpy as np
from time import sleep
import cv2
import math

## PARAMETERS ##
fspeed = 12 #Need more validations
aspeed = 36
interval = 0.25

dInterval = fspeed*interval
aInterval = aspeed*interval
####
x,y = 500,500
a = 0
yaw = 0

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

points = [(0,0), (0,0)]

def getKeyBoardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 10
    aspeed = 50
    d = 0
    global x,y,yaw, a

    if kp.getKey("LEFT"): #Movements controls
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180
    elif kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90
    elif kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    elif kp.getKey("a"):
        yv = aspeed
        yaw -= aInterval
    elif kp.getKey("d"):
        yv = -aspeed
        yaw += aInterval

    if kp.getKey("f"): #Take off
        drone.takeoff()
    if kp.getKey("l"): #Land
        drone.land()

    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img,point,5,(0,0,255),cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500) / 100},{(points[-1][1] - 500) / 100})m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 0, 255), 1)


while True:
    vals = getKeyBoardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000,1000,3),np.uint8)
    if (points[-1][0] != vals[4]or points[-1][1]!= vals[5]):
        points.append([vals[4],vals[5]])
    drawPoints(img, points)

    cv2.imshow("Output",img)
    cv2.waitKey(1)