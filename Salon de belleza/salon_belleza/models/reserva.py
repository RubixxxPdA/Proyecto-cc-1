# salon_belleza/models/reserva.py
"""
Modelo para reservas múltiples (varios servicios en un día).
"""
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from .turno import Turno

class ReservaMultiple:
    """Representa una reserva con múltiples servicios para un cliente."""
    
    def __init__(self, cliente_nombre: str, fecha: str, telefono: str = "", email: str = ""):
        self.id: Optional[str] = None
        self.cliente_nombre = cliente_nombre
        self.telefono = telefono
        self.email = email
        self.fecha = fecha
        self.turnos: List[Turno] = []
        self.estado = "pendiente"  # pendiente, confirmada, completada, cancelada
        self.timestamp_registro = datetime.now().isoformat()
        
    def agregar_turno(self, turno: Turno):
        """Agrega un turno a la reserva múltiple."""
        if turno.fecha != self.fecha:
            raise ValueError("Todos los turnos deben ser el mismo día")
        
        if turno.cliente_nombre != self.cliente_nombre:
            raise ValueError("Todos los turnos deben ser para el mismo cliente")
        
        self.turnos.append(turno)
    
    def calcular_duracion_total(self) -> int:
        """Calcula la duración total de todos los servicios."""
        return sum(turno.duracion_real or 0 for turno in self.turnos)
    
    def ordenar_turnos_por_hora(self):
        """Ordena los turnos por hora de inicio."""
        self.turnos.sort(key=lambda t: t.hora)
    
    def verificar_superposicion(self) -> bool:
        """Verifica si hay superposición entre los turnos."""
        self.ordenar_turnos_por_hora()
        
        for i in range(len(self.turnos) - 1):
            turno_actual = self.turnos[i]
            turno_siguiente = self.turnos[i + 1]
            
            # Calcular fin del turno actual
            hora_actual = datetime.strptime(turno_actual.hora, "%H:%M")
            duracion_actual = turno_actual.duracion_real or 60
            fin_actual = hora_actual + timedelta(minutes=duracion_actual)
            
            # Calcular inicio del siguiente turno
            hora_siguiente = datetime.strptime(turno_siguiente.hora, "%H:%M")
            
            if hora_siguiente < fin_actual:
                return True  # Hay superposición
        
        return False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte a diccionario."""
        return {
            "id": self.id,
            "cliente_nombre": self.cliente_nombre,
            "telefono": self.telefono,
            "email": self.email,
            "fecha": self.fecha,
            "turnos": [turno.to_dict() for turno in self.turnos],
            "estado": self.estado,
            "timestamp_registro": self.timestamp_registro
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ReservaMultiple':
        """Crea desde diccionario."""
        reserva = cls(
            cliente_nombre=data["cliente_nombre"],
            fecha=data["fecha"],
            telefono=data.get("telefono", ""),
            email=data.get("email", "")
        )
        
        reserva.id = data.get("id")
        reserva.estado = data.get("estado", "pendiente")
        reserva.timestamp_registro = data.get("timestamp_registro")
        
        # Reconstruir turnos
        from .turno import Turno
        for turno_data in data.get("turnos", []):
            turno = Turno.from_dict(turno_data)
            reserva.turnos.append(turno)
        
        return reserva
    
    def __str__(self) -> str:
        """Representación legible."""
        return f"Reserva múltiple: {self.cliente_nombre} - {self.fecha} ({len(self.turnos)} servicios)"

print("✅ Clase 'ReservaMultiple' definida")