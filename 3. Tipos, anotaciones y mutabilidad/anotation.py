x = 1
x = "string"

print(x)
print(type(x))

# Indica el tipo sin forzar ningun control (Algunos Linting Tools chequean)
y: int = 1
y = "otro string"

print(x)
print(type(x))


def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, by=3))
# print(increment(2, by="3"))  # Error al operar +, no de control
