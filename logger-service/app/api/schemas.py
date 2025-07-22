from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: str
    level: str
    message: str

class LogList(BaseModel):
    logs: List[LogEntry]

class LogQuery(BaseModel):
    source: Optional[str] = None
    level: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    skip: int = 0
    limit: int = 100
