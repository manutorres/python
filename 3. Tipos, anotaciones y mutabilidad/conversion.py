x = input("x: ")
# y = x + 1   # TypeError

# Python es fuertemente tipado. No realiza conversiones implicitas
# Usar funciones de conversion explicitas

print(int(x))
print(float(x))
print(bool(x))  # Valores falsos: "", 0, [], None
