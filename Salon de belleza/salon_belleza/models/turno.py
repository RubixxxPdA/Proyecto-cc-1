# salon_belleza/models/turno.py
"""
Modelo de Turno - representa una cita/reserva.
"""
from datetime import datetime
from typing import Optional, Dict, Any

class Turno:
    """Turno individual para un servicio."""
    
    def __init__(self, 
                 cliente_nombre: str,
                 fecha: str,           # "YYYY-MM-DD"
                 hora: str,            # "HH:MM"
                 servicio_id: int,
                 telefono: str = "",
                 email: str = "",
                 profesional_id: Optional[int] = None,
                 recurso: Optional[str] = None):
        
        # Datos del cliente
        self.id: Optional[str] = None
        self.cliente_nombre = cliente_nombre
        self.telefono = telefono
        self.email = email
        
        # Datos del turno
        self.fecha = fecha
        self.hora = hora
        self.servicio_id = servicio_id
        
        # Asignación
        self.profesional_id = profesional_id
        self.recurso = recurso
        
        # Estado
        self.estado = "pendiente"  # pendiente, confirmado, completado, cancelado
        self.timestamp_registro: Optional[str] = None
        
        # Datos internos (completados por el personal)
        self.precio_final: Optional[float] = None
        self.notas_internas = ""
        self.estado_pago = "pendiente"  # pendiente, pagado, parcial
        self.duracion_real: Optional[int] = None
        
        # Validación básica
        self._validar()
    
    def _validar(self):
        """Valida los datos básicos."""
        if not self.cliente_nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio")
        
        # Validar formato de fecha
        try:
            datetime.strptime(self.fecha, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
        
        # Validar formato de hora
        try:
            datetime.strptime(self.hora, "%H:%M")
        except ValueError:
            raise ValueError("Formato de hora inválido. Use HH:MM")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte a diccionario para guardar en JSON."""
        return {
            "id": self.id,
            "cliente_nombre": self.cliente_nombre,
            "telefono": self.telefono,
            "email": self.email,
            "fecha": self.fecha,
            "hora": self.hora,
            "servicio_id": self.servicio_id,
            "profesional_id": self.profesional_id,
            "recurso": self.recurso,
            "estado": self.estado,
            "timestamp_registro": self.timestamp_registro or datetime.now().isoformat(),
            "precio_final": self.precio_final,
            "notas_internas": self.notas_internas,
            "estado_pago": self.estado_pago,
            "duracion_real": self.duracion_real
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Turno':
        """Crea un Turno desde un diccionario."""
        turno = cls(
            cliente_nombre=data["cliente_nombre"],
            fecha=data["fecha"],
            hora=data["hora"],
            servicio_id=data["servicio_id"],
            telefono=data.get("telefono", ""),
            email=data.get("email", ""),
            profesional_id=data.get("profesional_id"),
            recurso=data.get("recurso")
        )
        
        # Asignar campos adicionales
        turno.id = data.get("id")
        turno.estado = data.get("estado", "pendiente")
        turno.timestamp_registro = data.get("timestamp_registro")
        turno.precio_final = data.get("precio_final")
        turno.notas_internas = data.get("notas_internas", "")
        turno.estado_pago = data.get("estado_pago", "pendiente")
        turno.duracion_real = data.get("duracion_real")
        
        return turno
    
    def __str__(self) -> str:
        """Representación legible."""
        return f"Turno: {self.cliente_nombre} - {self.fecha} {self.hora}"
    
    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"<Turno cliente={self.cliente_nombre} fecha={self.fecha} hora={self.hora}>"

print("✅ Clase 'Turno' definida")