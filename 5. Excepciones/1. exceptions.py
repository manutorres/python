# IndexError
numeros = [0, 1]
# print(numeros[2])

try:
    # ValueError al ingresar un valor no numerico
    edad = int(input("Ingrese su edad: "))
    # ZeroDivisionError si la edad es cero
    divisor = 10 / edad
    # IndexError por acceso aun indice que no existe
    numeros = [0, 1]
    print(numeros[2])
except ValueError as e:
    print("Por favor ingrese un valor numerico.")
    print(e, type(e))
except ZeroDivisionError as e:
    print("Ocurrio una division por cero.")
    print(e, type(e))
except:
    print("Excepcion atrapada pero no identificada")
else:
    print("Ninguna excepcion fue disparada.")
