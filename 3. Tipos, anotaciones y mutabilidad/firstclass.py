# Las funciones en Python son objetos de primera clase.
# Pueden ser almacenadas en variables:

def gritar(mensaje: str):
    return mensaje.upper()


def susurrar(mensaje: str):
    return mensaje.lower()


mensaje = "Hola amigos y amigas"
saludo = gritar
print(saludo(mensaje))

saludo = susurrar
print(saludo(mensaje))


# Pueden ser pasadas por parámetro:

def saludo(func):
    saludar = func(
        "Hola! Este saludo fue creado por una función pasada por argumento!"
    )
    print(saludar)


saludo(gritar)
saludo(susurrar)


# Pueden ser retornadas por otra función:

def crear_potenciador():
    def potencia(x):
        return x*x
    return potencia


operacion = crear_potenciador()
print(operacion(10))
