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

start_node = []
G.add_node(start_node)

open = [start_node]
visited = [start_node]

while len(open) > 0:
    current_node = open.pop(0)
    for i in range(1, n + 1):
        if i not in current_node:
            # Ezen a pontot tuti nincsenek ugyan abban a sorban/oszlopban
            new_node = current_node + [i]
            valid = is_valid(new_node)