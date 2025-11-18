__version__ = "3.2"
__description__ = "Module qui gere la bdd"

from .classes.connect import ConnectDB
from .classes.doctrine.select import DoctrineSelect
from db import ConnectDB

__all__ = ['ConnectDB', 'DoctrineSelect']