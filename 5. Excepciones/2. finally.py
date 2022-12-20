# Necesitamos cerrar el archivo abierto para que quede disponible
# a otros usos, ocurra o no una excepcion

try:
    # Considerar modo de ejecucion (debug/consola) para determinar el nombre de archivo
    file = open("5. Excepciones/1. exceptions.py")
    # ValueError al ingresar un valor no numerico
    edad = int(input("Ingrese su edad: "))
    # ZeroDivisionError si la edad es cero
    divisor = 10 / edad
except (ValueError, ZeroDivisionError):
    print("Por favor ingrese una edad valida.")
else:
    print("Ninguna excepcion fue disparada.")
finally:
    # Codigo que se ejecuta ocurra o no una excepcion
    file.close()
