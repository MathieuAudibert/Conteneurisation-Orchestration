from pathlib import Path
import os
from typing import Any
import pandas as pd
from datetime import datetime
from backend.src.core.logger import get_logger
from backend.src.core.classes.cars import Cars, TransmissionType, FuelType
from backend.src.core.classes.logs import Logs

logger = get_logger(__name__)

def _resolve_path(file_path: str) -> Path:
    p = Path(file_path)
    if p.is_absolute():
        return p

    data_dir = os.environ.get("DATA_DIR")
    if data_dir:
        return (Path(data_dir) / file_path).resolve()

    project_root = Path(__file__).resolve().parents[2]

    fp = Path(file_path)
    if fp.parts and fp.parts[0] == "cfg":
        return (project_root / fp).resolve()
    else:
        return (project_root / "cfg" / fp).resolve()

def _parse_ownership(value: Any) -> int:
    if pd.isna(value):
        return 0
    if isinstance(value, int):
        return value
    value_str = str(value).lower()
    if '1st' in value_str:
        return 1
    elif '2nd' in value_str:
        return 2
    elif '3rd' in value_str:
        return 3
    elif '4th' in value_str:
        return 4
    return int(value) if value else 0

def _parse_fuel_type(value: Any) -> FuelType:
    if pd.isna(value) or str(value).upper() in ['NAN', 'CNG']:
        return FuelType.PETROL 
    try:
        return FuelType[str(value).upper()]
    except KeyError:
        logger.warning(f"Unknown fuel type '{value}', defaulting to PETROL")
        return FuelType.PETROL

def extract(file_path: str) -> list[Cars]:
    logger.info(f"[INFO]: Début de l'extraction des données depuis {file_path}")
    try:
        path = _resolve_path(file_path)
        logger.debug(f"[INFO]: Chemin résolu pour l'extraction : {path}")
        df = pd.read_csv(path)
        
        cars = []
        logs = []
        
        for _, row in df.iterrows():
            try:
                car = Cars(
                    _brand=str(row.get('brand', '')),
                    _model=str(row.get('model', '')),
                    _full_model_name=str(row.get('full_model_name', '')),
                    _transmission=TransmissionType[str(row.get('transmission', 'MANUAL')).upper()],
                    _fuel_type=_parse_fuel_type(row.get('fuel_type')),
                    _make_year=str(row.get('make_year', '')),
                    _reg_year=str(row.get('reg_year', '')),
                    _engine_capacity_cc=int(row.get('engine_capacity_cc', 0)),
                    _engine_category=str(row.get('engine_category', '')),
                    _km_driven=int(row.get('km_driven', 0)),
                    _usage_category=str(row.get('usage_category', '')),
                    _ownership=_parse_ownership(row.get('ownership')),
                    _ownership_category=str(row.get('ownership_category', '')),
                    _price=int(row.get('price', 0)),
                    _overall_cost=int(row.get('overall_cost', 0)),
                    _total_value=int(row.get('total_value', 0)),
                    _price_category=str(row.get('price_category', '')),
                    _has_insurance=bool(row.get('has_insurance', False)),
                    _spare_key=bool(row.get('spare_key', False)),
                    _ready_for_sale=bool(row.get('ready_for_sale', False)),
                    _reg_number=str(row.get('reg_number', '')),
                    _title=str(row.get('title', '')),
                    _age_of_car=int(row.get('age_of_car', 0)),
                    _usage_efficency=int(row.get('usage_efficency', 0)),
                    _is_old_car=bool(row.get('is_old_car', False)),
                    _is_expensive=bool(row.get('is_expensive', False)),
                    _well_maintened=bool(row.get('well_maintened', False)),
                    _economy_score=float(row.get('economy_score', 0.0)),
                    _Cars__created_at=datetime.now()
                )
                cars.append(car)
            
                log = Logs(
                    _Logs__created_at=datetime.now(),
                    _Logs__timestamp=datetime.now(),
                    _user_id=0,
                    _action="car_extracted",
                    _metadata=f"Extracted car: {car.brand} {car.model}"
                )
                logs.append(log)
            
            except Exception as e:
                logger.warning(f"[WARNING]: Erreur lors de la création d'une instance Car : {e}")
                continue

        logger.info(f"[INFO]: Extraction réussie : {len(cars)} lignes extraites.")
        return cars
    except Exception as e:
        logger.error(f"[ERROR]: Erreur lors de l'extraction des données depuis {file_path} : {e}")
        raise