import No.network as network
import networkx as nx
import matplotlib.pyplot as plt

net = network.network() # Create a network object

# Create a star topology
net.add_node(network.node("n1")) 
net.add_node(network.node("n2"))
net.add_node(network.node("n3"))
net.add_node(network.node("n4"))
net.add_node(network.node("n5"))

net.add_switch(network.switch("s1", 5))

net.add_link(network.link("n1", "s1"))
net.add_link(network.link("n2", "s1"))
net.add_link(network.link("n3", "s1"))
net.add_link(network.link("n4", "s1"))
net.add_link(network.link("n5", "s1"))

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
    G.add_edge(link.get_node1(), link.get_node2())

# draw the graph
nx.draw_networkx(G, with_labels=True)
plt.show()
