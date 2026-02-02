from fastapi import APIRouter
from backend.src.etl.transform import transform_from_file
from backend.src.core.logger import get_logger

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])
logger = get_logger(__name__)

@router.get("/transform")
def run_transform():
    try:
        df = transform_from_file("cfg/dataset-cars-dirty.csv", logger=logger)
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