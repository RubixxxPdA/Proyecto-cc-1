# salon_belleza/persistence/turno_repository.py
"""
Repositorio específico para manejar turnos.
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from ..models.turno import Turno
from .json_storage import JSONStorage

class TurnoRepository:
    """Repositorio especializado para turnos."""
    
    def __init__(self, data_dir: str = "data"):
        """
        Inicializa el repositorio de turnos.
        
        Args:
            data_dir: Directorio donde están los archivos JSON
        """
        self.turnos_storage = JSONStorage(f"{data_dir}/turnos.json")
        self.servicios_storage = JSONStorage(f"{data_dir}/servicios.json")
        self.profesionales_storage = JSONStorage(f"{data_dir}/profesionales.json")
    
    def crear_turno(self, turno: Turno) -> Turno:
        """
        Crea un nuevo turno.
        
        Args:
            turno: Objeto Turno a crear
            
        Returns:
            El turno creado con ID asignado
        """
        # Validar que el servicio existe
        servicio_data = self.servicios_storage.buscar_por_id(turno.servicio_id)
        if not servicio_data:
            raise ValueError(f"Servicio con ID {turno.servicio_id} no existe")
        
        # Si hay profesional, validar que existe
        if turno.profesional_id:
            profesional_data = self.profesionales_storage.buscar_por_id(turno.profesional_id)
            if not profesional_data:
                raise ValueError(f"Profesional con ID {turno.profesional_id} no existe")
        
        # Asignar timestamp de registro
        turno.timestamp_registro = datetime.now().isoformat()
        
        # Convertir a diccionario y guardar
        turno_dict = turno.to_dict()
        resultado = self.turnos_storage.agregar(turno_dict)
        
        # Actualizar el ID en el objeto
        turno.id = resultado["id"]
        return turno
    
    def obtener_turno(self, turno_id: str) -> Optional[Turno]:
        """
        Obtiene un turno por ID.
        
        Args:
            turno_id: ID del turno
            
        Returns:
            Turno o None si no existe
        """
        turno_data = self.turnos_storage.buscar_por_id(turno_id)
        if not turno_data:
            return None
        
        return Turno.from_dict(turno_data)
    
    def obtener_todos_turnos(self) -> List[Turno]:
        """
        Obtiene todos los turnos.
        
        Returns:
            Lista de todos los turnos
        """
        turnos_data = self.turnos_storage.obtener_todos()
        return [Turno.from_dict(data) for data in turnos_data]
    
    def obtener_turnos_por_fecha(self, fecha: str) -> List[Turno]:
        """
        Obtiene turnos para una fecha específica.
        
        Args:
            fecha: Fecha en formato YYYY-MM-DD
            
        Returns:
            Lista de turnos para esa fecha
        """
        # Validar formato de fecha
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
        
        turnos_data = self.turnos_storage.buscar_por_campo("fecha", fecha)
        return [Turno.from_dict(data) for data in turnos_data]
    
    def obtener_turnos_por_profesional(self, profesional_id: int, fecha: Optional[str] = None) -> List[Turno]:
        """
        Obtiene turnos de un profesional.
        
        Args:
            profesional_id: ID del profesional
            fecha: (Opcional) Filtra por fecha específica
            
        Returns:
            Lista de turnos del profesional
        """
        # Validar que el profesional existe
        profesional_data = self.profesionales_storage.buscar_por_id(profesional_id)
        if not profesional_data:
            raise ValueError(f"Profesional con ID {profesional_id} no existe")
        
        todos_turnos = self.obtener_todos_turnos()
        
        turnos_profesional = [
            turno for turno in todos_turnos 
            if turno.profesional_id == profesional_id
        ]
        
        if fecha:
            # Validar formato de fecha
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
            
            turnos_profesional = [
                turno for turno in turnos_profesional
                if turno.fecha == fecha
            ]
        
        return turnos_profesional
    
    def actualizar_turno(self, turno_id: str, turno_actualizado: Turno) -> bool:
        """
        Actualiza un turno existente.
        
        Args:
            turno_id: ID del turno a actualizar
            turno_actualizado: Objeto Turno con los nuevos datos
            
        Returns:
            True si se actualizó, False si no se encontró
        """
        # Validar que el servicio existe
        servicio_data = self.servicios_storage.buscar_por_id(turno_actualizado.servicio_id)
        if not servicio_data:
            raise ValueError(f"Servicio con ID {turno_actualizado.servicio_id} no existe")
        
        # Si hay profesional, validar que existe
        if turno_actualizado.profesional_id:
            profesional_data = self.profesionales_storage.buscar_por_id(turno_actualizado.profesional_id)
            if not profesional_data:
                raise ValueError(f"Profesional con ID {turno_actualizado.profesional_id} no existe")
        
        # Convertir a diccionario (sin ID ya que no debe cambiar)
        turno_dict = turno_actualizado.to_dict()
        turno_dict.pop("id", None)  # No permitir cambiar el ID
        
        # Actualizar en el storage
        return self.turnos_storage.actualizar(turno_id, turno_dict)
    
    def eliminar_turno(self, turno_id: str) -> bool:
        """
        Elimina un turno.
        
        Args:
            turno_id: ID del turno a eliminar
            
        Returns:
            True si se eliminó, False si no se encontró
        """
        return self.turnos_storage.eliminar(turno_id)
    
    def cambiar_estado_turno(self, turno_id: str, nuevo_estado: str) -> bool:
        """
        Cambia el estado de un turno.
        
        Args:
            turno_id: ID del turno
            nuevo_estado: Nuevo estado (pendiente, confirmado, completado, cancelado)
            
        Returns:
            True si se actualizó, False si no se encontró
        """
        estados_validos = ["pendiente", "confirmado", "completado", "cancelado"]
        if nuevo_estado not in estados_validos:
            raise ValueError(f"Estado inválido. Use: {', '.join(estados_validos)}")
        
        return self.turnos_storage.actualizar(turno_id, {"estado": nuevo_estado})
    
    def contar_turnos_por_estado(self, estado: str = "pendiente") -> int:
        """
        Cuenta turnos por estado.
        
        Args:
            estado: Estado a filtrar
            
        Returns:
            Número de turnos con ese estado
        """
        turnos_data = self.turnos_storage.buscar_por_campo("estado", estado)
        return len(turnos_data)
    
    def existe_conflicto_horario(self, fecha: str, hora: str, duracion_minutos: int, 
                                profesional_id: Optional[int] = None, recurso: Optional[str] = None) -> bool:
        """
        Verifica si hay conflicto de horario.
        
        Args:
            fecha: Fecha del turno
            hora: Hora de inicio
            duracion_minutos: Duración en minutos
            profesional_id: (Opcional) ID del profesional
            recurso: (Opcional) Recurso (mesa_1, mesa_2, camilla)
            
        Returns:
            True si hay conflicto, False si está libre
        """
        # Obtener todos los turnos de esa fecha
        turnos_fecha = self.obtener_turnos_por_fecha(fecha)
        
        if not turnos_fecha:
            return False
        
        # Convertir hora de inicio a minutos desde medianoche
        hora_inicio_obj = datetime.strptime(hora, "%H:%M")
        inicio_minutos = hora_inicio_obj.hour * 60 + hora_inicio_obj.minute
        fin_minutos = inicio_minutos + duracion_minutos
        
        for turno in turnos_fecha:
            # Si hay profesional asignado, verificar conflictos del profesional
            if profesional_id and turno.profesional_id == profesional_id:
                # Calcular rango horario del turno existente
                turno_hora_obj = datetime.strptime(turno.hora, "%H:%M")
                turno_inicio = turno_hora_obj.hour * 60 + turno_hora_obj.minute
                
                # Obtener duración del servicio del turno existente
                servicio_data = self.servicios_storage.buscar_por_id(turno.servicio_id)
                if servicio_data:
                    turno_duracion = servicio_data.get("duracion_minutos", 60)
                else:
                    turno_duracion = 60
                
                turno_fin = turno_inicio + turno_duracion
                
                # Verificar superposición
                if (inicio_minutos < turno_fin and fin_minutos > turno_inicio):
                    return True
            
            # Si hay recurso asignado, verificar conflictos del recurso
            if recurso and turno.recurso == recurso:
                # Similar lógica para recursos
                turno_hora_obj = datetime.strptime(turno.hora, "%H:%M")
                turno_inicio = turno_hora_obj.hour * 60 + turno_hora_obj.minute
                
                servicio_data = self.servicios_storage.buscar_por_id(turno.servicio_id)
                if servicio_data:
                    turno_duracion = servicio_data.get("duracion_minutos", 60)
                else:
                    turno_duracion = 60
                
                turno_fin = turno_inicio + turno_duracion
                
                if (inicio_minutos < turno_fin and fin_minutos > turno_inicio):
                    return True
        
        return False

print("✅ Clase 'TurnoRepository' definida")