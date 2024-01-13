from train import train
from gen2 import load_graph
from testAgent import test
import env, envDeadEnd
import agent
import os

networks = [file for file in os.listdir("networks") if file.endswith(".pkl")]

for network in networks:   
    print(f"{network}\n")  
    graph = load_graph(f"networks/{network}")
    print("Training agent in Environment dealing with dead ends")
    env1 = envDeadEnd.GraphEnvironment(graph, 0, 9) 
    agent1 = agent.QLearningAgent(len(env1.graph.nodes), alpha=0.15, epsilon=1.0)
    train(graph, 0, 9, env1, agent1, muted=True, num_episodes=1000)
    print("\nTraining agent in Environment with backtracking")
    env2 = env.GraphEnvironment(graph, 0, 9)
    agent2 = agent.QLearningAgent(len(env2.graph.nodes), alpha=0.15, epsilon=1.0)
    train(graph, 0, 9, env2, agent2, muted=True, num_episodes=1000)

    print("\nTesting agent in Environment dealing with dead ends")
    test(graph, 0, 9, env1, agent1)
    print("\nTesting agent in Environment with backtracking")
    test(graph, 0, 9, env2, agent2)