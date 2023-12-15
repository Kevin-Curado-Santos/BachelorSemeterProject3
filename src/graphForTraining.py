import networkx as nx
import random
# You can visualize the graph using matplotlib
import matplotlib.pyplot as plt

def generate_graph(num_nodes, num_edges):
    """
    Generates a connected graph with num_nodes nodes and num_edges edges.

    Args:
    - num_nodes (int): The number of nodes in the graph.
    - num_edges (int): The number of edges in the graph.

    Returns:
    - G (networkx.Graph): The generated graph.
    """
    G = nx.connected_watts_strogatz_graph(num_nodes, 4, 0.2)

    # Add more random edges to increase density
    while G.number_of_edges() < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)

        # Ensure that the nodes are different and the edge doesn't already exist
        while node1 == node2 or G.has_edge(node1, node2):
            node1 = random.randint(0, num_nodes - 1)
            node2 = random.randint(0, num_nodes - 1)

        # Add the edge to the graph
        G.add_edge(node1, node2)
        
    nx.draw(G, with_labels=True)
    plt.savefig("graph.png")

    return G
