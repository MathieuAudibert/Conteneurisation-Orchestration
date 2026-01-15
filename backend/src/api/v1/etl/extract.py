from fastapi import APIRouter
from backend.src.etl.extract import extract

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/extract")
def run_extract():
    data = extract("cfg/dataset-cars-dirty.csv")
    return {"statusCode": 200, "message": "Data extracted successfully", "data": data}