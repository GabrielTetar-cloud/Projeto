from src.main import *
from unittest.mock import patch




def teste_root():
    assert root() == {"message":"Heloo World"}


def funcaoteste():
    with patch('random.randint',return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "numaleatorio": 12345}



def teste_create_estudante():
    estudante_teste = Estudante(name='Gabriel', curso='ADS', ativo=False)
    assert estudante_teste == create_estudante()


def teste_update_estudante_negativo():
    assert not update_estudante(-5)

def teste_update_estudante_positivo():
    assert update_estudante(10)


def delete_estudante_negativo():
    assert not delete_estudante(-5)

def delete_estudante_positivo():
    assert  delete_estudante(10)


