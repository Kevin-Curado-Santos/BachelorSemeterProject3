import gymnasium as gym
import numpy as np
import networkx as nx

class GraphEnvironment(gym.Env):
    def __init__(self, graph, source, destination):
        super().__init__()
        
        self.graph = graph
        self.source = source
        self.destination = destination
        self.current_node = source
        
        self.done = False
        self.path = []
        
        self.observation_space = gym.spaces.Discrete(len(self.graph.nodes))
        
        # self.unvisited_neighbors = [neighbor for neighbor in self.graph.adj[self.current_node] if neighbor not in self.path]
        self.unvisited_neighbors = list(self.graph.adj[self.current_node])
        self.action_space = gym.spaces.Discrete(len(self.unvisited_neighbors))
        
        
    def reset(self):
        self.current_node = self.source
        self.done = False
        self.path = []
        
        self.unvisited_neighbors = list(self.graph.adj[self.current_node])
        self.action_space = gym.spaces.Discrete(len(self.unvisited_neighbors))
        return self._get_observation()
    
    def step(self, action):
        self.path.append(self.current_node)
        next_node = self.unvisited_neighbors[action]
        self.done = next_node == self.destination
        
        self.current_node = next_node
        self.unvisited_neighbors = [neighbor for neighbor in self.graph.adj[next_node] if neighbor not in self.path] 
        
        if len(self.unvisited_neighbors) == 0:
            # Dead end
            self.unvisited_neighbors = list(self.graph.adj[self.current_node])
            self.action_space = gym.spaces.Discrete(len(self.unvisited_neighbors))
            # If we are at the destination, we are done
            if self.done:
                self.path.append(self.current_node)
                return self._get_observation(), 0, True, {}
            # If we are not at the destination
            return self._get_observation(), -10, False, {}

        self.action_space = gym.spaces.Discrete(len(self.unvisited_neighbors))
        
        return self._get_observation(), -1, self.done, {}
    
    def _get_observation(self):
        # obs = np.zeros((len(self.graph.nodes),), dtype=np.float32)
        # for node in self.path:
        #     obs[node] = 1
        # return obs
        return self.current_node
    
    def render(self):
        pass
        