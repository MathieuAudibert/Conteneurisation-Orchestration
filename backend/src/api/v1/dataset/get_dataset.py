from typing import Any, Hashable
from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/api/v1/dataset", tags=["dataset"])

@router.get("/")
def get_router() -> list[dict[Hashable, Any]]:
    df = pd.read_csv(filepath_or_buffer="cfg/dataset-cars-dirty.csv")
    return df.fillna("").to_dict(orient="records")