__version__ = "1.0"
__description__ = "Module backend avec les classes pour les voitures et les logs"

from .classes.logs import Logs
from .classes.cars import Cars
from backend import Cars, Logs

__all__ = ['Cars', 'Logs']