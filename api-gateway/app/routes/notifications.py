from fastapi import APIRouter, Request, Response
import httpx
from app.core.config import NOTIFICATION_SERVICE_URL

router = APIRouter()

@router.post("/notify/email")
async def notify_email(request: Request):
    async with httpx.AsyncClient() as client:
        body = await request.body()
        headers = dict(request.headers)
        resp = await client.post(f"{NOTIFICATION_SERVICE_URL}/notify/email", content=body, headers=headers)
        return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))
