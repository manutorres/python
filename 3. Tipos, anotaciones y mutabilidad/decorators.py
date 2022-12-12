# Los decorators son usados para modificar el comportamiento de una función o clase, sin modificarla explícitamente.
# Las funciones son tomadas como argumento de otra función y luego llamadas dentro del wrapper

def hola_decorator(func):
    print("Hola decorator!")
    return func


@hola_decorator
def hola():
    print("Hola")


"""
Es equivalente a:

def hola():
    print("Hola")


hola = hola_decorator(hola)
"""

hola()


print()
############################################################################

# Funcion decorador: recibe otra función a la cual modifica comportamiento


def saludo_decorator(func):
    # Wrapper: Ejecuta la función recibida y agrega nueva lógica
    def funcion_interna():
        print("Dentro del wrapper, antes de ejecutar la función")
        # Llamado a la función externa recibida
        func()
        print("Dentro del wrapper, después de ejecutar la función")

    return funcion_interna


@saludo_decorator
def funcion_a_usar():
    print("Funcion a usar ejecutándose!")


# Lo que sucede al aplicar el decorador a la funcion
# funcion_a_usar = saludo_decorator(funcion_a_usar)

funcion_a_usar()
