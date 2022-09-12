import networkx as nx
import numpy as np
import pylab as plt
L=[(0,1,2),(0,2,1),(0,3,8),(1,3,6),(1,4,1),
   (2,3,7),(2,6,9),(3,4,5),(3,5,1),(3,6,2),
   (4,5,3),(4,7,9),(5,6,4),(5,7,9),(6,7,3)]

G = nx.Graph()
G.add_weighted_edges_from(L)
T = nx.minimum_spanning_tree(G, algorithm="kruskal")
c=nx.to_numpy_matrix(T)
print("c=", c)
w1 = c.sum()/2
print("tree weight:", w1)
pos = nx.circular_layout(G)
key=range(8); s=['v'+str(i) for i in key]
s = dict(zip(key, s))
nx.draw(T, pos, labels=s, font_weight='bold')
w2=nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=w2)
plt.show()
