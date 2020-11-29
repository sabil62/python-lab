import networkx as nx

c = nx.complete_graph(1200)

nx.draw(c,with_labels=1)

#this is for the non graph section or terminal section
print('The total no of edges is ',c.size())
print('The total no of nodes is ',c.order())

#total edges
#print('The total edges are:',c.edges())

print("the diameter is",nx.diameter(c))



