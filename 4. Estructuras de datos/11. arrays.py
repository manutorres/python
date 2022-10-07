from array import array

# Menos memoria y un poco mas rapido para grandes cantidades > 10000

numeros = array("i", [1, 2, 3])
numeros.append(4)
numeros.pop(2)
numeros.insert(2, 5)

print(list(numeros))

# No admite valores de otro tipo -> TypeError
# numeros[1] = "a"
