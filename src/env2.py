import gym
import numpy as np
import networkx as nx

class ShortestPathEnv(gym.Env):
    def __init__(self, G, source, destination):
        # G is a NetworkX graph
        # source is the initial state (i.e., the source node)
        # destination is the final state (i.e., the destination node)
        self.G = G
        self.source = source
        self.destination = destination
        
    def reward_function(state, next_state, done):
        if done:
            # the episode is over
            if state == destination:
                # the agent has reached the destination, so it gets a positive reward
                return 1
            else:
                # the agent has not reached the destination, so it gets a negative reward
                return -1
        else:
            # the episode continues
            shortest_path = nx.shortest_path(G, source=source, target=destination, weight='weight')
            if next_state in shortest_path:
                # the agent has taken a step in the direction of the shortest path, so it gets a small positive reward
                return 0.1
            else:
                # the agent has taken a step that is not part of the shortest path, so it gets a small negative reward
                return -0.1

        
    def reset(self):
        # reset the environment by returning the initial state (i.e., the source node)
        return self.source
    
    def step(self, action):
        # the action is the next node in the path
        next_node = action
        
        # check if the action is a valid move
        if next_node not in self.G[self.source]:
            # the action is not a valid move, so the episode is over
            return self.destination, self.reward_function(self.source, self.destination, True), True, {}
        
        # update the source node
        self.source = next_node
        
        # check if the agent has reached the destination
        if self.source == self.destination:
            # the agent has reached the destination, so the episode is over
            return self.destination, self.reward_function(self.source, self.destination, True), True, {}
        
        # the agent has not reached the destination yet, so the episode continues
        return self.source, self.reward_function(self.source, next_node, False), False, {}


# create a new graph
G = nx.Graph()

# add some nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2, weight=1)

# specify the source and destination nodes
source = 1
destination = 2

# create the environment
env = ShortestPathEnv(G, source, destination)

# reset the environment
state = env.reset()

# loop until the episode is over
done = False
while not done:
    # choose a random action
    action = np.random.choice(list(G[state].keys()))
    
    # take a step in the environment
    next_state, reward, done, _ = env.step(action)
