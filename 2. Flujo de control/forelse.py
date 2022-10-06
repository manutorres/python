names = ["Juan", "Laura", "Carlos", "Sofia"]
for name in names:
    if name.startswith("K"):
        print("Encontrado")
        break
else:  # Ejecutado solo si termina el ciclo for sin break
    print("No encontrado")
