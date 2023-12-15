from gen2 import generate_static_network
from envDeadEnd import GraphEnvironment
import networkx as nx
import matplotlib.pyplot as plt

num_nodes = 10
num_switches = 10
source = 0
destination = 1

# Create a graph
graph = generate_static_network(num_nodes, num_switches, max_switch_connections=3)

# save the graph to a png
nx.draw(graph, with_labels=True)
plt.savefig("graph.png")

# Create an environment
env = GraphEnvironment(graph, source, destination)

# Reset the environment
obs = env.reset()

# Print the initial state
print("Initial state: {}".format(obs))

max_iter = 0 
while max_iter < 100:
    # Take a random action
    action = env.action_space.sample()
    next_state, reward, done, _ = env.step(action)
    if done:
        break
    print("Action: {}, Next state: {}, Reward: {}, Done: {}".format(action, next_state, reward, done))
    max_iter += 1
    
print("Shortest path: {}".format(env.path))
    