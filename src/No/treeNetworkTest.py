import No.network as network
import networkx as nx
import matplotlib.pyplot as plt
import random

net = network.network() # Create a network object

# Create a tree topology
for i in range(8):
    net.add_node(network.node("n" + str(i+1)))

for i in range(1,4):
    net.add_switch(network.switch("s" + str(i)))

net.add_link(network.link("n1", "s1", random.randint(1,10)))
net.add_link(network.link("n2", "s1", random.randint(1,10)))
net.add_link(network.link("s1", "s2", random.randint(1,10)))
net.add_link(network.link("n3", "s2", random.randint(1,10)))
net.add_link(network.link("n4", "s2", random.randint(1,10)))
net.add_link(network.link("n5", "s2", random.randint(1,10)))
net.add_link(network.link("s1", "s3", random.randint(1,10)))
net.add_link(network.link("n6", "s3", random.randint(1,10)))
net.add_link(network.link("n7", "s3", random.randint(1,10)))
net.add_link(network.link("n8", "s3", random.randint(1,10)))

# Print the network
print(net)

# create a graph object
G = nx.Graph()

# add nodes to the graph
for node in net.node_list:
    G.add_node(node.get_name())
    
# add switches to the graph
for switch in net.switch_list:
    G.add_node(switch.get_name())

# add links to the graph
for link in net.link_list:
    G.add_edge(link.get_node1(), link.get_node2(), weight = link.get_weight())

# draw the graph
nx.draw(G, with_labels=True)
plt.show()