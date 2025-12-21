__version__ = "3.2"
__description__ = "Module qui gere la bdd"

from .classes.connect import ConnectDB
from .classes.doctrine import Doctrine

__all__ = ['ConnectDB', 'Doctrine']