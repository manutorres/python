# Clase: molde para crear objetos que comparten caracteristicas
# Objeto: instacia de una clase

class Punto:
    # Magic method ejecutado automaticamente al crear instancia
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def cero(cls):
        return cls(0, 0)

    def dibujar(self):
        print(f"Punto ({self.x}, {self.y})")


punto = Punto(1, 2)

# punto inicializado con un metodo de clase
otro_punto = Punto.cero()
otro_punto.dibujar()
