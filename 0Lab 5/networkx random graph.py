import networkx as nx
import matplotlib.pyplot as plt


#the second variable is of probability
r = nx.gnp_random_graph(21,0.2)

nx.draw(r)








#dont include this

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

print(avg_cluster_coefficient(r))




#plot
def degree_histogram_directed(G, in_degree=False, out_degree=False):

    nodes = G.nodes()
    if in_degree:
        in_degree = dict(G.in_degree())
        degseq=[in_degree.get(k,0) for k in nodes]
    elif out_degree:
        out_degree = dict(G.out_degree())
        degseq=[out_degree.get(k,0) for k in nodes]
    else:
        degseq=[v for k, v in G.degree()]
    dmax=max(degseq)+1
    freq= [ 0 for d in range(dmax) ]
    for d in degseq:
        freq[d] += 1
    return freq

#degree_histogram_directed(r)


in_degree_freq = degree_histogram_directed(r)

degrees = range(len(in_degree_freq))
plt.figure(figsize=(12, 8)) 
plt.loglog(range(len(in_degree_freq)), in_degree_freq, 'go-', label='in-degree') 
plt.xlabel('Degree')
plt.ylabel('Frequency')

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()
    
plot_degree_dist(r)


        