from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

def http_exception_handler(request: Request, exc: HTTPException):
    """Manipulador personalizado para HTTPException"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "status_code": exc.status_code,
            "detail": exc.detail
        }
    )

def generic_exception_handler(request: Request, exc: Exception):
    """Manipulador para erros não tratados(500)"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": True,
            "status_code": 500,
            "detail": "Erro interno do servidor."
        }
    )