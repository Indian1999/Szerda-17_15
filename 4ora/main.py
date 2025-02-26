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
            score_map[i][j] = "#"


def find_values(i,j):
    pass

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "E":
            find_values(i,j)