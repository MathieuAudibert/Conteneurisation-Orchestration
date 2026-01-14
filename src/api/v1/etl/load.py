from fastapi import APIRouter

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/load")
def run_load():
    pass