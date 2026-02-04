# salon_belleza/core/__init__.py
"""
Módulo core con la lógica principal del sistema.
"""

from .calendario import Calendario
from .sistema_salon import SistemaSalon

__all__ = ['Calendario', 'SistemaSalon']

print("✅ Módulo 'core' cargado con clases: Calendario, SistemaSalon")