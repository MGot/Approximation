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

T = nx.minimum_spanning_tree(G)
M = naa.min_maximal_matching(T)

for i in M:
	T.add_edge(*i)

E = nx.eulerian_circuit(T)

print ()
print (G.edges(data=True))
print ()
print (T.edges(data=True))
print ()
print (M)
print ()
print (E)

nx.draw(T, pos=None, arrows=True, with_labels=True)
plt.show()