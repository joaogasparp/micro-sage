import json
from app.core.config import LOG_FILE
from app.api.schemas import LogEntry
from typing import List, Optional
from datetime import datetime
import os

def write_log(entry: LogEntry):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(entry.json() + "\n")

def read_logs(skip: int = 0, limit: int = 100) -> List[LogEntry]:
    logs = []
    if not os.path.exists(LOG_FILE):
        return logs
    with open(LOG_FILE, "r") as f:
        for line in f:
            logs.append(LogEntry.parse_raw(line))
    return logs[skip:skip+limit]

def search_logs(source: Optional[str], level: Optional[str], start: Optional[str], end: Optional[str], skip: int, limit: int) -> List[LogEntry]:
    logs = read_logs(0, 10000)
    if source:
        logs = [log for log in logs if log.source == source]
    if level:
        logs = [log for log in logs if log.level == level]
    if start:
        start_dt = datetime.fromisoformat(start)
        logs = [log for log in logs if log.timestamp >= start_dt]
    if end:
        end_dt = datetime.fromisoformat(end)
        logs = [log for log in logs if log.timestamp <= end_dt]
    return logs[skip:skip+limit]
