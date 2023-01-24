# Se describe una situación en la que los monos se pasan bananas unos a otros.
# Cada mono se puede representar como una instancia de una clase de Python con su id y su cantidad de bananas como ATRIBUTOS DE INSTANCIA.
# Sin embargo, hay muchos monos y necesitan poder interactuar entre ellos.
# Para almacenar todos los monos y que puedan interactuar entre ellos se puede definir un diccionario
# con todas las instancias de Mono como ATRIBUTO DE CLASE de la clase Mono.
# Usando Mono.monos[id] se puede acceder a todos los monos existentes sin necesidad de una clase extra o un diccionario externo


class Mono:
    monos = dict()

    def __init__(self, id=int):
        self.id = id
        self.cant_bananas = 3
        Mono.monos[id] = self

    def pasar_banana(self, id_destinatario: int):
        self.cant_bananas -= 1
        Mono.monos[id_destinatario].cant_bananas += 1


m1 = Mono("id1")
m2 = Mono("id2")
print(m1.cant_bananas, m2.cant_bananas)

m1.pasar_banana("id2")
print(m1.cant_bananas, m2.cant_bananas)
