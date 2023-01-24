# Las letras tienen diferentes valores. Las minúsculas a-z tienen valores del 1 al 26, y las mayúsculas a-z tienen valores del 27 al 52.

# VERSION USANDO DICCIONARIO GLOBAL POPULADO MEDIANTE LA FUNCION ENUMERATE
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_dict = dict()
for valor, letra in enumerate(letras, start=1):
    letras_dict[letra] = valor


def valor_de_letra(letra: str) -> int:
    return letras_dict[letra]


print(valor_de_letra("P"))


# VERSION USANDO UN STRING DE LETRAS COMO LOOKUP TABLE
def valor_de_letra_lookup(letra: str) -> int:
    return letras.index(letra) + 1


print(valor_de_letra_lookup("h"))
