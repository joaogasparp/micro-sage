from pydantic import BaseModel
from typing import Optional

class NotificationMessage(BaseModel):
    type: str  # email, sms, web, etc.
    to: Optional[str] = None
    subject: Optional[str] = None
    message: str
    external_id: Optional[str] = None
