import numpy as np
import matplotlib.pyplot as plt
import math
from djitellopy import Tello
import time

# Initializing Tello object
tello = Tello()

# Connect to Tello
tello.connect()
print(tello.get_battery())
# Start video stream
tello.streamon()

# Define the trajectory parameters
duration = 12   # duration of the trajectory in seconds
dt = 0.3        # time step in seconds

# Define the function to calculate the trajectory of the drone at a given time
def get_position(t):
    x = 50*math.cos(t)
    y = 50*math.sin(t)
    z = 15*t
    return int(round(x)), int(round(y)), int(round(z))

#Trajectory program
def trajectory_follow(position_derivated,dt):
    for i in range(len(position_derivated)):
        print((math.sqrt((position_derivated[i][0]*position_derivated[i][0])+(position_derivated[i][1]*position_derivated[i][1])+(position_derivated[i][2]*position_derivated[i][2]))/dt))
        tello.send_rc_control(int(position_derivated[i][0]),int(position_derivated[i][1]),int(position_derivated[i][2]),0)
        time.sleep(dt)
    tello.send_rc_control(0,0,0,0)

# Generate a list of time values
t_values = np.arange(0, duration, dt)

# Generate a list of positions for the drone over time
positions = []
for t in t_values:
    x, y, z = get_position(t)
    positions.append(np.array([x, y, z]))

#Calculate the velocity needed for given trajectory
positions_derivated = [(0,0,0)]
for i in range(1,len(t_values)):
    positions_derivated.append((positions[i]-positions[i-1])/dt)

# Taking off
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1/5)
tello.takeoff()
time.sleep(1)

#Start follow given trajectory
trajectory_follow(positions_derivated,dt)

# Landing
time.sleep(2)
tello.land()

# Stop the video stream
tello.streamoff()

# Disconnect from Tello
tello.end()

# Plot the trajectory of the drone in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot([pos[0] for pos in positions], [pos[1] for pos in positions], [pos[2] for pos in positions])
plt.show()