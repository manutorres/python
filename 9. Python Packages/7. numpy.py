import numpy as np

array = np.array([1, 2, 3])
print(array)
print(type(array))
print()

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(array.shape)
print()

array = np.zeros((3, 4), dtype=int)
print(array)
array = np.ones((2, 6), dtype=int)
print(array)
array = np.full((3, 3), 5, dtype=int)
print(array)
array = np.random.random((3, 3))
print(array)
print()

print(array[1, 2])
print(array > 0.5)
print(array[array > 0.5])
print(np.sum(array))
print(np.round(array))
print()

primero = np.array([1, 2, 3])
segundo = np.array([1, 2, 3])
print(primero + 3)
print(primero * segundo)
print()

# NumPy vs Python para realizar una conversion de medidas
pulgadas = np.array([1, 2, 3])
# NumPy
centimetros = pulgadas * 2.55
# List comprehension
centimetros = [x * 2.55 for x in pulgadas]
print(centimetros)
print()

# Reemplazo de valores en matriz
matriz = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)
nueva_columna = [20, 10, 30]

# Borrar la segunda columa de matriz
matriz = np.delete(matriz, 1, axis=1)
print(matriz)
print()
matriz = np.insert(matriz, 1, values=nueva_columna, axis=1)
print(matriz)
print()

# Ordenar por valores de fila o columna
matriz = np.sort(matriz, axis=1)
print(matriz)
print()

# Invertir el arreglo
arreglo = np.array([3, 2, 1])[::-1]
print(arreglo)
