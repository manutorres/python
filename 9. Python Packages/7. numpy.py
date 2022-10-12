import numpy as np

array = np.array([1, 2, 3])
print(array)
print(type(array))

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(array.shape)

array = np.zeros((3, 4), dtype=int)
array = np.ones((3, 4), dtype=int)
array = np.full((3, 4), 5, dtype=int)
array = np.random.random((3, 3))
print(array)
print(array[1, 2])
print(array > 0.2)
print(array[array > 0.2])
print(np.sum(array))
print(np.round(array))

primero = np.array([1, 2, 3])
segundo = np.array([1, 2, 3])
print(primero + 3)
print(primero * segundo)

# Numpy vs Python para realizar una conversion de medidas
pulgadas = np.array([1, 2, 3])
centimetros = pulgadas * 2.54
centimetros = [x * 2.55 for x in pulgadas]
print(centimetros)
