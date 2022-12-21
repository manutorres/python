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
        print("Animal comiendo")


class Mamifero(Animal):
    def __init__(self):
        # Llama al constructor padre (de lo contrario es sobreescrito)
        super().__init__()
        self.weight = 10

    def caminar(self):
        print("Mamifero caminando")
        Animal.comer(self)  # Redundante, solo a modo de prueba


class Pez(Animal):
    def nadar(self):
        print("Pez nadando")


mamifero = Mamifero()
mamifero.comer()
mamifero.caminar()

pez = Pez()
pez.nadar()
print(pez.age)

# isinstance()
print(isinstance(mamifero, Animal))
print(isinstance(pez, object))

# issubclass()
print(issubclass(Mamifero, Animal))
print(issubclass(Pez, Mamifero))
