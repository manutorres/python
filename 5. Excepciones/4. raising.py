def division(x, y):
    if y == 0:
        raise ZeroDivisionError("El divisor no puede ser cero")
    return x / y


a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))

try:
    print(division(a, b))
except ZeroDivisionError as e:
    print(e)
