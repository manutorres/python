class Text(str):
    def duplicate(self):
        return self + self


class ListaExtendida(list):
    def append(self, item):
        print("Append de ListaExtendida")
        super().append(item)


# Todos los metodos de String disponibles + duplicate()
text = Text("Python")
print(text.lower())
print(text.duplicate())

lista = ListaExtendida()
lista.append("A")
