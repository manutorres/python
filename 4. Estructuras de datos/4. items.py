letras = ["a", "b", "c"]

# Agregar al final
letras.append("d")
print(letras)

# En cualquier lugar
letras.insert(0, "-")
print(letras)

# Borrar
letras.pop(3)
print(letras)

letras.remove("b")  # ValueError si no la encuentra
print(letras)

del letras[0:3]
print(letras)

# Dejar vacia
letras.clear()
print(letras)

if "d" in letras:
    print(letras.index("d"))  # ValueError si no la encuentra
