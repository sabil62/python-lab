import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(1,2)
g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(1,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(1,6)

nx.draw(g,with_labels=1)
plt.show()
