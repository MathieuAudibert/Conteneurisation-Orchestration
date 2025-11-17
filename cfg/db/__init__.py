__version__ = "2.2"
__description__ = "Package to handle database"

from .classes.connect import ConnectDB
from db import ConnectDB

__all__ = ['ConnectDB']