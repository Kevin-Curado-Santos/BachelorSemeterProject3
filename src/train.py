import numpy as np
from graphForTraining import create_graph
import networkx as nx
from environment import ShortestPathEnv

# Create a graph
graph = create_graph()

env = ShortestPathEnv(graph, 1, 63)

# Initialize the Q-table
Q = np.zeros((len(graph.nodes), len(graph.nodes), len(graph.nodes)))

# Train the agent using the Q-learning algorithm
for i in range(10000):
    # Reset the environment
    state = env.reset()

    # Take some steps
    for j in range(10):
        # Choose an action
        action = np.argmax(Q[state[0]-1][state[1]-1])

        # Take a step in the environment
        next_state, reward, done, _ = env.step(action+1)

        # Update the Q-table
        Q[state[0]-1][state[1]-1][action] = reward + np.max(Q[next_state[0]-1][next_state[1]-1])

        # Update the state
        state = next_state

        # Check if the episode is done
        if done:
            break

# Print the final Q-table
print(Q)