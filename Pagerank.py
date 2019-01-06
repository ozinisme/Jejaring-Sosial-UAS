import networkx as nx 
import matplotlib.pyplot as plt 

def main():
	G = nx.read_edgelist('p2p-Gnutella06.txt', create_using=nx.DiGraph())

	deg = dict(G.in_degree())  #Returns a dictionay, with key as nodes and indegrees as values.
	pr = nx.pagerank(G)
	pr_values = []
	for i in deg.keys():
		pr_values.append(pr[i])

	plt.plot(deg.values(), pr_values, 'ro', markersize = 3)
	plt.xlabel('Indegree value of the nodes')
	plt.ylabel('PageRank value of the nodes')
plt.show()
main()
