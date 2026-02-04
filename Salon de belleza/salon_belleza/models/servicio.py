# salon_belleza/models/servicio.py
"""
Modelo de Servicio - representa un servicio ofrecido por el salón.
"""
from typing import List, Dict, Any

class Servicio:
    """Servicio ofrecido por el salón."""
    
    def __init__(self,
                 id: int,
                 nombre: str,
                 duracion_minutos: int,
                 precio_base: float,
                 categoria: str,
                 requiere_camilla: bool = False,
                 profesionales_posibles: List[int] = None,
                 descripcion: str = ""):
        
        self.id = id
        self.nombre = nombre
        self.duracion_minutos = duracion_minutos
        self.precio_base = precio_base
        self.categoria = categoria
        self.requiere_camilla = requiere_camilla
        self.profesionales_posibles = profesionales_posibles or []
        self.descripcion = descripcion
        
        self._validar()
    
    def _validar(self):
        """Valida los datos del servicio."""
        if self.id < 1:
            raise ValueError("ID debe ser mayor a 0")
        
        if not self.nombre.strip():
            raise ValueError("Nombre es obligatorio")
        
        if self.duracion_minutos <= 0:
            raise ValueError("Duración debe ser mayor a 0 minutos")
        
        if self.precio_base < 0:
            raise ValueError("Precio no puede ser negativo")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte a diccionario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "duracion_minutos": self.duracion_minutos,
            "precio_base": self.precio_base,
            "categoria": self.categoria,
            "requiere_camilla": self.requiere_camilla,
            "profesionales_posibles": self.profesionales_posibles,
            "descripcion": self.descripcion
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Servicio':
        """Crea un Servicio desde diccionario."""
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            duracion_minutos=data["duracion_minutos"],
            precio_base=data["precio_base"],
            categoria=data["categoria"],
            requiere_camilla=data.get("requiere_camilla", False),
            profesionales_posibles=data.get("profesionales_posibles", []),
            descripcion=data.get("descripcion", "")
        )
    
    def __str__(self) -> str:
        """Representación legible."""
        return f"{self.nombre} ({self.duracion_minutos}min - ${self.precio_base})"
    
    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"<Servicio id={self.id} nombre={self.nombre}>"

print("✅ Clase 'Servicio' definida")