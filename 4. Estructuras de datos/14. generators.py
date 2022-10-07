from sys import getsizeof

# Son iterables que generan un nuevo valor en cada iteracion
# Evitan almacenar todos los valores en memoria de una vez

valores = (x * 2 for x in range(10))
print(valores)
for x in valores:
    print(x)


# Analizando el tamaño de un generador
print("Tamaño en bytes:", getsizeof(valores))

valores = (x * 2 for x in range(100000))
print("Tamaño en bytes:", getsizeof(valores))

# Comparacion con el tamaño de una lista
valores = [x * 2 for x in range(100000)]
print("Tamaño en bytes:", getsizeof(valores))
