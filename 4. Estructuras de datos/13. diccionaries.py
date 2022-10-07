punto_a = {"x": 1, "y": 2}
punto_b = dict(x=3, y=4)

print(punto_a, punto_b)

print(punto_a["x"])
punto_a["x"] = 5
punto_a["z"] = 6
print(punto_a)

# Funcion get para evitar que el acceso no de error
# -1 como argumento en caso de no encontrar el indice
print(punto_a.get("a", -1))

# Eliminar una key
del punto_b["y"]
print(punto_b)

# Formas de iterar
for key in punto_a:
    print(key, punto_a[key])

# items() retorna una tupla que luego es desempaquetada
for key, valor in punto_a.items():
    print(key, valor)

# Comprehension
# [expresion] for item in iterable_de_items
valores = {x: x * 2 for x in range(5)}
print(valores)

# Unpacking
primero = {"Nombre": "Juan", "DNI": 123}
segundo = {"Apellido": "Perez", "Edad": 30}
datos = {**primero, **segundo}
print(datos)
