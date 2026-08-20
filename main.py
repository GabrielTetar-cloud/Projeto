from fastapi import FastAPI
import random
from pydantic import BaseModel
app = FastAPI()

class Estudante(BaseModel):
    name:str
    curso: str
    ativo: bool


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/funcaoteste")
async def funcaoteste(item_id: int, q: str | None = None):
    return {"teste": True, "num_aleatorio": random.randint(1,20000)}



@app.post("/estudante/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudante/update/(id_estudante")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("estudante/delete/{id_estudante")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0