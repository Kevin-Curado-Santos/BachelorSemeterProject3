from env import GraphEnvironment
from gen2 import generate_static_network, save_graph, load_graph
from agent import QLearningAgent
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Create a graph
num_nodes = 10
num_switches = 10
source = 0
destination = 1

muted = False # Set to True to mute the output

if os.path.exists("graph.gpickle"):
    graph = load_graph("graph.gpickle")
else:
    graph = generate_static_network(num_nodes, num_switches, max_switch_connections=3)
    save_graph(graph, "graph.gpickle")
    
# save the graph to a png
nx.draw(graph, with_labels=True)
plt.savefig("graph.png")

# Assuming you have already defined and instantiated the GraphEnvironment
env = GraphEnvironment(graph, source, destination)

# Q-learning agent setup
# alpha_list = np.arange(0.0, 1.05, 0.05)
# epsilon_list = np.arange(0.0, 1.05, 0.05)
# gamma = 0.9

# best_alpha = None
# best_epsilon = None
# best_path_count = -np.inf

# for alpha in alpha_list:
#     for epsilon in epsilon_list:
state_size = len(env.graph.nodes)
action_size = env.action_space.n
q_learning_agent = QLearningAgent(state_size, alpha = 0.15, epsilon=0.0)

# Training the Q-learning agent
num_episodes = 100000
num_experiments = 100
max_steps = 1000

path_count = 0

goal_reached_count = 0
shortest_path = nx.shortest_path(graph, source, destination)

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0
    state_size = len(env.graph.nodes)
    action_size = env.action_space.n
    
    while True:
        action = q_learning_agent.choose_action(state, action_size)
        next_state, reward, done, _ = env.step(action)
        action_size = env.action_space.n
        q_learning_agent.update_q_table(state, action, reward, next_state, action_size)
        
        state = next_state
        total_reward += reward
        
        if done:
            if state == destination:
                goal_reached_count += 1
            break
    if env.path == shortest_path:
        path_count += 1
    if not muted:
        print(f"Episode: {episode + 1}, Total Reward: {total_reward}")
        print(f"Path: {env.path}\n")
            
print(f"Path count: {path_count}")
print(f"Ratio: {path_count/num_episodes}")

# save the agent for later use
with open("agent.pickle", "wb") as f:
    pickle.dump(q_learning_agent, f)


# with open("output.txt", "w") as f:
#     f.write(q_learning_agent.q_table.__str__())
