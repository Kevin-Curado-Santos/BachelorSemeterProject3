import gym
import numpy as np
from environment import ShortestPathEnv
from graphForTraining import generate_graph

graph = generate_graph(100, 150)

# Define and create the environment
env = ShortestPathEnv(graph, 0, 50)

# Q-learning hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 0.1  # Exploration rate
num_episodes = 1000

# Initialize the Q-table as a dictionary
q_table = {}

# Training loop
for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        if state not in q_table:
            num_actions = len(env.action_space)
            q_table[state] = np.zeros(num_actions)

        if np.random.uniform(0, 1) < epsilon:
            action = env.random_action()  # Explore
        else:
            action = np.argmax(q_table[state])  # Exploit

        next_state, reward, done, _ = env.step(action)

        if next_state not in q_table:
            num_actions = len(env.action_space)
            q_table[next_state] = np.zeros(num_actions)

        # Q-table update
        q_table[state][action] = q_table[state][action] + alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state][action])

        state = next_state

# Evaluate the trained agent
total_reward = 0
state = env.reset()
while not env.done:
    if state in q_table:
        action = np.argmax(q_table[state])
    else:
        action = env.random_action() # Handle states not in Q-table
    state, reward, done, _ = env.step(action)
    total_reward += reward

print(f"Total reward on the shortest path: {total_reward}")
print("Shortest path:", env.shortest_path)
# print("Agent's path:", env.path)
print("Number of steps:", len(env.path))