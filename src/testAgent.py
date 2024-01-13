import networkx as nx

def test(graph, source, destination, env, q_learning_agent, max_steps = 1000):

    state = env.reset()
    while True:
        action = q_learning_agent.choose_action_without_randomness(state)
        state, reward, done, info = env.step(action)

        max_steps -= 1
        
        if done:
            break
        if max_steps == 0:
            print("Max steps reached")
            break
        
    print(f"Path: {env.path}\n")
    print(f"Algorithm path: {nx.shortest_path(graph, source, destination)}\n")