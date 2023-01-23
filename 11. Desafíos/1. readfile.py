# Leer un archivo con varios bloques de números. Cada bloque está separada por una línea vacía ('\n\n') y cada línea por un salto de línea ('\n').
# Los valores deben ser interpretados como tipo int para permitir futuras operaciones

# ENTRADA
# 10
# 20
# 30

# 50
# 60
# 70

# SALIDA DESEADA: [[10, 20, 30], [50, 60, 70]]

with open("11. Desafíos/numeros.txt") as archivo:
    lista_general = []
    lista = []
    for linea in archivo:
        if linea == "\n":
            lista_general.append(lista)
            lista = []
        else:
            lista.append(int(linea.rstrip()))
    lista_general.append(lista)
    print(lista_general)


with open("11. Desafíos/numeros.txt") as archivo:
    # Separo por bloques y luego los itero separando por linea y convirtiendo a int cada valor
    lista = [list(map(int, bloque.split()))
             for bloque in archivo.read().split('\n\n')]
    print(lista)
