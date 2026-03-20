from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float

class ItemDatabase:
    def __init__(self):
        self._itens: Dict[int, dict] = {
            1: {"nome": "Maçã", "preco": 1.50},
            2: {"nome": "Banana", "preco": 2.00},
            3: {"nome": "Laranja", "preco": 1.75},
            4: {"nome": "Pera", "preco": 2.30},
        }
        self._proximo_id = 5

    def listar(self, skip: int = 0, limit: int = 10) -> list[dict]:
        """Retorna lista paginada de todos os itens."""
        todos = list(self._itens.values())
        return todos[skip: skip + limit]
    
    def obter(self, item_id: int) -> dict:
        """Retorna um item ou levanta 404."""
        if item_id not in self._itens:
            raise HTTPException(status_code=404, detail="Item não encontrado.")
        return self._itens[item_id]
    
    def criar(self, item: Item) -> dict:
        """Cria um novo item e retorna com ID."""
        novo_item = item.model_dump()
        self._itens[self._proximo_id] = novo_item
        self._proximo_id += 1
        return {"id": self._proximo_id - 1, **novo_item}
    
    def atualizar(self, item_id: int, item: Item) -> dict:
        """Atualiza um item existente."""
        if item_id not in self._itens:
            raise HTTPException(status_code=404, detail="Item não encontrado.")
        self._itens[item_id] = item.model_dump()
        return {"id": item_id, **self._itens[item_id]}
    
    def remover(self, item_id: int) -> None:
        """Função vazia que remove um item"""
        if item_id not in self._itens:
            raise HTTPException(status_code=404, detail="Item não encontrado.")
        self._itens.pop(item_id)

db = ItemDatabase()

@app.get("/")
def raiz() -> dict:
    return {"mensagem": "String"}

@app.get("/itens/")
def listar_itens(skip: int = 0, limit: int = 10) -> list[dict]:
    return db.listar(skip, limit)

@app.get("/itens/{item_id}")
def ler_item(item_id: int) -> dict:
    item = db.obter(item_id)
    return {"id": item_id, **item}

@app.post("/itens/", status_code=201)
def criar_item(item: Item) -> dict:
    return db.criar(item)

@app.put("/itens/{item_id}")
def atualizar_item(item_id: int, item: Item) -> dict:
    return db.atualizar(item_id, item)

@app.delete("/itens/{item_id}", status_code=204)
def remover_item(item_id: int) -> None:
    db.remover(item_id)
    return