from array import array

# Menos memoria y un mas eficiente para grandes cantidades (> 10000 aprox)

numeros = array("i", [1, 2, 3])  # i = Typecode para integer
numeros.append(4)
numeros.pop(2)
numeros.insert(2, 5)

print(list(numeros))

# No admite valores de otro tipo -> TypeError
# numeros[1] = "a"
