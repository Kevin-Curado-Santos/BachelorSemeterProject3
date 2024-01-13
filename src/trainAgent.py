from envDeadEnd import GraphEnvironment
from agent import QLearningAgent
import networkx as nx

def train(graph, source, destination, muted = False, num_episodes = 100, alpha = 0.15, epsilon = 0.0):
    # Assuming you have already defined and instantiated the GraphEnvironment
    env = GraphEnvironment(graph, source, destination)

    # Instantiate the Q-learning agent
    state_size = len(env.graph.nodes)
    action_size = env.action_space.n
    q_learning_agent = QLearningAgent(state_size, alpha=alpha, epsilon=epsilon)

    path_count = 0
    first_time = True
    first_time_eps = 0

    goal_reached_count = 0
    shortest_path = nx.shortest_path(graph, source, destination)

    for episode in range(num_episodes):
        # linearly decrease epsilon
        q_learning_agent.epsilon -= 1/num_episodes
        if q_learning_agent.epsilon < 0:
            q_learning_agent.epsilon = 0
        state = env.reset()
        total_reward = 0
        state_size = len(env.graph.nodes)
        action_size = env.action_space.n
        
        while True:
            action = q_learning_agent.choose_action(state, action_size)
            next_state, reward, done, _ = env.step(action)
            action_size = env.action_space.n
            q_learning_agent.update_q_table(state, action, reward, next_state, action_size)
            
            state = next_state
            total_reward += reward
            
            if done:
                if state == destination:
                    goal_reached_count += 1
                break
        if env.path == shortest_path:
            path_count += 1
            if first_time:
                first_time = False
                first_time_eps = episode+1
        if not muted:
            print(f"Epsilon: {q_learning_agent.epsilon}")
            print(f"Episode: {episode + 1}, Total Reward: {total_reward}")
            print(f"Path: {env.path}\n")
                
    print(f"Path count: {path_count}")
    print(f"Ratio: {path_count/num_episodes}")
    print(f"First time goal reached: {first_time_eps}")