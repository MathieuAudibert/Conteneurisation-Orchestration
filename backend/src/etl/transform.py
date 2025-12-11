import datetime
import logging
from typing import Optional

import pandas as pd

from log_config import get_logger
from extract import extract

def _to_bool(x):
    if pd.isna(x):
        return False
    if isinstance(x, bool):
        return x
    s = str(x).strip().lower()
    return s in {"true", "t", "yes", "y", "1"}

def _to_int_safe(x):
    if pd.isna(x):
        return None
    try:
        return int(str(x).replace(",", "").split(".")[0])
    except Exception:
        return None

def transform_cars(df: pd.DataFrame, logger: Optional[logging.Logger] = None) -> pd.DataFrame:
    logger = logger or get_logger(__name__)
    logger.info("Starting transformation")
    logger.debug("Initial shape: %s, columns: %s", df.shape, list(df.columns))

    df = df.copy()
    initial_rows = len(df)

    dropped_last = 0
    if initial_rows > 0 and df.iloc[-1].isna().all():
        df = df.iloc[:-1]
        dropped_last = 1
        logger.info("Dropped last row because it was all 'MISSING' values")

    if 'reg_year' in df.columns:
        df = df.drop(columns=['reg_year'])
        logger.info("Dropped column 'reg_year' : too many missing values")    

    if 'engine_capacity(CC)' in df.columns:
        before = df['engine_capacity(CC)'].notna().sum()
        df['engine_capacity_cc'] = df['engine_capacity(CC)'].apply(_to_int_safe)
        after = pd.Series(df['engine_capacity_cc']).notna().sum()
        df = df.drop(columns=['engine_capacity(CC)'])
        logger.info("Converted engine_capacity(CC) to engine_capacity_cc (%d -> %d non-null)", before, after)
    else:
        df['engine_capacity_cc'] = None