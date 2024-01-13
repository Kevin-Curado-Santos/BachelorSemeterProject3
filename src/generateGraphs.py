from gen2 import generate_static_network, save_graph
import networkx as nx
import matplotlib.pyplot as plt

number_of_nodes = 10
number_of_switches = 2
max_switch_connections = 10
G = generate_static_network(number_of_nodes, number_of_switches, max_switch_connections)
save_graph(G, 'networks/graph_{}_{}_{}.pkl'.format(number_of_nodes, number_of_switches, max_switch_connections))
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig('networks/graph_{}_{}_{}.png'.format(number_of_nodes, number_of_switches, max_switch_connections))