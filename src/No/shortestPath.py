import sys

import No.generator as generator

# generate valid graph with nodes and switches, where nodes = arg1 and switches = arg2
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 shortestPath.py nodes switches source destination")
        exit(1)
    nodes = int(sys.argv[1])
    switches = int(sys.argv[2])
    source = int(sys.argv[3])
    destination = int(sys.argv[4])
    G, net = generator.generate_valid_graph(nodes, switches, source, destination)
    generator.draw_graph_shortest_path(G, net)
