import gym
from graphForTraining import create_graph
import networkx as nx
import numpy as np

class ShortestPathEnv(gym.Env):
    def __init__(self, graph, source, destination):
        # Initialize the network graph
        self.graph = graph

        # Save the source and destination nodes as attributes
        self.source = source
        self.destination = destination

        # Initialize the state and other necessary variables
        self.state = self.source  # The start and end nodes for the shortest path
        self.done = False
        
        self.shortest_path = nx.dijkstra_path(self.graph, self.source, self.destination)
        
        self.path = [self.source]

        # Define the action space and the observation space
        self.action_space = gym.spaces.Discrete(len(self.graph.nodes))
        self.observation_space = gym.spaces.Tuple((
            gym.spaces.Discrete(len(self.graph.nodes)),
            gym.spaces.Discrete(len(self.graph.edges))
        ))

    def reset(self):
        # Reset the state and other variables
        self.state = self.source
        self.done = False

        return self.state

    def step(self, action):
        # Check if the current state is a dead-end
        if not self.graph.has_edge(self.state, action):
            self.reset()
            return self.state, -1.0, False, {}
        # Calculate the reward based on the length of the path
        reward = 1.0 / len(self.shortest_path)

        # Update the state and other variables
        self.state = action
        self.done = self.state == self.destination
        
        self.path.append(self.state)

        return self.state, reward, self.done, {}

    def render(self, mode='human', close=False):
        # Print the current state to the screen
        print(self.state)

# Create a graph
graph = create_graph()

# Create an instance of the environment
env = ShortestPathEnv(graph, 1, 40)

# Initialize the Q-table for the new graph
Q = np.zeros((len(graph.nodes)))
Q[0] = -1
# Train the agent using the Q-learning algorithm
for i in range(10000):
    # Reset the environment
    state = env.reset()

    # Take some steps
    for j in range(len(env.shortest_path)):
        env.render()
        # Choose an action
        action = np.argmax(Q[state-1])
        print(action)

        # Take a step in the environment
        next_state, reward, done, _ = env.step(action+1)

        # Update the Q-table
        Q[state-1] = np.maximum(Q[state-1], reward + np.max(Q[next_state-1]))

        # Update the state
        state = next_state

        # Check if the episode is done
        if done:
            break

# Print the final Q-table
print('Q:', Q)


# Set the initial state of the environment
env.reset()

# Take some steps in the environment until the destination is reached
while env.state != env.destination:
    # Choose an action using the Q-table
    action = np.argmax(Q[env.state-1])

    # Take a step in the environment
    env.step(action+1)

# Print the shortest path
print('Path:', env.path)