from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/etl", tags=["etl"])

@router.get("/workflow")
def run_workflow():
    pass