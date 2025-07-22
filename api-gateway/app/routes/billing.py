from fastapi import APIRouter, Request, Response, status
import httpx
from app.core.config import BILLING_SERVICE_URL

router = APIRouter()

@router.post("/billing/pay", status_code=status.HTTP_201_CREATED)
async def pay(request: Request):
    async with httpx.AsyncClient() as client:
        body = await request.body()
        headers = dict(request.headers)
        resp = await client.post(f"{BILLING_SERVICE_URL}/payments/", content=body, headers=headers)
        return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))
