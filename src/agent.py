import numpy as np

class QLearningAgent:
    def __init__(self, state_size, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.state_size = state_size
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        
        # Initialize the Q-table as a dictionary of arrays with states as keys and actions and rewards as values
        self.q_table = {}
        for i in range(state_size):
            self.q_table[str(i)] = None
        
    def choose_action(self, state, action_size):
        state = str(state)
        #if state not in self.q_table:
        self.q_table[state] = np.zeros(action_size)
        if np.random.random() < self.epsilon:
            return np.random.choice(action_size)
        else: 
            # get the action with the highest q-value 
            return np.argmax(self.q_table[state])
        
    def update_q_table(self, state, action, reward, next_state, action_size):
        state, next_state = str(state), str(next_state)
        #if next_state not in self.q_table:
        self.q_table[next_state] = np.zeros(action_size)
            
        old_q_value = self.q_table[state][action]
        max_future_q_value = np.max(self.q_table[next_state])
        new_q_value = (1-self.alpha)*old_q_value+self.alpha*(reward+self.gamma*max_future_q_value)
        self.q_table[state][action] = new_q_value
        
        
