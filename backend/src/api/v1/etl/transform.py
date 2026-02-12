from typing import Any
from fastapi import APIRouter
from backend.src.etl.transform import transform_from_file
from backend.src.core.logger import get_logger
from pathlib import Path

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])
logger = get_logger(__name__)

@router.get("/transform")
def run_transform() -> dict[str, Any]:
    try:
        project_root = Path(__file__).parent.parent.parent.parent.parent.parent
        csv_path = project_root / "cfg" / "dataset-cars-dirty.csv"
        df = transform_from_file(str(csv_path), logger=logger)
        return {
            "statusCode": 200,
            "message": "Data transformed successfully",
            "rows": len(df),
            "columns": list(df.columns)
        }
    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        return {
            "statusCode": 500,
            "message": f"Error during transformation: {str(e)}"
        }