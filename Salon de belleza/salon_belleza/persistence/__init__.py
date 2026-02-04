# salon_belleza/persistence/__init__.py
"""
Módulo de persistencia de datos (JSON).
"""

from .json_storage import JSONStorage
from .turno_repository import TurnoRepository

__all__ = ['JSONStorage', 'TurnoRepository']

print("✅ Módulo 'persistence' cargado con clases: JSONStorage, TurnoRepository")