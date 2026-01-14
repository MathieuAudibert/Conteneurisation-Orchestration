from fastapi import APIRouter
from src.etl.extract import extract

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/load")
def run_load():
    data = extract("cfg/dataset-cars-dirty.csv")
    return {"status": "success", "message": "Data extracted successfully", "data": data}