# Implementacion no "pythonic"
# El atributo es privado y se maneja por su getter y setter
class Producto:
    def __init__(self, valor) -> None:
        # Llamo a set_price para que maneje la logica de control
        self.set_precio(valor)

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser menor a cero.")
        self.__precio = precio


# Implementacion con propiedad y decorators
# La propiedad es accesible como un atributo normal
class Producto2:
    def __init__(self, valor) -> None:
        # Uso precio como un atributo
        self.__precio = valor

    @property  # Decorator para crear una propiedad
    def precio(self):
        return self.__precio

    @precio.setter  # Decorator para indicar el setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser menor a cero.")
        self.__precio = precio


prod = Producto(50)
print(prod.get_precio())

prod2 = Producto2(40)
print(prod2.precio)
prod2.precio = -1
print(prod2.precio)

# AtributeError
# print(prod2.__precio)
