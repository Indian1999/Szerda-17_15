import numpy as np # pip install numpy (terminálba)

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
