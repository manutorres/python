# Bucle for con step
# Escriba un programa para imprimir todos los números del 0 al 100
# que son divisibles por 7.
# Tenga en cuenta que cero se considera divisible por todos los demás
# enteros, por lo que el resultado debe incluir cero.

divisible_by_7 = []
for div in range(0, 101, 7):
    divisible_by_7 += [div]  # Union de listas

print(divisible_by_7)
