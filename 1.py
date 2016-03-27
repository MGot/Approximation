import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.approximation as naa

import random

n = 5 #number of nodes
G = nx.Graph()

for i in range(0,n):
	G.add_node(i)
	for j in range(i,n):
		if i != j:
			G.add_edge(i,j,weight = random.randint(0,100))
nx.draw(G)

T = nx.minimum_spanning_tree(G)
M = naa.min_maximal_matching(T)
print ()
print (G.edges(data=True))
print ()
print (T.edges(data=True))
print ()
print (M)


plt.show()