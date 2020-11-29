
#cis dataset

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#edges, nodes and cost
header = ["e","n","c"]
T = pd.read_csv("mammalia/cis-n4c6-b14.mtx",sep=" ", header = None, names=header)

Graph = nx.from_pandas_edgelist(T, "e", "n", ["c"])
nx.draw(Graph)
plt.show()

#for other tasks

#a)for no of edges and node
nodes = Graph.order()
edges = Graph.size()
print("The number of nodes is: ",nodes)
print("The number of edges is: ",edges)

#b) avaerage degree
degree = [val for (node, val) in Graph.degree()]
avg_degree = 0
for i in range(len(degree)):
    avg_degree = avg_degree + degree[i]
average_degree = avg_degree/len(degree)
print("The average degree is:  ",average_degree)

#c) density
total_node = Graph.order()
total_edges = Graph.size()
density = (2 * total_edges)/(total_node *(total_node - 1))
print("The density of graph is:",density)

# diameter

connected = nx.is_connected(Graph)
if (connected):
    print('The diameter of graph is: ',nx.diameter(Graph))
else:
    print("The graph is disconnected graph so diameter is infinite")


    
# e) clustering coefficient
def clusters(graph):
    cluster = []
    for node in graph.nodes():
        neighbour=[n for n in nx.neighbors(graph,node)]
        n_neighbors=len(neighbour)
        n_links=0
    
        if n_neighbors>1:
            for node1 in neighbour:
                for node2 in neighbour:
                    if graph.has_edge(node1,node2):
                        n_links+=1
            n_links/=2 #=n_links is done twice
            #formula 2.0 * E / (V *(V - 1))
            clustering_coeff=n_links/(0.5*n_neighbors*(n_neighbors-1))
            cluster.append(clustering_coeff)
           # print(clustering_coeff)
        else:     
            cluster.append(0)
        
        
    return cluster

def avg_cluster_coefficient(graph):
    cluster_coeff = clusters(graph)
    total_coeff = 0
    for i in cluster_coeff:
        total_coeff += i
    avg_coeff = total_coeff / len(cluster_coeff) 
    return avg_coeff   


print("The average clustering coeffiecient is: ",avg_cluster_coefficient(Graph))





def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()
    
plot_degree_dist(Graph)

