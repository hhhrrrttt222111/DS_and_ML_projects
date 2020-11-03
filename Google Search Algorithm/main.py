import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


DG = nx.DiGraph()
DG.add_nodes_from("ABCD")
nx.draw(DG, with_labels=True)
plt.show()

pr = nx.pagerank(DG, alpha=0.85)
print(pr)

DG.add_weighted_edges_from([("A", "B", 1), ("B", "C", 1), ("C", "D", 1), ("D", "A", 1)])
nx.draw(DG, with_labels=True)
plt.show()

G = nx.fast_gnp_random_graph(10,0.5,directed=True)
nx.draw(G, with_labels=True)
plt.show()

pr = nx.pagerank(G, alpha=0.85)
rank = np.array([[*pr.values()]])
best = np.argmax(rank)
print("The most popular website is {}".format(best))