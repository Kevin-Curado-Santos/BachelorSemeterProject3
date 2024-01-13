import No.network as network
import networkx as nx
import matplotlib.pyplot as plt
import random

# given an amount of nodes and swithes, generate a random graph
# each node can only be connected switches and switches can be connected to other switches and nodes 
def generate_graph(nodes, switches, source, destination):
    net = network.network() # Create a network object
    
    for i in range(nodes):
        net.add_node(network.node("node" + str(i+1)))
    
    for i in range(switches):
        net.add_switch(network.switch("switch" + str(i+1)))
    
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
                    #weight = random.randint(1,10)
                    G.add_edge(node1.get_name(), node2.get_name())
                    net.add_link(network.link(node1, node2))

  
     # randomly connect the nodes and switches such that each node is connected to at least one switch and no node as more than one connection
    for node in net.node_list: 
        switch = net.switch_list[random.randint(0, len(net.switch_list)-1)]
        #weight = random.randint(1,10)
        G.add_edge(node.get_name(), switch.get_name())
        net.add_link(network.link(node, switch))
            
    # set the source and destination
    net.get_node_list()[source-1].set_source()
    net.get_node_list()[destination-1].set_destination()
  
    return G, net

def generate_valid_graph(nodes, switches, source, destination):
    while True:
        G, net = generate_graph(nodes, switches, source, destination)
        if nx.is_connected(G):
            break
    return G, net

# # given a graph and a network, draw the graph
# def draw_graph(G, net):
#     pos = nx.spring_layout(G)
#     nx.draw_networkx_nodes(G, pos, nodelist = [node.get_name() for node in net.node_list], node_color = "blue")
#     nx.draw_networkx_nodes(G, pos, nodelist = [switch.get_name() for switch in net.switch_list], node_color = "red")
#     nx.draw_networkx_edges(G, pos)
#     nx.draw_networkx_labels(G, pos)
#     plt.show()
    
# given a graph and a network, draw the graph with the shortest path
def draw_graph_shortest_path(G, net):
    source = [node.get_name() for node in net.node_list if node.isSource][0]
    target = [node.get_name() for node in net.node_list if node.isDestination][0]
    weight = nx.shortest_path_length(G, source, target)
    # shortest path from source to target with weights using Dijkstra's algorithm
    shortest_path = nx.shortest_path(G, source, target, weight, method = "dijkstra")
    print(shortest_path)
    print([x.get_node1().get_name() +' '+ x.get_node2().get_name() for x in net.link_list])
    pos = nx.spring_layout(G)
    # draw the nodes with blue color and a circle shape 
    nx.draw_networkx_nodes(G, pos, nodelist = [node.get_name() for node in net.node_list], node_color = "blue")
    # draw the switches with orange color and a square shape and a label displaying the number of the switch
    nx.draw_networkx_nodes(G, pos, nodelist = [switch.get_name() for switch in net.switch_list], node_color = "orange", node_shape = "s")
    # draw edges with the different widths depending on the weight
    nx.draw_networkx_edges(G, pos, width = [(G[u][v]['weight'])/5 for u,v in G.edges()])
    #print([G[u][v] for u,v in G.edges()])
    # draw the shortest path with color green and width depending on the weight of the edges
    nx.draw_networkx_edges(G, pos, edgelist = [(u,v) for u,v in G.edges() if u in shortest_path and v in shortest_path], edge_color = "green", width = [(G[u][v]['weight'])/5 for u,v in G.edges() if u in shortest_path and v in shortest_path])
    nx.draw_networkx_labels(G, pos)
    plt.show()
    

# test the generator
if __name__ == "__main__":
    G, net = generate_valid_graph(100, 20, 1, 2)
    draw_graph_shortest_path(G, net)
