import numpy as np

# 1. feladat: 0-tól 9-ig a számok egy np tömbben
arr = np.arange(10)
print(arr)

# 2. feladat: 3x3-as mátrix tele 0-kal
arr = np.zeros((3,3))
print(arr)

# 3. feladat: 5x2x4-es mátrix tele 8-asokkal
arr = np.full((5,2,4), 8)
print(arr)

# 4. feladat: 5x6-os mátrix tele 1-15 közötti random számokkal
arr = np.random.randint(1, 16, (5,6))
print(arr)
# 5. feladat: Egy tömb, minden második elemehéze adjunk hozzá 10-et
arr = np.array([4,2,3,6,7,6,4,3,4,2,2,4,3,2,1])
arr[1::2] += 10
print(arr)

# 6. feladat: A kapott tömböt fordítsuk meg
arr = arr[::-1]
print(arr)
# 7. feladat: Határozzuk meg, a tömb elemeinek, összegét, átlagát, mediánját
print("Összeg:", arr.sum())
print("Átlag:", arr.mean())
print("Medián:", np.median(arr))
print("Szórás:", round(arr.std(),2)) # Standard Deviation (Szórás)
print("Legnagyobb elem indexe:", arr.argmax())

# 8. feladat: Hozzunk létre egy tömböt, ami 100 elemet tartalmaz, a legkisebb 3, 
# a legnagyobb 80, legyen növekvő sorrendben, egyenletesen elosztva a számokat
arr = np.linspace(1, 100, 100)
print(arr)

# 9. feladat: csináljuk ebből a tömbböl egy 10x5x2-es mátrixot
# Ahoz hogy ez megcsinálható legyen 10x5x2 = 100
arr = arr.reshape((10,5,2))
print(arr)
print(arr.shape)

# 10. feladat: Csináljunk ebből egy 5x5x2x2-es mátrixot
# AKkor végezhető el ez az átalakítás, ha 5x5x2x2 = 10x5x2
arr = arr.reshape((5,5,2,2))
print(arr.shape)

# 11. feladat: Generáljunk egy 20 elemű random tömböt (1-99)
tomb = np.random.randint(1, 100, 20)
print(tomb)

# 12. feladat: Határozzuk meg, hogy hány szám van a tömbben ami az átlagnál nagyobb
print(tomb.mean())
print("Az átlagtól nagyobb számok száma:", np.sum(tomb > tomb.mean()))

# 13. feladat: a 7-tel osztható számokat cseréljük ki -1 -re
tomb[tomb % 7 == 0] = -1
print(tomb)

# 14. feladat: Hozzunk létre egy aknamezőt:
# Legyen egy 10x10 mátrixunk, tele 0-val (üres mezőt)
# És helyezzünk el 10 darab aknát (1) erre a mátrixra
matrix = np.zeros((10,10))
aknák = np.random.choice(100, 10, replace=False) # 0-99 számokból kiválasztunk 10-et (ismétlés nélkül)
matrix[np.unravel_index(aknák, (10,10))] = 1
print(matrix)

# 15. feladat: Determináns (n x n)-es mátrixokra
matrix = np.random.randint(1, 10, (8,8))
print(matrix)
print(np.linalg.det(matrix))

# 16. feladat: generáljunk le 100 pontot a koordináta rendszerben.
# Mekkora ezeknek az átlagos távolsága az origótól?
x = np.random.randint(-100, 101, 100)
y = np.random.randint(-100, 101, 100)
distances = np.sqrt(x**2 + y**2)
print(distances.mean())

# 17. feladat: csináljunk egy 100 elemű listát amiben random gyömülcsök vannak
fruits = np.random.choice(["alma", "banán", "citrom", "dinnye", "málna", "szeder", "körte"], 100)
print(fruits)

# 18. feladat: Generáljunk le egy aknakeresű táblát!
minesweaper = np.zeros((10,10))
mines = np.random.choice(100, 10, replace=False) # 0-99 számokból kiválasztunk 10-et (ismétlés nélkül)
mine_coords = np.unravel_index(mines, (10,10))
minesweaper[mine_coords] = -1

# [1, 2, 3]    -> *mine_coords -> 1, 2, 3           zip -> [(1,1), (2,1), (3,2)]
# [1, 1, 2]                    -> 1, 1, 2

for x, y in zip(*mine_coords):
    for i in range(max(0, x-1), min(x+2, minesweaper.shape[0])):
        for j in range(max(0, y-1), min(y+2, minesweaper.shape[1])):
            if minesweaper[i][j] != -1:
                minesweaper[i][j] += 1

print(minesweaper)
            