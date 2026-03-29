from fastapi import APIRouter, Depends
from loja.models import Item
from loja.database import ItemDatabase, get_db

router = APIRouter(prefix="/itens", tags=["itens"])

@router.get("/")
def listar_itens(skip: int = 0, 
    limit: int = 10,
    db: ItemDatabase = Depends(get_db)
    ) -> list[dict]:
    return db.listar(skip, limit)

@router.get("/{item_id}")
def obter_item(item_id: int,
    db: ItemDatabase = Depends(get_db)
    ) -> dict:
    item = db.obter(item_id)
    return {"id": item_id, **item}

@router.post("/", status_code=201)
def criar_item(item: Item,
    db: ItemDatabase = Depends(get_db)
    ) -> dict:
    return db.criar(item)

@router.put("/{item_id}")
def atualizar_item(item_id: int, 
    item: Item,
    db: ItemDatabase = Depends(get_db)
    ) -> dict:
    return db.atualizar(item_id, item)

@router.delete("/{item_id}", status_code=204)
def remover_item(item_id: int,
    db: ItemDatabase = Depends(get_db)
    ) -> None:
    db.remover(item_id)
    return