from tiendaonline.envios import costos

# Retorna los atributos de un objeto modulo
print(dir(costos))
print(costos.__name__)
print(costos.__package__)
print(costos.__file__)
print()


# Otros usos de DIR sobre clases y tipos predefinidos

class Clase():
    pass


print(dir(Clase))
print()

print(dir(list))
