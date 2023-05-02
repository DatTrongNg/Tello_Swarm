from djitellopy import Tello
import time
import math

# Initializing Tello object
tello = Tello()

def Circle_curve(Circle_Center_Angle, radius, Curve_Angle, speed):
    angleSpeed = speed/radius
    circleTime = 2 * math.pi / angleSpeed
    # Start the circle path
    startTime = time.time()
    while (time.time() - startTime) < circleTime * (Curve_Angle / (2 * math.pi)):
        T = time.time()
        time.sleep(1 / 5)  # delay 1/4 sec for better accuracy
        DeltaT = (time.time() - T)
        tello.send_rc_control(int(speed * math.cos(-Circle_Center_Angle + math.pi)), int(speed * math.sin(-Circle_Center_Angle + math.pi)), 0, 0)
        # update Center
        Circle_Center_Angle = Circle_Center_Angle - angleSpeed * DeltaT
    # stop
    time.sleep(1 / 5)
    tello.send_rc_control(0, 0, 0, 0)
# Connect to Tello
tello.connect()
print(tello.get_battery())
# Start video stream
tello.streamon()

# Defining circle path parameters

#Circle's properties:
radius = 50 #cm
Theta1 = 0 #for defining the center of the circle

#The angle drone would rotate
Theta2 = math.pi*2
#Velocity
speed = 35

# Taking off
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1/5)
tello.takeoff()
time.sleep(1)

Circle_curve(Theta1,radius, Theta2,speed)

# Landing
time.sleep(2)
tello.land()

# Stop the video stream
tello.streamoff()

# Disconnect from Tello
tello.end()



