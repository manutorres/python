from collections import namedtuple

# Evita usar clases que solo almacenan datos sin metodos
Punto = namedtuple("Punto", ["x", "y"])

# Los keyword arguments hacen el codigo mas claro
p1 = Punto(x=1, y=2)
p2 = Punto(x=1, y=2)

# Compara los atributos en vez de las direcciones de memoria (default)
print(p1 == p2)

# TypeError porque las tuplas son inmutables
p1["x"] = 3
