import pickle
import os
from envDeadEnd import GraphEnvironment


# Create a graph
num_nodes = 10
num_switches = 10
source = 0
destination = 1

muted = True # Set to True to mute the output

if os.path.exists("graph.gpickle"):
    with open("graph.gpickle", "rb") as f:
        graph = pickle.load(f)

# save the agent for later use
with open("agent.pickle", "rb") as f:
    q_learning_agent = pickle.load(f)
    
# Test the agent
env = GraphEnvironment(graph, source, destination)

while True:
    action = q_learning_agent.choose_action_without_randomness(env.current_node, env.action_space.n)
    state, reward, done, info = env.step(action)
    if done:
        break
    
print(f"Path: {env.path}\n")