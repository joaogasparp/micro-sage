from fastapi import FastAPI
from app.api import orders

app = FastAPI(title="Order Service", version="1.0.0")

app.include_router(orders.router, prefix="/orders", tags=["orders"])
