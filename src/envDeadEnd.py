import gymnasium as gym
# import numpy as np
# import networkx as nx

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
        
        # self.unvisited_neighbors = list(self.graph.adj[self.current_node])
        self.adjacent_nodes = list(self.graph.adj[self.current_node])
        self.action_space = gym.spaces.Discrete(len(self.adjacent_nodes))
        
        
    def reset(self):
        self.current_node = self.source
        self.done = False
        self.path = []
        
        self.adjacent_nodes = list(self.graph.adj[self.current_node])
        self.action_space = gym.spaces.Discrete(len(self.adjacent_nodes))
        return self._get_observation()
    
    def step(self, action):
        self.path.append(self.current_node)
        next_node = self.adjacent_nodes[action]
        self.done = (next_node == self.destination)

        self.current_node = next_node
        # self.unvisited_neighbors = [neighbor for neighbor in self.graph.adj[next_node] if neighbor not in self.path] 
        
        self.adjacent_nodes = list(self.graph.adj[self.current_node])
        if len(self.adjacent_nodes) == 1:
            # Dead end
            # If we are at the destination, we are done
            self.path.append(self.current_node)
            if self.done:
                return self._get_observation(), 0, True, {}
            
            # If we are not at the destination
            return self._get_observation(), -2, True, {}

        self.action_space = gym.spaces.Discrete(len(self.adjacent_nodes))
        
        return self._get_observation(), -1, self.done, {}
    
    def _get_observation(self):
        # obs = np.zeros((len(self.graph.nodes),), dtype=np.float32)
        # for node in self.path:
        #     obs[node] = 1
        # return obs
        return self.current_node
    
    def render(self):
        pass
        