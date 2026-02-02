from fastapi import APIRouter
from backend.src.etl.transform import transform_from_file
from backend.src.core.db.doctrine import Doctrine
from backend.src.core.logger import get_logger

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])
logger = get_logger(__name__)

@router.get("/load")
def run_load():
    try:
        df = transform_from_file("cfg/dataset-cars-dirty.csv", logger=logger)
        data = df.to_dict(orient='records')
        
        doctrine = Doctrine()
        
        doctrine.delete('cars', {}, many=True)
        logger.info("Cleared existing data from cars collection")
        
        inserted_ids = doctrine.insert('cars', data)
        
        return {
            "statusCode": 200,
            "message": "Data loaded successfully into MongoDB",
            "rows_inserted": len(inserted_ids) if isinstance(inserted_ids, list) else 1
        }
    except Exception as e:
        logger.error(f"Error during load: {e}")
        return {
            "statusCode": 500,
            "message": f"Error during load: {str(e)}"
        }