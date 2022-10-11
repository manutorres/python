# Clase: molde para crear objetos que comparten caracteristicas
# Objeto: instacia de una clase

class Punto:
    # Magic method ejecutado automaticamente al crear instancia
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic method ejecutado para imprimir o convertir a str un objeto
    def __str__(self):
        return f"({self.x}, {self.y})"

    def dibujar(self):
        print(f"Punto ({self.x}, {self.y})")


punto = Punto(1, 2)
print(punto)
punto_en_string = str(punto)
print(punto_en_string)
