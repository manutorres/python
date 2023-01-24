# Leer letras de líneas (ver la entrada a continuación). Cada letra está en un cuarto índice, comenzando desde el índice 1.

# ENTRADA
#     [D]
# [N] [C]
# [Z] [M] [P]

# SALIDA DESEADA
# [' D ', 'NC', 'ZMP']


# VERSION CON DOBLE CICLO FOR PARA RECORRER LINEAS Y LETRAS
with open("11. Desafíos/letras.txt") as archivo:
    resultado = []
    for line in archivo:
        grupo = ""
        for index in range(1, len(line), 4):
            grupo += line[index]
        resultado.append(grupo)
    print(resultado)


# VERSION EN UNA LINEA CON CODIGO REDUNDANTE
with open("11. Desafíos/letras.txt") as archivo:
    resultado = ["".join([line[1:len(line):4]])
                 for line in archivo.read().split("\n")]
    print(resultado)


# VERSION PYTHON MINIMALISTA
with open("11. Desafíos/letras.txt") as archivo:
    resultado = [line[1::4] for line in archivo]
    print(resultado)
