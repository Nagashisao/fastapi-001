from fastapi import FastAPI
from .routers import itens


app = FastAPI()

app.include_router(itens.router)

@app.get("/")
def raiz() -> dict:
    return {"mensagem": "String"}