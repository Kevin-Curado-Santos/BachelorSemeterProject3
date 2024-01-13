import matplotlib.pyplot as plt
from gen2 import load_graph
import networkx as nx
import os 

for filename in os.listdir("networks"):
    if filename.endswith(".pkl"):
        G = load_graph("networks/" + filename)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.savefig("networks/" + filename[:-4] + ".png")
        continue
    else:
        continue