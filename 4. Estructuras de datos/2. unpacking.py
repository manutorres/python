letras = ["a", "b", "c"]
print(letras)

numeros = list(range(20))
print(numeros)

a, b, c = letras
print("Las variables a, b y c valen: {}, {} y {}".format(a, b, c))

uno, dos, *otros = numeros
print("Las variables uno, dos y otros valen: {}, {} y {}".format(
    uno, dos, otros))

# Desempaquetado en una lista
numeros = [*range(5)]
print(numeros)

letras = [*"Python"]
print(letras)

combinado = [*numeros, *letras]
print(combinado)
