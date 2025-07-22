from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.api.schemas import ItemCreate, ItemRead, ItemUpdate
from app.db.crud import (
    create_item, get_item, get_items, update_item, delete_item
)
from app.db.database import get_db

router = APIRouter()

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/", response_model=list[ItemRead])
def list_all(db: Session = Depends(get_db)):
    return get_items(db)

@router.get("/{item_id}", response_model=ItemRead)
def get(item_id: str, db: Session = Depends(get_db)):
    return get_item(db, item_id)

@router.put("/{item_id}", response_model=ItemRead)
def update(item_id: str, item: ItemUpdate, db: Session = Depends(get_db)):
    return update_item(db, item_id, item)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: str, db: Session = Depends(get_db)):
    delete_item(db, item_id)
    return None
