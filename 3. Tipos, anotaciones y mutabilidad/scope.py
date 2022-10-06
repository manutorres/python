message = "a"


def greet():
    # Acceso a modificar la variable de manera global (mala practica)
    # global message
    if True:  # La variable pertenece a la funcion, no al bloque
        message = "b"  # La variable ahora referencia otra ubicacion
    print(id(message))


print(id(message))
greet()
print(id(message))
print(message)
