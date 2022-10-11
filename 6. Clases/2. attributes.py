# Clase: molde para crear objetos que comparten caracteristicas
# Objeto: instacia de una clase

class Punto:
    # Atributo a nivel de clase
    color = "Rojo"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        print(f"Punto ({self.x}, {self.y})")


punto = Punto(1, 2)
punto.dibujar()

# Atributo de instacia definido dinamicamente
punto.z = 3
print(punto.z)

otro_punto = Punto(3, 4)
otro_punto.dibujar()

print(punto.color)
print(Punto.color)

# Los atributos de clase son compartidos por todas las instancias
Punto.color = "Azul"
print(otro_punto.color)
