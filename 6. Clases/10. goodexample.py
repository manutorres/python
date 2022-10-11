class InvalidOperationError(Exception):
    pass


class Stream:
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


class FileStream(Stream):
    def leer(self):
        print("Leyendo datos de un archivo")


class NetworkStream(Stream):
    def leer(self):
        print("Leyendo datos de una red")


# Bajo esta implementacion puedo llamar abrir en Stream
# que deberia ser un concepto abstracto
stream = Stream()
stream.abrir()
