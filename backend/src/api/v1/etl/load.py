from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])

@router.get("/load")
def run_load():
    pass