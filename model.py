from typing import List
from pydantic import BaseModel, EmailStr, Field


class Client(BaseModel):
    name: str
    contact: str
    lang: str 


class Item(BaseModel):
    sku: str
    qty: int = Field(..., gt=0)
    unit_cost: float = Field(..., ge=0)
    margin_pct: int


class QuoteRequest(BaseModel):
    client: Client
    currency: str 
    items: List[Item]
    delivery_terms: str
    notes: str | None = None