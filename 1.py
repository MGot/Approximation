import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.approximation as naa

import random

n = 10 #number of nodes
G = nx.MultiGraph()

for i in range(0,n):
	G.add_node(i)
	for j in range(i,n):
		if i != j:
			G.add_edge(i,j,weight = random.randint(0,100))

tempMst = nx.minimum_spanning_tree(G)
T = nx.MultiGraph()

weights = nx.get_edge_attributes(tempMst, 'weight')

for i in tempMst.edges():
	T.add_edge(*i,weight=weights[i])

M = naa.min_maximal_matching(T)

for i in M:
	T.add_edge(*i,weight=weights[i])

E = nx.eulerian_circuit(T)

print ()
print ("G:", G.edges(data=True))
print ()
print ("T:", T.edges(data=True))
print ()
print ("M:", M)
print ()
print ("E:", E)

pos=nx.shell_layout(T)

edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in T.edges(data=True)])

nx.draw_networkx_edge_labels(T,pos,edge_labels=edge_labels)
nx.draw(T,pos, node_color = 'r',edge_size=50,width=5,font_size=18, 
	node_size=700,edge_color='b',edge_cmap=plt.cm.Reds,with_labels=True)

plt.show()