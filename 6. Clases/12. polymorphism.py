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


def consumir_medios(streams):
    for stream in streams:
        # Polimorfismo: se ejecuta el leer() correspondiente
        stream.leer()


fs = FileStream()
ns = NetworkStream()
ms = MemoryStream()
medios = [fs, ns, ms]
consumir_medios(medios)

# Puede lograrse el mismo comportamiento sin emplear herencia teniendo
# en cuenta que Python es dinamicamente tipado
