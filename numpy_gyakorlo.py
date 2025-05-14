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
arr = np.linspace(3, 80, 100)
print(arr)