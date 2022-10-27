import network
import networkx as nx
import matplotlib.pyplot as plt
import random

# given an amount of nodes and swithes, generate a random graph
# each node can only be connected switches and switches can be connected to other switches and nodes 
def generate_graph(nodes, switches):
    net = network.network() # Create a network object
    
    for i in range(nodes):
        net.add_node(network.node("node" + str(i+1)))
    
    for i in range(switches):
        net.add_switch(network.switch("switch" + str(i+1), 2))
    
    # Create a graph with the nodes and switches
    G = nx.Graph()
    for node in net.node_list:
        G.add_node(node.get_name())
    for switch in net.switch_list:
        G.add_node(switch.get_name())
    
    # connect the switches such that they are all connected and sometimes more than one path is possible                  
    for i in range(switches):
        for j in range(switches):
            if i != j:
                if random.randint(0,1) == 1:
                    node1 = net.get_switch_list()[i]
                    node2 = net.get_switch_list()[j]
                    G.add_edge(node1.get_name(), node2.get_name())
                    net.add_link(network.link(node1, node2))

  
     # randomly connect the nodes and switches such that each node is connected to at least one switch and no node as more than one connection
    for node in net.node_list: 
        switch = net.switch_list[random.randint(0, len(net.switch_list)-1)]
        G.add_edge(node.get_name(), switch.get_name())
        net.add_link(network.link(node, switch))
    
  
    return G, net
    
G, net = generate_graph(10, 5)

link_list = [x.get_node1().get_name() + x.get_node2().get_name() for x in net.link_list]
print(link_list)
print(nx.is_connected(G))

nx.draw_networkx(G, with_labels=True)
plt.savefig("graph.png")