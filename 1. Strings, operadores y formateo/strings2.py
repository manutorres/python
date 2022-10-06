ciudad = "Río Colorado"

print(ciudad)

print(ciudad[-11])
print(ciudad[-1])
print(ciudad[-5])
print(ciudad[-11])
print(ciudad[-8])
print(ciudad[-6])

print()

print(ciudad[0:6])
print(ciudad[3:5])
print(ciudad[:9])   # no start = 0
print()

print(ciudad[10:14])
print(ciudad[-4:])
print()

print(ciudad[:6] + ciudad[6:])
print(ciudad[:])
print()

print(ciudad[-4:-2])
print(ciudad[-4:12])
print()

print(ciudad[0:6:2])
print(ciudad[0:6:3])
print()
print("-" * 80)

# number = "9,223;342:234 456,982;234"
# separators = number[1::4]   #Slice de posicion 1 al final saltando de a 4

number = input(
    "Por favor ingrese una serie de números, usando cualquier separador: ")
# Si no supiera la posicion de los separadores
# Obtengo todos los separadores encontrados
separators = ""
for char in number:
    if not char.isnumeric():
        separators += char

print(separators)
print()

values = "".join(char if char not in separators else " " for char in number)
print("Separadores reemplazados por espacios: " + values)
split_values = values.split()
print("Valores separados en una lista de strings: {}".format(split_values))
int_values = [int(val) for val in split_values]
print("Valores convertidos a una lista de int: {}".format(int_values))

print("La suma total: {}".format(sum(int_values)))
