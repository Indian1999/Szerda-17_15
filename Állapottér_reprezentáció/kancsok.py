import networkx as nx
import matplotlib.pyplot as plt

#Kezdőállapot definiálása
start_node = (0,0,5)

# Egy üres irányított gráf létrehozása
G = nx.DiGraph()

# Ehez a gráfhoz, hozzá tudunk adni csúcsokat (Node) és éleket (Edge)