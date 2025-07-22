from sqlalchemy.orm import Session
from app.models.order import Order, OrderStatus
from app.schemas.order import OrderCreate, OrderUpdate
from fastapi import HTTPException, status

def create_order(db: Session, order_in: OrderCreate):
    order = Order(description=order_in.description, status=order_in.status)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def list_orders(db: Session):
    return db.query(Order).all()

def get_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

def update_order(db: Session, order_id: int, order_in: OrderUpdate):
    order = get_order(db, order_id)
    order.status = order_in.status
    db.commit()
    db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    db.delete(order)
    db.commit()
