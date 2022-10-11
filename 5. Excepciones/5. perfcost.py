from timeit import timeit


codigo1 = """
def division(x, y):
    if y == 0:
        raise ZeroDivisionError("El divisor no puede ser cero")
    return x / y


try:
    resultado = division(2, 0)
except ZeroDivisionError as e:
    # print(e)
    pass
"""

print("Primer codigo: ", timeit(codigo1, number=10000))

codigo2 = """
def division(x, y):
    if y == 0:
        return None
    return x / y


resultado = division(2, 0)
if resultado == None:
    # print(e)
    pass
"""

print("Segundo codigo: ", timeit(codigo2, number=10000))
