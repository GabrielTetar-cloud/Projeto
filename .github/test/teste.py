from src.main import *
from unittest.mock import patch

import pytest
import asyncio

@pytest.mark.asynio
async def teste_root():
    result = await root()
    assert result == {"message":"Heloo World"}

@pytest.mark.asynio
async def funcaoteste():
    with patch('random.randint',return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "numaleatorio": 12345}


@pytest.mark.asynio
async def teste_create_estudante():
    estudante_teste = Estudante(name='Gabriel', curso='ADS', ativo=False)
    result = await  create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asynio
async def teste_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asynio
async def teste_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asynio
async def delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asynio
async def delete_estudante_positivo():
    result = await delete_estudante(10)
    assert result


