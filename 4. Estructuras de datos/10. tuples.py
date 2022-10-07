punto_a = (1, 2)
punto_b = 3, 4

print(type(punto_b))

tupla_vacia = ()

tupla = ("a", "b") * 3
print(tupla)

# Acceso a valores
print(tupla[1])
print(tupla[0:4])

# Unpacking
x, y = punto_a
print("Valores asignados: x={}, y={}".format(x, y))

# Inmutables -> TypeError
# punto_a[1] = 5

# Tuplas para swappear valores
y, x = x, y  # Se crea una tupla que luego es desempaquetada
print("Valores asignados: x={}, y={}".format(x, y))
