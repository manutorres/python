import sys

if len(sys.argv) == 1:
    # Un argumento = nombre de la aplicacion
    print("USO: Python script.py <nombre>")
else:
    nombre = sys.argv[1]
    print("Nombre:", nombre)
