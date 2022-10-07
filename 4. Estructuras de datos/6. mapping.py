items = [
    ("Producto 1", 400),
    ("Producto 3", 1000),
    ("Producto 2", 600)
]

precios = []
for item in items:
    precios.append(item[1])

print(precios)

# Usando la funcion map
# map retorna un iterable que convertimos en list
precios = list(map(lambda item: item[1], items))
print(precios)

# Usando map comprehension
precios = [item[1] for item in items]
print(precios)
