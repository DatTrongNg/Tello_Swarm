#This keyboard control uses arrows to move the drone to corressponding directions
#Uses A,D to control the angle and W,S to move up and down
#Uses F to take off
#Uses L to land
#Uses P for taking pictures

from djitellopy import tello
import KeyPressModule as kp
import time
import cv2

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

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
        time.sleep(3)

    if kp.getKey('p'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    vals = getKeyBoardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])



