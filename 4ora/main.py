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

# alt + bal click -> új kurzort hoz létre
def possible_moves(i,j):
    moves = []
    if i > 0 and (score_map[i-1][j] == "." or int(score_map[i-1][j]) >= int(score_map[i][j]) + 2):
        moves.append("up")
    if i < len(score_map) - 1 and (score_map[i+1][j] == "." or int(score_map[i+1][j]) >= int(score_map[i][j]) + 2):
        moves.append("down")
    if j < len(score_map[i]) - 1 and (score_map[i][j+1] == "." or int(score_map[i][j+1]) >= int(score_map[i][j]) + 2):
        moves.append("right")
    if j > 0 and (score_map[i][j-1] == "." or int(score_map[i][j-1]) >= int(score_map[i][j]) + 2):
        moves.append("left")
    return moves

def find_values(i,j):
    moves = possible_moves(i,j)
    print(moves)

#Keressük meg a kijáratot:
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "E":
            score_map[i][j] = 0
            find_values(i,j)