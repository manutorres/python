lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

# zip toma iterables y retorna un iterable
zipped = zip(lista1, lista2, "xyz")
print(list(zipped))
