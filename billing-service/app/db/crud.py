from sqlalchemy.orm import Session
from app.db.models import Payment, Invoice
from app.api.schemas import PaymentCreate, PaymentUpdate, InvoiceCreate
from fastapi import HTTPException, status
import uuid

def create_payment(db: Session, payment_in: PaymentCreate):
    payment = Payment(**payment_in.dict())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

def get_payments(db: Session):
    return db.query(Payment).all()

def get_payment(db: Session, payment_id: str):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return payment

def update_payment(db: Session, payment_id: str, payment_in: PaymentUpdate):
    payment = get_payment(db, payment_id)
    payment.status = payment_in.status
    db.commit()
    db.refresh(payment)
    return payment

def create_invoice(db: Session, invoice_in: InvoiceCreate):
    invoice = Invoice(**invoice_in.dict())
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

def get_invoice(db: Session, invoice_id: str):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found")
    return invoice
