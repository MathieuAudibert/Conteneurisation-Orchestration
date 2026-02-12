from typing import Any
from fastapi import APIRouter, HTTPException
from backend.src.core.db.doctrine import Doctrine

router = APIRouter(prefix="/api/v1/data", tags=["data"])

@router.get("/logs")
def get_all_logs() -> dict[str, Any]:
    """Get all logs from MongoDB"""
    try:
        doctrine = Doctrine()
        logs = doctrine.select_all("logs")
        for log in logs:
            if '_id' in log:
                log['_id'] = str(log['_id'])
        return {
            "statusCode": 200,
            "data": logs,
            "count": len(logs)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching logs: {str(e)}")

@router.get("/logs/recent")
def get_recent_logs(limit: int = 10) -> dict[str, Any]:
    try:
        doctrine = Doctrine()
        logs = doctrine.select_all("logs")
        for log in logs:
            if '_id' in log:
                log['_id'] = str(log['_id'])
        recent_logs = logs[-limit:] if len(logs) > limit else logs
        return {
            "statusCode": 200,
            "data": recent_logs,
            "count": len(recent_logs)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recent logs: {str(e)}")
