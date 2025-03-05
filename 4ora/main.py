import matplotlib.pyplot as plt # terminálba: pip install matplotlib
import numpy as np              # pip install numpy

# Input beolvasása:
map = []
with open("4ora/input.txt", "r", encoding="utf-8") as f:
   for line in f:
       map.append(list(line.strip())) 

# Score_map létrehozása alap értékekkel:
score_map = [["." for j in range(len(map[i]))] for i in range(len(map))]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "#":
            score_map[i][j] = -1
        if score_map[i][j] == ".":
            score_map[i][j] = float("inf")

# alt + bal click -> új kurzort hoz létre
def possible_moves(i,j):
    moves = []
    if i > 0 and (score_map[i-1][j] == "." or score_map[i-1][j] >= score_map[i][j] + 2):
        moves.append("up")
    if i < len(score_map) - 1 and (score_map[i+1][j] == "." or score_map[i+1][j] >= score_map[i][j] + 2):
        moves.append("down")
    if j < len(score_map[i]) - 1 and (score_map[i][j+1] == "." or score_map[i][j+1] >= score_map[i][j] + 2):
        moves.append("right")
    if j > 0 and (score_map[i][j-1] == "." or score_map[i][j-1] >= score_map[i][j] + 2):
        moves.append("left")
    return moves

def find_values(i,j):
    moves = possible_moves(i,j)
    if "up" in moves:
        score_map[i-1][j] = score_map[i][j] + 1
        find_values(i-1, j)
    if "down" in moves:
        score_map[i+1][j] = score_map[i][j] + 1
        find_values(i+1, j)
    if "right" in moves:
        score_map[i][j+1] = score_map[i][j] + 1
        find_values(i, j+1)
    if "left" in moves:
        score_map[i][j-1] = score_map[i][j] + 1
        find_values(i, j-1)

#Keressük meg a kijáratot:
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "E":
            score_map[i][j] = 0
            find_values(i,j)
            
labirint = [row[:] for row in score_map]
for i in range(len(labirint)):
    for j in range(len(labirint[i])):
        if labirint[i][j] == -1:
            labirint[i][j] = [0, 0, 0]
        else:
            labirint[i][j] = [(labirint[i][j] + 20) / 70, 0, 0]
plt.imshow(labirint)
plt.title("Labirinth heatmap")
plt.axis("off")
plt.savefig("4ora\images\heatmap.png")
plt.close()

path_matrix = np.zeros((len(map), len(map[0]), 3))
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "#":
            path_matrix[i, j] = [0,0,0]
        else:
            path_matrix[i, j] = [1,1,1]

plt.imshow(path_matrix)
plt.savefig("4ora\images\labirinth_map.png")   
plt.close()

def find_path(i,j):
    path_matrix[i,j] = [0,1,0]
    if score_map[i][j] != 0:
        if score_map[i][j+1] + 1 == score_map[i][j]:
            find_path(i, j+1)
        elif score_map[i][j-1] + 1 == score_map[i][j]:
            find_path(i, j-1)
        elif score_map[i+1][j] + 1 == score_map[i][j]:
            find_path(i+1, j)
        elif score_map[i-1][j] + 1 == score_map[i][j]:
            find_path(i-1, j)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            find_path(i,j)

plt.imshow(path_matrix)
plt.show()
            

    
