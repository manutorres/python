# Se trata de un juego de piedra, papel o tijera. Cada forma elegida (piedra, papel o tijera)
# da como resultado una cantidad diferente de puntos: 1 (X), 2 (Y) y 3 (Z) respectivamente.

# ENTRADA
# X
# Y
# Z

# RESULTADO DESEADO
# 1
# 2
# 3

from enum import Enum


# VERSION CON FUNCION IF-THEN-ELSE
def puntaje(forma: str) -> int:
    if forma == "X":
        return 1
    elif forma == "Y":
        return 2
    elif forma == "Z":
        return 3
    else:
        raise ValueError("Forma desconocida")


# VERSION UTILIZANDO DICCIONARIO
puntajes = {"X": 1, "Y": 2, "Z": 3}


def puntaje_por_forma_dict(forma: str) -> int:
    return puntajes[forma]


print(puntaje_por_forma_dict("X"))


# VERSION UTILIZANDO CLASE QUE EXTIENDE A ENUM
class Puntaje(Enum):
    X = 1
    Y = 2
    Z = 3


def puntaje_por_forma_enum(forma: str) -> int:
    return Puntaje[forma].value


print(puntaje_por_forma_enum("Z"))
