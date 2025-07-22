from fastapi import APIRouter, status, Query
from app.api.schemas import LogEntry, LogQuery, LogList
from app.logs.handler import write_log, read_logs, search_logs
from typing import Optional

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_log(entry: LogEntry):
    write_log(entry)
    return {"message": "Log registered."}

@router.get("/", response_model=LogList)
def get_logs(skip: int = 0, limit: int = 100):
    logs = read_logs(skip=skip, limit=limit)
    return {"logs": logs}

@router.get("/search", response_model=LogList)
def search(
    source: Optional[str] = Query(None),
    level: Optional[str] = Query(None),
    start: Optional[str] = Query(None),
    end: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 100
):
    logs = search_logs(source, level, start, end, skip, limit)
    return {"logs": logs}
