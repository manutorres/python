numeros = [1, 1, 2, 3, 3, 4]

# No admite repetidos
unicos = set(numeros)
print(unicos)

# Operaciones de conjuntos
a = {"x", "y"}
b = {"w", "z", "x"}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

# Son una coleccion no ordenada
# No admite acceso por indice -> TypeError
# print(a[0])

# Comprehension
# [expresion] for item in iterable_de_items
valores = {x * 2 for x in [1, 2, 3]}
print(valores)


# Chequear si todos los valores son únicos
def todos_unicos(numeros):
    return len(numeros) == len(set(numeros))


numeros = [1, 2, 3]
print(f"Son los números {numeros} todos únicos? ", todos_unicos(numeros))
