for i in range(1, 13):
    print("El numero {0:2} al cuadrado es {1:3} y al cubo es {2:4}".format(
        i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("El numero {0:2} al cuadrado es {1:<3} y al cubo es {2:^4}".format(
        i, i ** 2, i ** 3))

print()

print("Pi es aproximadamente {0:12}".format(22 / 7))
print("Pi es aproximadamente {0:12f}".format(
    22 / 7))     # Default 6 digitos decimales
print("Pi es aproximadamente {0:12.50f}".format(
    22 / 7))  # Se ignora el 12 por precision
print("Pi es aproximadamente {0:52.50f}".format(22 / 7))
print("Pi es aproximadamente {0:62.50f}".format(22 / 7))
print("Pi es aproximadamente {0:<72.50f}".format(22 / 7))
print("Pi es aproximadamente {0:<72.54f}".format(22 / 7))
print()

for i in range(1, 13):
    print("El numero {} al cuadrado es {} y al cubo es {:4}".format(i, i ** 2, i ** 3))
