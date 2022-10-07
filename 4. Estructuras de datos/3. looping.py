letras = ["a", "b", "c"]

for letra in letras:
    print(letra)

for tupla in enumerate(letras):
    print(tupla)
    index, letra = tupla
    print(index, "-", letra)
