# Comprehensions de listas y diccionarios
lista = [2, 3, 5, 7, 11]
lista_al_cuadrado = [x**2 for x in lista]  # list comprehension
print(lista_al_cuadrado)

dicc_al_cuadrado = {x: x**2 for x in lista}  # dict comprehension
print(dicc_al_cuadrado)

# Iteración paralela sobre dos listas
a = [1, 2, 3]
b = [7, 8, 9]
suma_paralela = [(x + y) for (x, y) in zip(a, b)]  # iterador en paralelo
print(suma_paralela)

# Iteración anidada sobre dos listas
producto_cartesiano = [(x, y) for x in a for y in b]
print(producto_cartesiano)
