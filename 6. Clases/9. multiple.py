class Empleado:
    def saludar(self):
        print("Saludo de empleado")


class Persona:
    def saludar(self):
        print("Saludo de persona")


# Se ejecuta el saludo de la primera clase de la lista
# Mal uso de le herencia multiple que introduce problemas
class Jefe(Empleado, Persona):
    pass


jefe = Jefe()
jefe.saludar()
