from src.main import *
from unittest.mock import patch



def teste_root():
    result = root()
    yield result
    assert result == {"message":"Heloo World"}


def funcaoteste():
    with patch('random.randint',return_value=12345):
        result = funcaoteste()
        yield result
    assert result == {"teste": True, "numaleatorio": 12345}



def teste_create_estudante():
    estudante_teste = Estudante(name='Gabriel', curso='ADS', ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result


def teste_update_estudante_negativo():
    result = update_estudante(-5)
    yield  result
    assert not result

def teste_update_estudante_positivo():
    result = update_estudante(10)
    yield result
    assert result


def delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result

def delete_estudante_positivo():
    result = delete_estudante(10)
    yield result
    assert result


