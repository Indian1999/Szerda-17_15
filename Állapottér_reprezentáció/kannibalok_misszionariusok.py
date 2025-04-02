import networkx as nx
import mathplotplib.pyplot as plt

G = nx.DiGraph()

start_node = (3,3,1)
end_node = (0,0,0)

open_list = [start_node]
visited = [start_node]

while len(open_list) > 0:
    current_node = open_list.pop(0)
    if current_node[2] == 1: # A hajó a bal parton van
        if current_node[0] - 1 >= current_node[1]: # 1 misszionárius
            new_node = (current_node[0] - 1, current_node[1], 0)
            if new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            G.add_edge(current_node, new_node)
            
        if current_node[0] - 2 >= current_node[1]: # 2 misszionárius
            new_node = (current_node[0] - 2, current_node[1], 0)
            if new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            G.add_edge(current_node, new_node)
        
        if 3 - (current_node[1] - 1) <= 3 - current_node[0]: # 1 kannibál
            new_node = (current_node[0], current_node[1] - 1, 0)
            if new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            G.add_edge(current_node, new_node)
            
        if 3 - (current_node[1] - 2) <= 3 - current_node[0]: # 2 kannibál
            new_node = (current_node[0], current_node[1] - 2, 0)
            if new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            G.add_edge(current_node, new_node)
            
        if 3 - (current_node[0] - 1) >= 3 - (current_node[1] - 1): # 1 kannibál 1 misszionárius
            new_node = (current_node[0]-1, current_node[1] - 1, 0)
            if new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            G.add_edge(current_node, new_node)
    else:
        pass # jobb parton
        
    
