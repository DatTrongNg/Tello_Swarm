# Towards experimental validation of structure of motion estimation problem by using the DJI Tello Ryze drone SDK

**I. Introduction:**

In recent years, the utilization of drones has witnessed exponential growth across various industries, ranging from aerial photography and surveillance to delivery services and infrastructure inspection. The efficient and accurate control of drones requires precise information about their spatial position, particularly their depth or distance from objects in their surroundings. Determining depth information traditionally relied on the use of multiple cameras or complex sensor arrays, which added to the cost and weight of drones. However, with advancements in artificial intelligence and specifically, neural networks, it is now possible to calculate depth from a single image captured by a drone's camera. This project seeks to leverage the power of neural networks to calculate the depth of images captured by drones, enabling precise location determination and enhancing drone control capabilities. By employing a single camera-based depth estimation approach, we aim to provide an efficient and cost-effective solution that enhances the autonomy, safety, and performance of drones across various industries. 

**II. Objective:**

Integrate a distance estimation NN model into a drone control system, allowing for the estimation of the drone's location based on the depth information derived from its camera feed; therefore, having suitable coressponding action.

**III. Methodology:**

_1. Drone's movement control using waypoint:_

The methodology for controlling a DJI Tello drone using waypoint-based methods involves leveraging the capabilities of the DJI Tello Software Development Kit (SDK) and implementing a waypoint navigation system. This approach allows for precise control over the drone's flight path by specifying a sequence of predefined waypoints that the drone should follow.

To begin, the first step is to establish a connection between the controlling device (In this project, we use a laptop connect with the drone via WIFI).

The drone's movement is controlled by controlling 4 motors with two rotating clockwise (CW) and the other two rotating counterclockwise (CCW).

Next, the waypoints for the drone's flight path need to be defined. Waypoints are specific coordinates in three-dimensional space that represent the desired positions and altitudes for the drone to navigate through. There are many ideas to define the path, but in this project, I choose reinforcement learning - Q_learning to plan the flight path.

Once the waypoints are defined, the waypoint navigation system is implemented using the DJI Tello SDK. This involves sending commands to the drone to instruct it to fly from one waypoint to the next. 

The trajectory result valuated using the Vicon system and compare with the input trajectory.

_2. Flight path - planning using reinforcemant learning:_

The method applied is here is the same method used by Valentyn N. Sichkar(1). Q-learning is a model-free reinforcement learning algorithm that aims to find the optimal policy for an agent in an environment without any prior knowledge. It utilizes a Q-table, which is a lookup table storing the expected rewards for all possible state-action pairs.

The algorithm iteratively updates the Q-values in the Q-table based on the agent's experiences. At each time step, the agent observes the current state, selects an action based on an exploration-exploitation strategy (such as epsilon-greedy), executes the action, and receives a reward along with the next state.

The Q-value update equation in Q-learning is:

Q(s, a) = Q(s, a) + α * [R + γ * max(Q(s', a')) - Q(s, a)]

Here, Q(s, a) represents the Q-value of taking action a in state s, R is the immediate reward obtained, s' is the next state, α is the learning rate, and γ is the discount factor that balances the importance of immediate and future rewards.

The update equation propagates the future rewards by considering the maximum Q-value achievable from the next state. Over time, the Q-values converge to their optimal values, reflecting the long-term expected rewards.

The Q-learning algorithm continues this process of exploration, action selection, and Q-value updates until it converges to the optimal policy, where the agent knows the best action to take in each state. Once the Q-table is learned, the agent can navigate the environment by selecting actions with the highest Q-values.

_3. Environment building using NN - DenseDepth:_

The idea is to use multiple cameras from multiple drones (swarm drone ideally) which would give the drones location using a NN model that would give distances from drones to drones and to other objects. In this project, we use the NN model Ibraheem Alhashim (2) has developed.

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/b541e318-e49d-4dec-8593-786d8dfe9bc1)

A straightforward encoder-decoder architecture with skip connections. The encoder part is a pre-trained truncated DenseNet-169 with no additional modifications. The decoder is composed of basic blocks of convolutional layers applied on the concatenation of the 2× bilinear upsampling of the previous block with the block in the encoder with the same spatial size after upsampling.

Using the model estimating a depth map from a single RGB image , we implement the model on a real-time cammera, uses the obtained result and a look up table to have the distance estimation. 

**IV. Experiments and result:**

_1. Set up:_

The Tello drone's codes is based on a coordinate attached ti itself with the following orientation:

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/3f00e71a-a614-40e0-ab10-4cfcee665c8a)

The unit used in the trajectory and velocity of the drone: cm and cm/s.

Trajectory validation is using Vicon System - There are 4 bullets attached to the drone from multiple directions.

_2. Results:_

_2.1. Waypoints:_

The drone is able to do from simple to complex trajectories with arevage speed. There are still errors since there is no feed back-loop as the location defining part is not fully developed.

- The drone was doing a circle trajectory(radius = 500mm):

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/b60d7540-8713-4cb4-9f95-18d25dddb105)

- Apply waypoint to more complex trajectory (unit are in cm):

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/daa7c784-3f8c-45c1-ac1d-05dff410500e)

![Tello_Trajectory](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/77455e26-23ce-4240-9225-01780980bf17)

_2.2. Waypoints and Q-learning:_

Applying Q-learning on a pre-built environment, we obtained the trajectory:

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/b0e8ab6d-604a-4db8-b1ce-838b76a7841b)

Applying the waypoints method under the Vicon System(in mm):

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/f5eb258e-8a9e-4d1a-9211-ba2310a80591)

_2.3. NN Dense-Depth:_

The Dense-Depth NN model is implemented in real-time and tested:

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/bcf0d58d-1d89-42ca-ad93-41c12c752bb6)

![image](https://github.com/DatTrongNg/Tello_Swarm/assets/87078249/17084b30-b3a1-4647-9364-437d9a5eff84)

We haven't have a look up table for converting the result into digital signal for environment building.

**V. Conclusion:**

There are still plenty of  works and problems need to be done. The environment building is not fully completed; Q-learning is not really efficient since the environment is built at the same time the drone moves; need to implement the project on multiple drones (Swarm application) for feed back to minimize errors. However, the result shown that the project is potential and do-able.

**VI. Implementation:**

Need to include the following packages: numpy, matplotlib, math, djitellopy, time, pandas, tkinter, PIL, keras, pillow, scikit-learn, scikit-image, opencv-python, pydot

After connected to a Tello SDK drone:

_1. Trajectory follow:_

Access the 'PathPlanning' folder.

The trajectory is imported from 'trajectory.txt' - change the file for different trajectory. Simply run 'Trajectory_follow.py' for the drone to follow the given trajectory.

_2. Path planning:_

Access the 'PathPlanning' folder.

The environment is defined by 'env.py'. 

Simply run 'run_agent.py' for planning the trajectory and write the trajectory to 'trajectory.txt'.

_3. Real-time Dense-Depth:_

Download the model 'nyu' from: https://drive.google.com/file/d/19dfvGvDfCRYaqxVKypp1fRHwK7XtSjVu/view

Put the 'nyu' file in 'DenseDepth' folder.

Run 'ImageCapture.py' for capturing images from the drone's camera to '\DenseDepth\examples'.

Access 'DenseDepth" folder.

Run 'test.py' for Depth estimation.

**Reference:**

(1) Valentyn N. Sichkar, "Reinforcement Learning Algorithms in Global Path Planning for Mobile Robot", 2019 International Conference on Industrial Engineering, Applications and Manufacturing (ICIEAM)

(2) Ibraheem Alhashim, Peter Wonka, "High Quality Monocular Depth Estimation via Transfer Learning", arXiv:1812.11941v2 [cs.CV] 10 Mar 2019

