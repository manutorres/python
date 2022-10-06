name = input("Por favor ingrese su nombre: ")
# Cast a int para evitar errores
age = int(input("Cuántos años tenés, {0}? ".format(name)))
print(age)

# Comentario multilinea con Ctrl + /
# if age >= 18:
#     print("Tenés suficiente edad para votar")
#     print("Por favor, poné una X en el casillero")
# else:
#     print("Por favor regresá en {0} años".format(18-age))

# Mismo resultado con la condicion invertida
if age < 18:
    print("Por favor regresá en {0} años".format(18-age))
elif age == 900:
    print("Perdón, Joda, ya moriste en el retorno del Jedi")
else:
    print("Tenés suficiente edad para votar")
    print("Por favor, poné una X en el casillero")

# Comentario para notar el git diff
