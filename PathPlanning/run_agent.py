# File: run_agent.py
# Description: Running algorithm
# Environment: PyCharm and Anaconda environment


# Importing classes
from env import Environment
from agent_brain import QLearningTable
import numpy as np


# Processing trajectory data to save
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


# Processing trajectory data to save
def get_positions(q_table):
    positions = []
    for j in range(len(q_table)):
        count = 0
        freeze = 0
        X = []
        Y = []
        x = 0
        y = 0
        for i in range(len(q_table[j])):
            if q_table[j][i] == '.':
                freeze = 1
            if q_table[j][i] == ' ':
                count += 1
                freeze = 0
            if freeze == 0:
                if count == 0:
                    if string_to_int(q_table[j][i]) != 'not valid':
                        X.append(string_to_int(q_table[j][i]))

                if count == 1:
                    if string_to_int(q_table[j][i]) != 'not valid':
                        Y.append(string_to_int(q_table[j][i]))
        for i in range(len(X)):
            x += X[i] * pow(10, len(X) - i - 1)
        x = int(round(x - 3))
        for i in range(len(Y)):
            y += Y[i] * pow(10, len(Y) - i - 1)
        y = int(round(y - 3))
        positions.append(np.array([x, y, 0]))
    return positions


def update():
    # Resulted list for the plotting Episodes via Steps
    steps = []

    # Summed costs for all episodes in resulted list
    all_costs = []

    for episode in range(5000):
        # Initial Observation
        observation = env.reset()

        # Updating number of Steps for each Episode
        i = 0

        # Updating the cost for each episode
        cost = 0

        while True:
            # Refreshing environment
            env.render()

            # RL chooses action based on observation
            action = RL.choose_action(str(observation))

            # RL takes an action and get the next observation and reward
            observation_, reward, done = env.step(action)

            # RL learns from this transition and calculating the cost
            cost += RL.learn(str(observation), action, reward, str(observation_))

            # Swapping the observations - current and next
            observation = observation_

            # Calculating number of Steps in the current Episode
            i += 1

            # Break while loop when it is the end of current Episode
            # When agent reached the goal or obstacle
            if done:
                steps += [i]
                all_costs += [cost]
                break

    # Showing the final route
    env.final()

    # Showing the Q-table with values for each action
    RL.print_q_table()

    # Plotting the results
    RL.plot_results(steps, all_costs)

    # Calculate trajectory
    positions = get_positions(RL.q_table_final.index)

    # Saving the trajectory data
    f = open("trajectory.txt", "w+")
    print('Writing...')
    for i in range(len(positions)):
        f.write(str(positions[i]))
        if i != len(positions) - 1:
            f.write(",")
    print('Saved')


# Commands to be implemented after running this file
if __name__ == "__main__":
    # Calling for the environment
    env = Environment()
    # Calling for the main algorithm
    RL = QLearningTable(actions=list(range(env.n_actions)))
    # Running the main loop with Episodes by calling the function update()
    env.after(100, update)  # Or just update()
    env.mainloop()
