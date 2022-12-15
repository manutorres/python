from pprint import pprint

oracion = "Esta es una pregunta de entrevista clasica"
oracion = "".join(oracion.split())
print(oracion)

repeticiones = {}
for letra in oracion:
    if letra in repeticiones:
        repeticiones[letra] += 1
        continue
    repeticiones[letra] = 1

pprint(repeticiones, width=20)

# Pasarlo a tupla para luego ordenarlo usando SORT
lista_de_tuplas = [*repeticiones.items()]
lista_de_tuplas.sort(key=lambda item: item[1], reverse=True)
mas_repetida, cantidad = lista_de_tuplas.pop(0)
print("La letra mas repetida es {}. Aparece {} veces".format(
    mas_repetida, cantidad))

# Usando SORTED que puede recibir los dict_items
tupla = sorted(repeticiones.items(),
               key=lambda item: item[1],
               reverse=True)
print(tupla[0])

# Forma tradicional sin funciones predefinidas de Python
# cantidad = 0
# mas_repetida = ""
# for letra, cant in repeticiones.items():
#     if cant > mayor:
#         mas_repetida = letra
#         cantidad = cant

# print("La letra mas repetida es {}. Aparece {} veces".format(mas_repetida, cantidad))
