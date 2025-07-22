from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.api.schemas import PaymentCreate, PaymentRead, PaymentUpdate, InvoiceCreate, InvoiceRead
from app.db.crud import (
    create_payment, get_payment, get_payments, update_payment,
    create_invoice, get_invoice
)
from app.db.database import get_db

router = APIRouter()

@router.post("/payments/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
def create(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db, payment)

@router.get("/payments/", response_model=list[PaymentRead])
def list_all(db: Session = Depends(get_db)):
    return get_payments(db)

@router.get("/payments/{payment_id}", response_model=PaymentRead)
def get(payment_id: str, db: Session = Depends(get_db)):
    return get_payment(db, payment_id)

@router.put("/payments/{payment_id}", response_model=PaymentRead)
def update(payment_id: str, payment: PaymentUpdate, db: Session = Depends(get_db)):
    return update_payment(db, payment_id, payment)

@router.post("/invoices/", response_model=InvoiceRead, status_code=status.HTTP_201_CREATED)
def create_inv(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db, invoice)
