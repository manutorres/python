class NubeDeTags:
    def __init__(self):
        # __tags pasa a ser atributo privado, inaccesible
        self.__tags = {}

    # Sumar una aparicion de un determinado tag
    def add(self, tag):
        # Encapsulamos el problema del case-sensitive de tags
        # inherente a un diccionario predefinido
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # Definimos el acceso por indice que no esta predefinido
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # Establecemos de forma directa la cantidad de apariciones
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    # Retorna un iterador que permite recorrer la estructura
    def __iter__(self):
        return iter(self.__tags)


nube = NubeDeTags()

nube.add("Python")
nube.add("python")
nube.add("python")
# print(nube.tags)

# print(nube["python"])

nube["JavaScript"] = 10

print(len(nube))

for tag in nube:
    print(tag)

# Error por posibilidad de acceso al diccionario (es case sensitive)
# Ni tags ni __tags son atributos accesibles
# print(nube.tags["PYTHON"])

# Forma de lograr acceso a atributos privados de todas formas
print(nube.__dict__)  # Todos los atributos de la instancia
print(nube._NubeDeTags__tags)
