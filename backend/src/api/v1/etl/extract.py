from typing import Any
from fastapi import APIRouter
from backend.src.etl.extract import extract
from pathlib import Path

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])

@router.get("/extract")
def run_extract() -> dict[str, Any]:
    project_root = Path(__file__).parent.parent.parent.parent.parent.parent
    csv_path = project_root / "cfg" / "dataset-cars-dirty.csv"
    data = extract(str(csv_path))
    return {"statusCode": 200, "message": "Data extracted successfully", "data": data}