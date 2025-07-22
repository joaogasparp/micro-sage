from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.order import OrderStatus

class OrderBase(BaseModel):
    description: str
    status: Optional[OrderStatus] = OrderStatus.pending

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: OrderStatus

class OrderRead(OrderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
