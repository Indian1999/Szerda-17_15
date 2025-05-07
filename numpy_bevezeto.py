import numpy as np # pip install numpy (terminálba)
import random
# A fő feature: numpy array - tömb adatszerkezet

tömb = np.array([1,2,3,4,5])
print(tömb)
print(type(tömb)) # <class 'numpy.ndarray'>

# tömb tulajdonságai: mérete, nem változtatható, (nem adhatunk hozzá elemet definiálás után)
# csakúgy mint a tuple adatszerkezetnél
# törölni se tudunk 

mátrix = np.array([[1,2,3], [4,5,6]])
print(mátrix)

print("A tömb dimenziója:", tömb.shape) # (5,)
print("A mátrix dimenziója:", mátrix.shape) # (2, 3)

zeros = np.zeros((5,8))
print(zeros)
ones = np.ones((3,3,2))
print(ones)
sevens = np.full((2, 5), 7)
print(sevens)

num = np.random.randint(1, 5)
print(num)

random_mátrix = [[random.randint(-100, 200) for j in range(4)] for i in range(5)]
print(random_mátrix)

print(np.random.randint(-100, 201, (2,3,5,6,7,2)))

range_array = np.arange(10, 100, 20)
print(range_array)

szamok = np.linspace(0, 1, 101)
print(szamok)

print(szamok[6])
print(szamok[2:10])

np_matrix = np.random.randint(1, 20, (8, 6))
np_matrix[2, 3] = -50
print(np_matrix[2, 3])
print(np_matrix[2][3])
print(np_matrix[5, :])

lista = [4, 2, 39 , 3]
lista2 = [2, 3, 11, 7]
print(lista)
print(lista + lista2)

x = np.array([3, 8, 2])
y = np.array([5, 2, 5])
print(x+y)
print(x * 5)
print(x ** 2)

mtx1 = np.array([[1,2], [3,4]])          #   n1 x m1   (2x2)
mtx2 = np.array([[5,1, 5, 6], [3,2,3,1]])#   n2 x m2   (2x4)

print(np.dot(mtx1, mtx2)) # m1 = n2
#print(np.dot(mtx2, mtx1))

print(mtx2)
print(mtx2.T) # sorból oszlopot, oszlopokból sort

print("Elemek összege:", mtx2.sum())
print("Elemek átlaga:", mtx2.mean())
print("Legnagyobb elem:", mtx2.max())
print("Legkisebb elem:", mtx2.min())
print("A legnagyobb elem indexe:",mtx2.argmax())

# mtx2.shape = (2,4)   # 0. eleme: sorok száma, 1. eleme: oszlopok száma
print("Oszlopösszeg:", mtx2.sum(axis=0))
print("Sorátlag:", mtx2.mean(axis=1))

print(mtx2.flatten())
print(mtx2.reshape((2,1,2,2)))