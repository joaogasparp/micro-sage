from fastapi import APIRouter, Request, Response, status
import httpx
from app.core.config import INVENTORY_SERVICE_URL

router = APIRouter()

@router.get("/inventory/{item_id}")
async def get_item(item_id: str, request: Request):
    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        resp = await client.get(f"{INVENTORY_SERVICE_URL}/items/{item_id}", headers=headers)
        return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))
