from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = Field(..., ge=0)
    price: Optional[float] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = None

class ItemRead(ItemBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
