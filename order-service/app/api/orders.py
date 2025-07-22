from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate
from app.services import order_service
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return order_service.create_order(db, order)

@router.get("/", response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return order_service.list_orders(db)

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return order_service.get_order(db, order_id)

@router.put("/{order_id}", response_model=OrderRead)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    return order_service.update_order(db, order_id, order)

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order_service.delete_order(db, order_id)
    return None
