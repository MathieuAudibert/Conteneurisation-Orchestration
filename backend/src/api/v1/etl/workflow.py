from fastapi import APIRouter

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/workflow")
def run_workflow():
    pass