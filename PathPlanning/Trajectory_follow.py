import numpy as np
import matplotlib.pyplot as plt
import math
from djitellopy import Tello
import time


# Uncomment lines 10-28 and 106-123 for drone test flies

# # Initializing Tello object
# tello = Tello()
#
# # Connect to Tello
# tello.connect()
# print(tello.get_battery())
# # Start video stream
# tello.streamon()
#
#
# # Trajectory program
# def trajectory_follow(position_derivated, dt):
#     for i in range(len(position_derivated)):
#         print("Sending velocity: ", (math.sqrt((position_derivated[i][0] * position_derivated[i][0]) + (
#                 position_derivated[i][1] * position_derivated[i][1]) + (
#                                                         position_derivated[i][2] * position_derivated[i][2])) / dt))
#         tello.send_rc_control(int(position_derivated[i][0]),int(position_derivated[i][1]),int(position_derivated[i][2]),0)
#         time.sleep(dt)
#     tello.send_rc_control(0, 0, 0, 0)
#

def string_to_int(string):
    if string == '1':
        return 1
    elif string == '2':
        return 2
    elif string == '3':
        return 3
    elif string == '4':
        return 4
    elif string == '5':
        return 5
    elif string == '6':
        return 6
    elif string == '7':
        return 7
    elif string == '8':
        return 8
    elif string == '9':
        return 9
    elif string == '0':
        return 0
    else:
        return 'not valid'


def get_positions(q_table):
    positions = []
    for j in range(len(q_table)):
        count = 0
        X = []
        Y = []
        Z = []
        x = 0
        y = 0
        z = 0
        for i in range(len(q_table[j])):
            if count == 0:
                if string_to_int(q_table[j][i]) != 'not valid':
                    X.append(string_to_int(q_table[j][i]))

            if count == 1:
                if string_to_int(q_table[j][i]) != 'not valid':
                    Y.append(string_to_int(q_table[j][i]))

            if count == 2:
                if string_to_int(q_table[j][i]) != 'not valid':
                    Z.append(string_to_int(q_table[j][i]))

            if q_table[j][i] == ' ' and string_to_int(q_table[j][i - 1]) != 'not valid':
                count += 1

        for i in range(len(X)):
            x += X[i] * pow(10, len(X) - i - 1)
        x = int(round(x))
        for i in range(len(Y)):
            y += Y[i] * pow(10, len(Y) - i - 1)
        y = int(round(y))
        for i in range(len(Z)):
            z += Z[i] * pow(10, len(Z) - i - 1)
        z = int(round(z))
        positions.append(np.array([x, y, z]))
    return positions


f = open("trajectory.txt", "r")
positions = f.read().split(',')
positions = get_positions(positions)

dt = 0.5  # time needed for 1 step

# Applying waypoint method
positions_derivated = [(0, 0, 0)]
for i in range(1, len(positions)):
    positions_derivated.append((positions[i] - positions[i - 1]) / dt)

# # Taking off
# tello.send_rc_control(0, 0, 0, 0)
# time.sleep(1 / 5)
# tello.takeoff()
# time.sleep(1)
#
# # Start follow given trajectory
# trajectory_follow(positions_derivated, dt)
#
# # Landing
# time.sleep(2)
# tello.land()
#
# # Stop the video stream
# tello.streamoff()
#
# # Disconnect from Tello
# tello.end()

# Plot the trajectory of the drone in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot([pos[0] for pos in positions], [pos[1] for pos in positions], [pos[2] for pos in positions])
plt.show()
