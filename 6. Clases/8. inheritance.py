# class Mamifero:
#     def comer(self):
#         print("Comiendo")

#     def caminar(self):
#         print("Caminando")


# class Pez:
#     def comer(self):
#         print("Comiendo")

#     def nadar(self):
#         print("Nadando")


class Animal:
    def __init__(self):
        self.age = 1

    def comer(self):
        print("Comiendo")


class Mamifero(Animal):
    def __init__(self):
        # Llama al constructor padre (de lo contrario es sobreescrito)
        super().__init__()
        self.weight = 10

    def caminar(self):
        print("Caminando")


class Pez(Animal):
    def nadar(self):
        print("Nadando")


mamifero = Mamifero()
mamifero.caminar()
mamifero.comer()

pez = Pez()
pez.nadar()
print(pez.age)

# isinstance()
print(isinstance(mamifero, Animal))
print(isinstance(pez, object))

# issubclass()
print(issubclass(Mamifero, Animal))
