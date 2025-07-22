import logging
from app.api.schemas import NotificationMessage

logger = logging.getLogger("notification-service")

def send_email(payload: NotificationMessage):
    logger.info(f"[EMAIL] To: {payload.to} | Subject: {payload.subject} | Message: {payload.message} | External ID: {payload.external_id}")
    print(f"[EMAIL] To: {payload.to} | Subject: {payload.subject} | Message: {payload.message} | External ID: {payload.external_id}")

def send_sms(payload: NotificationMessage):
    logger.info(f"[SMS] To: {payload.to} | Message: {payload.message} | External ID: {payload.external_id}")
    print(f"[SMS] To: {payload.to} | Message: {payload.message} | External ID: {payload.external_id}")

def send_event(payload: NotificationMessage):
    logger.info(f"[EVENT] Type: {payload.type} | Message: {payload.message} | External ID: {payload.external_id}")
    print(f"[EVENT] Type: {payload.type} | Message: {payload.message} | External ID: {payload.external_id}")
