import networkx as nx
import matplotlib.pyplot as plt

#Kezdőállapot definiálása
start_node = (0,0,5)

# Egy üres irányított gráf létrehozása
G = nx.DiGraph()

# Ehez a gráfhoz, hozzá tudunk adni csúcsokat (Node) és éleket (Edge)

G.add_node(start_node)          # Done
G.add_node((2,0,3))             # Done
G.add_node((0,3,2))             # Done
G.add_edge((0,0,5), (2,0,3))
G.add_edge((0,0,5), (0,3,2))

G.add_node((0,2,3))             # Done
G.add_node((2,3,0))
G.add_edge((2,0,3), (0,2,3))
G.add_edge((2,0,3), (2,3,0))
G.add_edge((2,0,3), (0,0,5))

G.add_node((2,1,2))
G.add_edge((0,3,2), (0,0,5))
G.add_edge((0,3,2), (0,0,5))
G.add_edge((0,3,2), (2,3,0))
G.add_edge((0,3,2), (2,1,2))

G.add_node((2,2,1))
G.add_edge((0,2,3), (0,0,5))
G.add_edge((0,2,3), (2,0,3))
G.add_edge((0,2,3), (0,3,2))
G.add_edge((0,2,3), (2,2,1))

layout = nx.kamada_kawai_layout(G)
nx.draw(G, layout, with_labels = True, arrows = True)
plt.show()