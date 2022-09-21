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

number = "9,223;342:234 456,982;234"
separators = number[1::4]
print(separators)
print()

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])