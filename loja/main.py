from fastapi import FastAPI
from loja.routers import itens
from loja.exceptions import http_exception_handler, generic_exception_handler
from fastapi.exceptions import HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(itens.router)

@app.get("/")
def raiz() -> dict:
    return {"mensagem": "Teste"}