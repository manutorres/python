import temperatura
import pytest


def test_hace_calor():
    t = 28
    hace_calor = temperatura.hace_calor(t)
    assert hace_calor == True


def test_esta_helando():
    t = 5
    esta_helando = temperatura.esta_helando(t)
    assert esta_helando == False
