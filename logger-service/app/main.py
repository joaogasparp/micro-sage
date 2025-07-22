from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Logger Service", version="1.0.0")
app.include_router(router, prefix="/logs", tags=["logs"])
