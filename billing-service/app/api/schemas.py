from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class PaymentBase(BaseModel):
    order_id: UUID
    amount: float
    status: str = Field(default="pending")

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    status: str

class PaymentRead(PaymentBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    payment_id: UUID
    file_url: Optional[str] = None

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceRead(InvoiceBase):
    id: UUID
    issued_at: datetime

    class Config:
        orm_mode = True
