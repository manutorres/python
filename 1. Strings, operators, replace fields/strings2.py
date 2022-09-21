parrot = "Norwegian Blue"

print(parrot)

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[0:6])
print(parrot[3:5])
print(parrot[:9])   # no start = 0
print()

print(parrot[10:14])
print(parrot[-4:])
print()

print(parrot[:6] + parrot[6:])
print(parrot[:])
print()

print(parrot[-4:-2])
print(parrot[-4:12])
print()

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw
print()
print("-" * 80)

#number = "9,223;342:234 456,982;234"
#separators = number[1::4]   #Slice de posicion 1 al final saltando de a 4

number = input("Please enter a series of numbers, using any separators you like: ")
# Si no supiera la posicion de los separadores
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