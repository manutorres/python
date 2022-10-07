numeros = [5, 2, 7, 1, 6]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

# Sorted es funcion que retorna otra lista
print("Sorted devuelve una nueva lista: ", sorted(numeros))
print(numeros)

# Reverse es metodo que modifica la lista original
numeros.reverse()
print(numeros)

# ********************************************************************


def ordenar_por_precio(item):
    return item[1]


items = [
    ("Producto 1", 400),
    ("Producto 3", 1000),
    ("Producto 2", 600)
]

# El argumento key determina la funcion de ordenamiento personalizada
items.sort(key=ordenar_por_precio)
print(items)

# Usando una funcion lambda. Mas claro y conciso
items.sort(key=lambda item: item[0], reverse=True)
print(items)
