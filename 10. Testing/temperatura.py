def hace_calor(temperatura: int) -> bool:
    return temperatura > 25


def esta_helando(temperatura: int) -> bool:
    # Mal funcionamiento de la funcion que usa 6 en lugar de 0
    return temperatura < 6
