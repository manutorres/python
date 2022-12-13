lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

# zip toma iterables y retorna un iterable
zipped = zip(lista1, lista2, "xyz")
print(list(zipped))

# List comprehension a partir de iterar sobre ambas listas a la vez
combinado = [(str(a) + b) for (a, b) in zip(lista1, lista2)]
print(combinado)
