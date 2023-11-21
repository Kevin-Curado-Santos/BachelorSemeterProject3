from env import GraphEnvironment
from gen2 import generate_static_network, save_graph, load_graph
from agent import QLearningAgent
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

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
q_learning_agent = QLearningAgent(state_size, alpha = 0.15, epsilon=0.2)

# Training the Q-learning agent
num_episodes = 1000
num_experiments = 100
max_steps = 1000

path_count = 0

goal_reached_count = 0
shortest_path = nx.shortest_path(graph, source, destination)
best_path = None

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    while True:
        action = q_learning_agent.choose_action(state, action_size)
        next_state, reward, done, _ = env.step(action)
        action_size = env.action_space.n
        q_learning_agent.update_q_table(state, action, reward, next_state, action_size)
        
        state = next_state
        total_reward += reward
        
        if done:
            goal_reached_count += 1
            break
    if best_path is None or len(env.path) < len(best_path):
        best_path = env.path
    if not muted:
        print(f"Episode: {episode + 1}, Total Reward: {total_reward}")
        print(f"Path: {env.path}\n")
        #print(f"Optimal Path: {nx.shortest_path(graph, source, destination)}\n")
    
print(f"Best path: {best_path}")
if len(best_path) == len(shortest_path):
    path_count += 1

        # if path_count > best_path_count:
        #     best_path_count = path_count
        #     best_alpha = alpha
        #     best_epsilon = epsilon
            
        #print(f"Alpha: {alpha}, Epsilon: {epsilon}, Path count: {path_count}")
print(f"Path count: {path_count}")
#print(f"Best alpha: {best_alpha}, Best epsilon: {best_epsilon}, Best path count: {best_path_count}")
