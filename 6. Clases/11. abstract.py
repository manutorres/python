from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.abierto = False

    def abrir(self):
        if self.abierto:
            raise InvalidOperationError("El archivo ya esta abierto")
        self.abierto = True

    def cerrar(self):
        if not self.abierto:
            raise InvalidOperationError("El archivo ya esta cerrado")
        self.abierto = False

    # Interface que establece una manera de llamar al metodo
    @abstractmethod
    def leer(self):
        pass


class FileStream(Stream):
    def leer(self):
        print("Leyendo datos de un archivo")


class NetworkStream(Stream):
    def leer(self):
        print("Leyendo datos de una red")


class MemoryStream(Stream):
    def leer(self):
        print("Leyendo datos de memoria")


# stream = Stream()
# stream.abrir()

# MemoryStream es abstracta hasta que implemente los metodos abstractos
ms = MemoryStream()
