# Clase: molde para crear objetos que comparten caracteristicas
# Objeto: instacia de una clase

class Punto:
    # Magic method ejecutado automaticamente al crear instancia
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)


punto = Punto(1, 2)
otro = Punto(3, 4)

# == por defecto compara direcciones de memoria
print(punto == otro)

# > no esta definido por defecto para instancias de punto
print(punto > otro)

# Al definir >, Python resuelve como tratar el <
print(punto < otro)

suma = punto + otro
print(suma.x, suma.y)
