from pathlib import Path
import os
import pandas as pd
from log_config import get_logger

logger = get_logger(__name__)

def _resolve_path(file_path):
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


def extract(file_path):
    logger.info(f"[INFO]: Début de l'extraction des données depuis {file_path}")
    try:
        path = _resolve_path(file_path)
        logger.debug(f"[INFO]: Chemin résolu pour l'extraction : {path}")
        cars = pd.read_csv(path)
        logger.info(f"[INFO]: Extraction réussie : {len(cars)} lignes extraites.")
        return cars
    except Exception as e:
        logger.error(f"[ERROR]: Erreur lors de l'extraction des données depuis {file_path} : {e}")
        raise


if __name__ == "__main__":
    default_file = os.environ.get("DEFAULT_FILE", "raw/pre-owned dataset-cars-dirty.csv")
    cars = extract(default_file)
    print(cars.head())