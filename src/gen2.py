import networkx as nx
import random
import matplotlib.pyplot as plt
import pickle

def generate_static_network(num_nodes, num_switches, max_switch_connections):
    G = nx.Graph()

    # Add nodes
    node_list = [i for i in range(num_nodes)]
    node_list_len = len(node_list)
    switch_list = [i + node_list_len  for i in range(num_switches)]

    G.add_nodes_from(node_list, node_type='node')
    G.add_nodes_from(switch_list, node_type='switch')

    # Connect nodes to switches
    for node in node_list:
        switch = random.choice(switch_list)
        G.add_edge(node, switch)

    # Connect switches to switches
    for switch in switch_list:
        num_connections = random.randint(1, max_switch_connections)
        other_switches = list(set(switch_list) - {switch})
        other_switches = random.sample(other_switches, min(num_connections, len(other_switches)))
        for other_switch in other_switches:
            G.add_edge(switch, other_switch)

    return G


# save the graph into a loadable format
def save_graph(G, filename):
    with open(filename, 'wb') as f:
        pickle.dump(G, f)
    
# load the graph from a loadable format
def load_graph(filename):
    with open(filename, 'rb') as f:
        G = pickle.load(f)
    return G