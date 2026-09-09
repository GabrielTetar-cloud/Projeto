import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso:str
    ativo:bool


@app.get("/helloWorld")
async def root():
    return {"message": "HeloWorld" }



@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": True, "numaleatorio": random.randint}

@app.get("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0