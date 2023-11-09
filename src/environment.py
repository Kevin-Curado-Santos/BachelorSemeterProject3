import gymnasium as gym
from graphForTraining import generate_graph
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
        
        self.neighbors = list(self.graph.neighbors(self.state))

        self.num_nodes = len(self.graph.nodes())
        self.action_space = self.neighbors  # Actions are node indices
        self.observation_space = gym.spaces.Discrete(self.num_nodes)  # Observations are node indices

    def reset(self):
        # Reset the state and other variables
        self.state = self.source
        self.done = False

        return self.state

    def step(self, action):
        print("action: {}".format(action))
        # print("neighbors: {}".format(self.neighbors))
        self.state = self.neighbors[action]
        self.path.append(self.state)
        self.neighbors = list(self.graph.neighbors(self.state))
        self.action_space = self.neighbors
    
        if self.state == self.destination:
            reward = 100.0
            self.done = True
        elif self.state in self.shortest_path:
            reward = -1.0
            self.done = False
        else:
            reward = -100.0
            self.done = False
        
        return self.state, reward, self.done, {}
    
    def render(self, mode='human', close=False):
        # Print the current state to the screen
        print(self.state)
        
    def random_action(self):
        action = np.random.choice(self.neighbors)
        print("random action: {}".format(action))
        print("neighbors: {}".format(self.neighbors))
        return self.neighbors.index(action)

# # Create a graph
# graph = generate_graph(100, 150)

# # create an environment
# env = ShortestPathEnv(graph, 0, 99)

# # Reset the environment
# obs = env.reset()

# # Print the initial state
# print("Initial state: {}".format(obs))

# while not env.done:
#     # Take a random action
#     action = env.action_space.sample()
#     obs, reward, done, _ = env.step(action)
#     print("Next state: {}, reward: {}, done: {}".format(obs, reward, done))
    
# print("Path: {}".format(env.path))
# print("Shortest path: {}".format(env.shortest_path))