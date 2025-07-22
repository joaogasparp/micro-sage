from fastapi import APIRouter, status
from app.api.schemas import NotificationMessage
from app.services.notify import send_email, send_sms, send_event

router = APIRouter()

@router.post("/email", status_code=status.HTTP_200_OK)
def notify_email(payload: NotificationMessage):
    send_email(payload)
    return {"message": "Email notification simulated."}

@router.post("/sms", status_code=status.HTTP_200_OK)
def notify_sms(payload: NotificationMessage):
    send_sms(payload)
    return {"message": "SMS notification simulated."}

@router.post("/event", status_code=status.HTTP_200_OK)
def notify_event(payload: NotificationMessage):
    send_event(payload)
    return {"message": "Event notification simulated."}
