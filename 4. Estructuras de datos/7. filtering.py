items = [
    ("Producto 1", 400),
    ("Producto 3", 1000),
    ("Producto 2", 600)
]

# Usando la funcion filter
# filter retorna un iterable que convertimos en list
mas_caros = list(filter(lambda item: item[1] > 500, items))
print(mas_caros)

# Usando map comprehension
mas_caros = [item for item in items if item[1] > 500]
print(mas_caros)
