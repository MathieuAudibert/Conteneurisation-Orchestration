__version__ = "2.1"
__description__ = "Package to handle database"

from .classes.connect import ConnectDb
from db import ConnectDb

__all__ = ['ConnectDb']