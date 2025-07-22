from sqlalchemy.orm import Session
from app.db.models import Item
from app.api.schemas import ItemCreate, ItemUpdate
from fastapi import HTTPException, status
from uuid import UUID

def create_item(db: Session, item_in: ItemCreate):
    item = Item(**item_in.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items(db: Session):
    return db.query(Item).all()

def get_item(db: Session, item_id: str):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

def update_item(db: Session, item_id: str, item_in: ItemUpdate):
    item = get_item(db, item_id)
    for field, value in item_in.dict(exclude_unset=True).items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: str):
    item = get_item(db, item_id)
    db.delete(item)
    db.commit()
