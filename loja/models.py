from typing import Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do produto. Mínimo de 2 caracteres")
    preco: float = Field(..., gt=0, description="Preço do produto. Valor deve ser maior que zero.")
    marca: Optional[str] = Field(None, min_length=2, description="Marca do produto(Opcional)")