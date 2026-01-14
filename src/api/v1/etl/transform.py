from fastapi import APIRouter

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/transform")
def run_transform():
    pass