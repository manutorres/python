# Necesitamos cerrar el archivo abierto para que quede disponible
# a otros usos, ocurra o no una excepcion

try:
    # Python cierra el archivo automaticamente para liberar
    # el recurso sin necesidad del finally
    # Si un objeto soporta Context Management Protocol (tiene __enter y __exit)
    # Python aplica la liberacion de recursos
    with open("exceptions.py") as file:
        print("Archivo abierto.")

    edad = int(input("Ingrese su edad: "))
    divisor = 10 / edad
except (ValueError, ZeroDivisionError):
    print("Por favor ingrese una edad valida.")
else:
    print("Ninguna excepcion fue disparada.")
