import networkx as nx
import matplotlib.pyplot as plt
import math

def is_valid(node):
    last_index = len(node) - 1
    for i in range(0, last_index):
        if math.fabs(node[i] - node[last_index]) == math.fabs(i - last_index):
            return False
    return True        

n = 8
G = nx.Graph()

start_node = tuple()
G.add_node(start_node)

open_list = [start_node]
visited = [start_node]

end_nodes = []

while len(open_list) > 0:
    current_node = open_list.pop(0)
    
    if len(current_node) == n:
        end_nodes.append(current_node)
    else:
        for i in range(1, n + 1):
            if i not in current_node:
                # Ezen a pontot tuti nincsenek ugyan abban a sorban/oszlopban
                new_node = tuple(list(current_node) + [i])
                valid = is_valid(new_node)
                if valid:
                    G.add_node(new_node)
                    G.add_edge(current_node, new_node)
                    open_list.append(new_node)
    
                    
#layout = nx.spring_layout(G)
#nx.draw(G, layout, with_labels=True)
#plt.show()

with open(f"{n}_queen_results.txt", "w", encoding = "utf-8") as f:
    f.write(str(len(end_nodes)))
    f.write("\n")
    for node in end_nodes:
        f.write(str(node))
        f.write("\n")