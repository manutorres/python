# Clase: molde para crear objetos que comparten caracteristicas
# Objeto: instacia de una clase

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        print(f"Punto ({self.x}, {self.y})")


punto = Punto(1, 2)
print(type(punto))
print(isinstance(punto, int))
print(isinstance(punto, Punto))

print("X en punto vale:", punto.x)

punto.dibujar()
