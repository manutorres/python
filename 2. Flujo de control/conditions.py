age = int(input("Qué edad tenés? "))

# if age >= 16 and age <= 65:

# Comparacion simplificada
# if 16 <= age <= 65:
if age in range(16, 66):  # Condicion con range. NO efectiva
    print("Tenga un buen día en el trabajo")
else:
    print("Disfrute el tiempo libre")

print("-" * 80)

if age < 16 or age > 65:
    print("Disfrute el tiempo libre")
else:
    print("Tenga un buen día en el trabajo")
