import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.approximation as naa

import random
import sys
import math
import datetime
import os.path

bf_count = 0
min_weight = math.inf
min_cycle = []

def print_cycle():
	for i in min_cycle[:-1]:
		print(str(i)+"->", end="")
	print(str(min_cycle[-1]))

def brude_force(G, nodes=[], weight=0):
	global bf_count
	global min_weight
	global min_cycle
	if len(nodes)==len(G.nodes()):
		edge_weight = G[nodes[-1]][nodes[0]][0]['weight']
		weight = edge_weight + weight
		bf_count = bf_count + 1
		if min_weight > weight:
			min_weight = weight
			min_cycle = nodes + [nodes[0]]
		return weight
	for n in list(set(G.nodes())-set(nodes)):
		if len(nodes)==0:
			brude_force(G, nodes + [n], 0)
		else:
			edge_weight = G[nodes[-1]][n][0]['weight']
			brude_force(G, nodes + [n], weight+edge_weight)

def aprox_tcp_weight(E,G):
	weight = 0
	for e in E:
		weight += G[e[0]][e[1]][0]['weight']
	return weight

def aprox_tcp(G, prints=False, draw=False, time=False):
	if time:
		start = datetime.datetime.now()

	tmpMst = nx.minimum_spanning_tree(G)
	T = nx.MultiGraph()

	weights = nx.get_edge_attributes(G, 'weight')
	weightsMST = nx.get_edge_attributes(tmpMst, 'weight')

	for i in tmpMst.edges():
		T.add_edge(*i,weight=weightsMST[i])

	nodesT = list() # lista wierzchołków o nieparzystego stopnia
	degrees = nx.degree(T)
	for key in degrees.keys():
	    if degrees[key] % 2 != 0:
	        nodesT.append(key)

	tmpM = nx.MultiGraph()
	for i in nodesT:
	    for j in nodesT:
	        if i < j: # bierzemy krawędź tylko raz
	            tmpM.add_edge(i, j, weight = G[i][j][0]['weight'])

	M = naa.min_maximal_matching(tmpM)

	for e in M:
		T.add_edge(*e, weight = weights[e + (0,)])

	E1 = nx.is_eulerian(T)
	if E1:
		E = list(nx.eulerian_circuit(T))
		H = list()
		for e in E:
			if e[0] not in H:
				H.append(e)

	if time:
		end = datetime.datetime.now()
		print(end-start)

	if prints:
		print ()
		print ("G:", G.edges(data=True))
		print ()
		print ("MST:", tmpMst.edges(data=True))
		print ()
		print ("M:", M)
		print ()
		print ("T:", T.edges(data=True))
		print ()
		print ("E1:", E1)
		if E1:
			print ()
			print ("E:", E)
			print ()
			print ("H:", H)

	if draw:
		edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
		pos=nx.shell_layout(G)
		nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
		#caly graf (czerwone krawedzie)
		nx.draw(G,pos, node_color = 'r',edge_size=50,width=6,font_size=18, 
			node_size=700,edge_color='r',edge_cmap=plt.cm.Reds,with_labels=True)
		pos=nx.shell_layout(T)
		pos=nx.shell_layout(tmpMst)
		#MST (zolte)
		nx.draw(tmpMst,pos, node_color = 'r',edge_size=50,width=4,font_size=18, 
			node_size=700,edge_color='y',edge_cmap=plt.cm.Reds,with_labels=False)
		#T (niebieskie)
		nx.draw(T,pos, node_color = 'r',edge_size=50,width=2,font_size=18, 
			node_size=700,edge_color='b',edge_cmap=plt.cm.Reds,with_labels=False)
		if not os.path.exists("figures/"):
			os.makedirs("figures/")
		plt.savefig("figures/"+str(datetime.datetime.now()).replace(":","-")+".png")
		plt.clf()

	return H, aprox_tcp_weight(H,G)

def print_aprox_cycle(E):
	for i in E:
		print(str(i[0])+"->",end="")
	print(E[0][0])


def calc(G, draw=True, time=False):
	global bf_count
	global min_weight
	global min_cycle
	E, w = aprox_tcp(G, draw=draw, time=time)
	print("aprox")
	print_aprox_cycle(E)
	print(w)
	if not time:
		brude_force(G)
		print("brude force("+str(bf_count)+"):")
		print_cycle()
		print(min_weight)
		print(w/min_weight)
		bf_count = 0
		min_weight = math.inf
		min_cycle = []
	

if len(sys.argv)==1:
	print("Write arguments [1 <number of nodes>] to create random n-nodes graph (time test)")
	print("Write arguments [2] to create random 2 to 7-nodes graphs (aproximation test)")
	exit()
elif sys.argv[1] == "1":
	if int(sys.argv[2])>1:
		n = int(sys.argv[2]) #number of nodes
		G = nx.MultiGraph()
		for i in range(0,n):
			for j in range(i,n):
				if i != j:
					G.add_edge(i,j,weight = random.randint(0,100))
		calc(G, draw=False, time=True)
	else:
		print("Should be n > 1")
		exit()
elif sys.argv[1] == "2":
	for n in range(2,8):
		G = nx.MultiGraph()
		for i in range(0,n):
			for j in range(i,n):
				if i != j:
					G.add_edge(i,j,weight = random.randint(0,100))
		print(str(n))
		print(G.edges(data=True))
		calc(G)
		print()




