from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float

itens_exemplo = [
    {"nome": "Maçã", "preco": 1.50},
    {"nome": "Banana", "preco": 2.00},
    {"nome": "Laranja", "preco": 1.75},
    {"nome": "Pera", "preco": 2.30},
]

@app.get("/")
def raiz():
    return {"mensagem" : "String"}

@app.get("/itens/")
def listar_itens(skip: int = 0, limit: int = 10):
    return itens_exemplo[skip: skip + limit]

@app.get("/itens/{item_id}")
def ler_item(item_id : int):
    if item_id < 0 or item_id >= len(itens_exemplo):
        raise HTTPException(status_code=404, detail="Item não encontrado.")
    item = itens_exemplo[item_id]
    return {"id" : item_id, **item}

@app.post("/itens/")
def criar_item(item: Item):
    novo_item = item.model_dump()
    itens_exemplo.append(novo_item)
    return novo_item