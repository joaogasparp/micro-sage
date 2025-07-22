from fastapi import FastAPI
from app.routes.orders import router as orders_router
from app.routes.billing import router as billing_router
from app.routes.inventory import router as inventory_router
from app.routes.notifications import router as notifications_router
from app.routes.logs import router as logs_router

app = FastAPI(title="API Gateway - MicroSage", version="1.0.0")

app.include_router(orders_router)
app.include_router(billing_router)
app.include_router(inventory_router)
app.include_router(notifications_router)
app.include_router(logs_router)
