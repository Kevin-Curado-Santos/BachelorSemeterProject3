import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from agent import QLearningAgent
from env import GraphEnvironment
from gen2 import generate_static_network, save_graph, load_graph

def get_graph(num_nodes, num_switches):
    if os.path.exists("graph.gpickle"):
        graph = load_graph("graph.gpickle")
    else:
        graph = generate_static_network(num_nodes, num_switches, max_switch_connections=3)
        save_graph(graph, "graph.gpickle")
        
    # save the graph to a png
    nx.draw(graph, with_labels=True)
    plt.savefig("graph.png")
    return graph

env = GraphEnvironment(get_graph(10, 10), 0, 1)

def train_agent(agent, num_episodes, muted=False):
    reward_list = []
    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0
    
        while True:
            action = agent.choose_action(state, env.action_space.n)
            next_state, reward, done, _ = env.step(action)
            agent.update_q_table(state, action, reward, next_state, env.action_space.n)
            state = next_state
            total_reward += reward
            if done:
                break
        if not muted:
            print("Episode {} with total reward {}".format(episode+1, total_reward))
        reward_list.append(total_reward)

def test_agent(agent, num_experiments, muted=False):
    shortest_path = nx.shortest_path(env.graph, env.source, env.destination)
    best_path_count = 0
    for _ in range(num_experiments):
        state = env.reset()
        path = [state]
        
        while True:
            action = agent.choose_action(state, env.action_space.n)
            next_state, reward, done, _ = env.step(action)
            state = next_state
            path.append(state)
            if done:
                break
        if not muted:
            print("Path: {}".format(path))
        if len(path) <= len(shortest_path):
            best_path_count += 1
    print("Best path count: {}".format(best_path_count))
    return best_path_count

if __name__ == "__main__":
    agent = QLearningAgent(env.observation_space.n, alpha=0.15, epsilon=0.2)
    train_agent(agent, 1000, True)
    num_experiments = 100
    count = test_agent(agent, num_experiments)
    print("Success rate: {}".format(count/num_experiments))
    