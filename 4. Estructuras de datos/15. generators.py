from sys import getsizeof

# Son iterables que generan un nuevo valor en cada iteracion
# Evitan almacenar todos los valores en memoria de una vez

valores = (x * 2 for x in range(10))
print(valores)
for abc1 in valores:
    print(abc1)


# Analizando el tamaño de un generador
print("Tamaño en bytes:", getsizeof(valores))

valores = (x * 2 for x in range(100000))
print("Tamaño en bytes:", getsizeof(valores))

# Comparacion con el tamaño de una lista
valores = [x * 2 for x in range(100000)]
print("Tamaño en bytes:", getsizeof(valores))

print()


# Definiendo un generador con la sentencia YIELD
def abecedario():
    letras = "abcdefghijklmnopqrstuvwxyz"
    for l in letras:
        yield l  # Retorna una letra en cada llamado a next()


abc1 = abecedario()
abc1.__next__()
abc1.__next__()
print(abc1.__next__())
print()

abc2 = abecedario()
for l in abc2:
    print(l)

# StepIteration error
print(abc2.__next__())
