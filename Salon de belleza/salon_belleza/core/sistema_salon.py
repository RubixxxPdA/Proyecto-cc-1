# salon_belleza/core/sistema_salon.py
"""
Sistema principal de gestión del salón de belleza.
"""
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from ..models.turno import Turno
from ..models.servicio import Servicio
from ..persistence.turno_repository import TurnoRepository
from ..persistence.json_storage import JSONStorage
from .calendario import Calendario

class SistemaSalon:
    """Sistema principal de gestión del salón."""
    
    def __init__(self, data_dir: str = "data"):
        """
        Inicializa el sistema del salón.
        
        Args:
            data_dir: Directorio donde están los archivos de datos
        """
        self.data_dir = data_dir
        
        # Inicializar componentes
        self.calendario = Calendario(f"{data_dir}/config.json")
        self.turno_repository = TurnoRepository(data_dir)
        
        # Cargar servicios y profesionales
        self._cargar_servicios()
        self._cargar_profesionales()
        
        print("✅ Sistema de salón inicializado")
    
    def _cargar_servicios(self):
        """Carga los servicios desde el archivo JSON."""
        servicios_storage = JSONStorage(f"{self.data_dir}/servicios.json")
        servicios_data = servicios_storage.obtener_todos()
        
        self.servicios = []
        for data in servicios_data:
            try:
                servicio = Servicio.from_dict(data)
                self.servicios.append(servicio)
            except Exception as e:
                print(f"⚠️  Error cargando servicio {data.get('id')}: {e}")
    
    def _cargar_profesionales(self):
        """Carga los profesionales desde el archivo JSON."""
        profesionales_storage = JSONStorage(f"{self.data_dir}/profesionales.json")
        self.profesionales = profesionales_storage.obtener_todos()
    
    def obtener_servicios(self) -> List[Servicio]:
        """
        Obtiene todos los servicios disponibles.
        
        Returns:
            Lista de servicios
        """
        return self.servicios
    
    def obtener_servicio_por_id(self, servicio_id: int) -> Optional[Servicio]:
        """
        Obtiene un servicio por ID.
        
        Args:
            servicio_id: ID del servicio
            
        Returns:
            Servicio o None si no existe
        """
        for servicio in self.servicios:
            if servicio.id == servicio_id:
                return servicio
        return None
    
    def obtener_profesionales(self, activos: bool = True) -> List[Dict[str, Any]]:
        """
        Obtiene todos los profesionales.
        
        Args:
            activos: Si True, solo devuelve profesionales activos
            
        Returns:
            Lista de profesionales
        """
        if activos:
            return [p for p in self.profesionales if p.get("activo", True)]
        return self.profesionales
    
    def obtener_profesional_por_id(self, profesional_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene un profesional por ID.
        
        Args:
            profesional_id: ID del profesional
            
        Returns:
            Profesional o None si no existe
        """
        for profesional in self.profesionales:
            if profesional.get("id") == profesional_id:
                return profesional
        return None
    
    def crear_turno(self, cliente_nombre: str, fecha: str, hora: str, servicio_id: int,
                   telefono: str = "", email: str = "", 
                   profesional_id: Optional[int] = None) -> Tuple[bool, str, Optional[Turno]]:
        """
        Crea un nuevo turno.
        
        Args:
            cliente_nombre: Nombre del cliente
            fecha: Fecha del turno (YYYY-MM-DD)
            hora: Hora del turno (HH:MM)
            servicio_id: ID del servicio
            telefono: Teléfono del cliente
            email: Email del cliente
            profesional_id: ID del profesional (opcional)
            
        Returns:
            Tuple (éxito, mensaje, turno_creado)
        """
        try:
            # Obtener servicio
            servicio = self.obtener_servicio_por_id(servicio_id)
            if not servicio:
                return False, f"Servicio con ID {servicio_id} no existe", None
            
            # Validar horario
            valido, mensaje = self.calendario.validar_horario(
                fecha, hora, servicio.duracion_minutos
            )
            
            if not valido:
                return False, mensaje, None
            
            # Verificar conflictos de horario si hay profesional
            if profesional_id:
                profesional = self.obtener_profesional_por_id(profesional_id)
                if not profesional:
                    return False, f"Profesional con ID {profesional_id} no existe", None
                
                # Verificar si el profesional puede hacer este servicio
                if servicio.id not in profesional.get("especialidades", []):
                    return False, f"El profesional no está especializado en este servicio", None
                
                # Determinar recurso
                recurso = None
                if servicio.requiere_camilla:
                    recurso = "camilla"
                else:
                    recurso = profesional.get("preferencia_recurso", "mesa_1")
                
                # Verificar conflicto horario
                conflicto = self.turno_repository.existe_conflicto_horario(
                    fecha, hora, servicio.duracion_minutos,
                    profesional_id=profesional_id, recurso=recurso
                )
                
                if conflicto:
                    return False, "El profesional ya tiene un turno en ese horario", None
            else:
                recurso = None
            
            # Verificar límite de turnos por día
            turnos_fecha = self.turno_repository.obtener_turnos_por_fecha(fecha)
            max_turnos = self.calendario.config["turnos"]["max_turnos_dia"]
            if len(turnos_fecha) >= max_turnos:
                return False, f"No hay disponibilidad para esa fecha (límite de {max_turnos} turnos)", None
            
            # Crear turno
            turno = Turno(
                cliente_nombre=cliente_nombre,
                fecha=fecha,
                hora=hora,
                servicio_id=servicio_id,
                telefono=telefono,
                email=email,
                profesional_id=profesional_id,
                recurso=recurso
            )
            
            # Guardar turno
            turno_creado = self.turno_repository.crear_turno(turno)
            
            return True, "Turno creado exitosamente", turno_creado
            
        except Exception as e:
            return False, f"Error al crear turno: {str(e)}", None
    
    def obtener_turnos(self, fecha: Optional[str] = None, 
                      profesional_id: Optional[int] = None) -> List[Turno]:
        """
        Obtiene turnos con filtros opcionales.
        
        Args:
            fecha: Filtrar por fecha (YYYY-MM-DD)
            profesional_id: Filtrar por profesional
            
        Returns:
            Lista de turnos
        """
        if fecha:
            return self.turno_repository.obtener_turnos_por_fecha(fecha)
        elif profesional_id:
            return self.turno_repository.obtener_turnos_por_profesional(profesional_id)
        else:
            return self.turno_repository.obtener_todos_turnos()
    
    def cancelar_turno(self, turno_id: str) -> Tuple[bool, str]:
        """
        Cancela un turno.
        
        Args:
            turno_id: ID del turno a cancelar
            
        Returns:
            Tuple (éxito, mensaje)
        """
        try:
            exito = self.turno_repository.cambiar_estado_turno(turno_id, "cancelado")
            if exito:
                return True, "Turno cancelado exitosamente"
            else:
                return False, "No se encontró el turno"
        except Exception as e:
            return False, f"Error al cancelar turno: {str(e)}"
    
    def confirmar_turno(self, turno_id: str) -> Tuple[bool, str]:
        """
        Confirma un turno.
        
        Args:
            turno_id: ID del turno a confirmar
            
        Returns:
            Tuple (éxito, mensaje)
        """
        try:
            exito = self.turno_repository.cambiar_estado_turno(turno_id, "confirmado")
            if exito:
                return True, "Turno confirmado exitosamente"
            else:
                return False, "No se encontró el turno"
        except Exception as e:
            return False, f"Error al confirmar turno: {str(e)}"
    
    def obtener_disponibilidad(self, fecha: str, servicio_id: int) -> Dict[str, Any]:
        """
        Obtiene disponibilidad para una fecha y servicio.
        
        Args:
            fecha: Fecha a consultar (YYYY-MM-DD)
            servicio_id: ID del servicio
            
        Returns:
            Diccionario con disponibilidad
        """
        servicio = self.obtener_servicio_por_id(servicio_id)
        if not servicio:
            return {"error": f"Servicio con ID {servicio_id} no existe"}
        
        # Verificar si está abierto
        abierto, _ = self.calendario.esta_abierto(fecha)
        if not abierto:
            return {
                "fecha": fecha,
                "abierto": False,
                "horarios_disponibles": [],
                "profesionales_disponibles": []
            }
        
        # Obtener horarios disponibles
        horarios = self.calendario.obtener_horarios_disponibles(fecha, servicio.duracion_minutos)
        
        # Filtrar profesionales disponibles para cada horario
        profesionales_disponibles = []
        
        for profesional in self.obtener_profesionales(activos=True):
            if servicio.id in profesional.get("especialidades", []):
                # Verificar disponibilidad del profesional para algún horario
                for horario in horarios:
                    conflicto = self.turno_repository.existe_conflicto_horario(
                        fecha, horario, servicio.duracion_minutos,
                        profesional_id=profesional["id"]
                    )
                    
                    if not conflicto:
                        profesionales_disponibles.append({
                            "id": profesional["id"],
                            "nombre": profesional["nombre"],
                            "especialidades": profesional.get("especialidades", []),
                            "color_calendario": profesional.get("color_calendario", "#000000")
                        })
                        break
        
        return {
            "fecha": fecha,
            "abierto": True,
            "horarios_disponibles": horarios,
            "profesionales_disponibles": profesionales_disponibles,
            "servicio": servicio.nombre,
            "duracion_minutos": servicio.duracion_minutos
        }
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas del sistema.
        
        Returns:
            Diccionario con estadísticas
        """
        todos_turnos = self.turno_repository.obtener_todos_turnos()
        
        # Contar por estado
        estados = {"pendiente": 0, "confirmado": 0, "completado": 0, "cancelado": 0}
        
        for turno in todos_turnos:
            estados[turno.estado] = estados.get(turno.estado, 0) + 1
        
        # Contar por servicio
        servicios_count = {}
        for turno in todos_turnos:
            servicio_id = turno.servicio_id
            servicios_count[servicio_id] = servicios_count.get(servicio_id, 0) + 1
        
        # Obtener fechas de turnos futuros
        hoy = datetime.now().date()
        turnos_futuros = []
        
        for turno in todos_turnos:
            try:
                fecha_turno = datetime.strptime(turno.fecha, "%Y-%m-%d").date()
                if fecha_turno >= hoy:
                    turnos_futuros.append(turno)
            except ValueError:
                continue
        
        return {
            "total_turnos": len(todos_turnos),
            "turnos_futuros": len(turnos_futuros),
            "estados": estados,
            "servicios": servicios_count,
            "profesionales_activos": len(self.obtener_profesionales(activos=True)),
            "servicios_disponibles": len(self.servicios)
        }

print("✅ Clase 'SistemaSalon' definida")