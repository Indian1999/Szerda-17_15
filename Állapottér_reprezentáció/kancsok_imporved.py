import networkx as nx
import matplotlib.pyplot as plt

# Az open listát sorként fogjuk kezelni (FIFO adatszerkezet)
# First in First out
# Csak a végére rakhatunk új elemet
# Csak az elejéről tudunk elemet kivenni

start_node = (0,0,5)
capacities = (2,3,5)

open = [(0,0,5)]
visited = [(0,0,5)]

G = nx.DiGraph() # Irányított gráf
G.add_node(start_node)

while len(open) > 0:
    current_node = open.pop(0) # 0. indexű elemet kivesszük
    for i in range(len(current_node)): # 0, 1, 2
        if current_node[i] != 0: # Üres kancsóból nem tudunk önteni
            for j in range(len(current_node)):
                if i != j:
                    amount = min(current_node[i], capacities[j] - current_node[j])
                    new_node = list(current_node)
                    new_node[i] -= amount
                    new_node[j] += amount
                    new_node = tuple(new_node)
                        
                    if new_node not in visited:
                        open.append(new_node)
                        visited.append(new_node)
                        G.add_node(new_node)
                        
                    if current_node != new_node:
                        G.add_edge(current_node, new_node)
                    
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()