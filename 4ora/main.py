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
            
for row in score_map:
    print(row)