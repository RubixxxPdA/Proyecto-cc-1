# salon_belleza/core/calendario.py
"""
Módulo de gestión de calendario y horarios.
"""
import json
import os
from datetime import datetime, timedelta, date
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path

class Calendario:
    """Gestión de horarios del salón."""
    
    def __init__(self, config_path: str = "data/config.json"):
        """
        Inicializa el calendario.
        
        Args:
            config_path: Ruta al archivo de configuración
        """
        self.config_path = Path(config_path)
        self._cargar_configuracion()
    
    def _cargar_configuracion(self):
        """Carga la configuración desde el archivo JSON."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Configuración por defecto
            print(f"⚠️  No se pudo cargar configuración: {e}. Usando valores por defecto.")
            self.config = {
                "horarios": {
                    "semana": {
                        "dias": ["lunes", "martes", "miércoles", "jueves", "viernes"],
                        "apertura": "09:00",
                        "cierre": "20:00"
                    },
                    "sabado": {
                        "dias": ["sábado"],
                        "apertura": "09:00",
                        "cierre": "18:00"
                    },
                    "domingo": {
                        "dias": ["domingo"],
                        "abre": False
                    },
                    "almuerzo": {
                        "inicio": "13:30",
                        "fin": "14:00",
                        "activo": True
                    }
                },
                "turnos": {
                    "intervalo_entre_turnos": 15,
                    "anticipacion_minima_horas": 2,
                    "anticipacion_maxima_dias": 30,
                    "max_turnos_dia": 25
                }
            }
    
    def esta_abierto(self, fecha_str: str) -> Tuple[bool, Optional[str]]:
        """
        Verifica si el salón está abierto en una fecha.
        
        Args:
            fecha_str: Fecha en formato YYYY-MM-DD
            
        Returns:
            Tuple (está_abierto, horario_apertura)
        """
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
        
        # Obtener día de la semana
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        dia_nombre = dias_semana[fecha.weekday()]
        
        # Verificar si es domingo
        if dia_nombre == "domingo":
            domingo_config = self.config["horarios"]["domingo"]
            if not domingo_config.get("abre", False):
                return False, None
        
        # Determinar horario según el día
        horarios = self.config["horarios"]
        
        # Verificar sábado
        if dia_nombre == "sábado" and "sabado" in horarios:
            sabado_config = horarios["sabado"]
            if dia_nombre in sabado_config.get("dias", []):
                return True, sabado_config.get("apertura", "09:00")
        
        # Para días de semana
        semana_config = horarios["semana"]
        if dia_nombre in semana_config.get("dias", []):
            return True, semana_config.get("apertura", "09:00")
        
        return False, None
    
    def obtener_horario_cierre(self, fecha_str: str) -> Optional[str]:
        """
        Obtiene la hora de cierre para una fecha.
        
        Args:
            fecha_str: Fecha en formato YYYY-MM-DD
            
        Returns:
            Hora de cierre o None si está cerrado
        """
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
        
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        dia_nombre = dias_semana[fecha.weekday()]
        
        horarios = self.config["horarios"]
        
        if dia_nombre == "sábado" and "sabado" in horarios:
            return horarios["sabado"].get("cierre", "18:00")
        
        if dia_nombre in horarios["semana"].get("dias", []):
            return horarios["semana"].get("cierre", "20:00")
        
        return None
    
    def obtener_horarios_disponibles(self, fecha_str: str, duracion_minutos: int = 60) -> List[str]:
        """
        Genera lista de horarios disponibles para una fecha.
        
        Args:
            fecha_str: Fecha en formato YYYY-MM-DD
            duracion_minutos: Duración del servicio en minutos
            
        Returns:
            Lista de horarios disponibles (HH:MM)
        """
        # Verificar si está abierto
        abierto, apertura = self.esta_abierto(fecha_str)
        if not abierto:
            return []
        
        cierre = self.obtener_horario_cierre(fecha_str)
        if not cierre:
            return []
        
        # Convertir horarios a minutos
        apertura_min = self._hora_a_minutos(apertura)
        cierre_min = self._hora_a_minutos(cierre)
        
        # Obtener horario de almuerzo
        almuerzo_activo = self.config["horarios"]["almuerzo"].get("activo", True)
        if almuerzo_activo:
            almuerzo_inicio = self._hora_a_minutos(self.config["horarios"]["almuerzo"]["inicio"])
            almuerzo_fin = self._hora_a_minutos(self.config["horarios"]["almuerzo"]["fin"])
        
        # Intervalo entre turnos
        intervalo = self.config["turnos"]["intervalo_entre_turnos"]
        
        # Generar horarios
        horarios = []
        hora_actual = apertura_min
        
        while hora_actual + duracion_minutos <= cierre_min:
            # Verificar si está dentro del horario de almuerzo
            if almuerzo_activo:
                if hora_actual < almuerzo_fin and hora_actual + duracion_minutos > almuerzo_inicio:
                    hora_actual += intervalo
                    continue
            
            # Convertir a formato HH:MM
            horario_str = self._minutos_a_hora(hora_actual)
            horarios.append(horario_str)
            
            hora_actual += intervalo
        
        return horarios
    
    def validar_horario(self, fecha_str: str, hora_str: str, duracion_minutos: int) -> Tuple[bool, str]:
        """
        Valida si un horario es válido para el salón.
        
        Args:
            fecha_str: Fecha en formato YYYY-MM-DD
            hora_str: Hora en formato HH:MM
            duracion_minutos: Duración del servicio
            
        Returns:
            Tuple (válido, mensaje_error)
        """
        # Verificar fecha futura
        try:
            fecha_turno = datetime.strptime(fecha_str, "%Y-%m-%d")
            hoy = datetime.now()
            
            # Verificar anticipación mínima
            anticipacion_min_horas = self.config["turnos"]["anticipacion_minima_horas"]
            if fecha_turno.date() == hoy.date():
                # Si es hoy, verificar hora
                hora_turno = datetime.strptime(hora_str, "%H:%M")
                hora_actual = datetime.now()
                
                diferencia = hora_turno - hora_actual
                if diferencia.total_seconds() / 3600 < anticipacion_min_horas:
                    return False, f"Se requiere al menos {anticipacion_min_horas} horas de anticipación"
            
            # Verificar anticipación máxima
            anticipacion_max_dias = self.config["turnos"]["anticipacion_maxima_dias"]
            fecha_max = hoy + timedelta(days=anticipacion_max_dias)
            if fecha_turno > fecha_max:
                return False, f"No se pueden reservar turnos con más de {anticipacion_max_dias} días de anticipación"
        
        except ValueError as e:
            return False, f"Error en formato de fecha/hora: {e}"
        
        # Verificar si está abierto
        abierto, apertura = self.esta_abierto(fecha_str)
        if not abierto:
            return False, "El salón está cerrado ese día"
        
        # Obtener horarios disponibles
        horarios_disponibles = self.obtener_horarios_disponibles(fecha_str, duracion_minutos)
        
        # Verificar que la hora esté en los horarios disponibles
        if hora_str not in horarios_disponibles:
            return False, "Horario no disponible"
        
        return True, "Horario válido"
    
    @staticmethod
    def _hora_a_minutos(hora_str: str) -> int:
        """Convierte hora HH:MM a minutos desde medianoche."""
        try:
            hora_obj = datetime.strptime(hora_str, "%H:%M")
            return hora_obj.hour * 60 + hora_obj.minute
        except ValueError:
            return 540  # 9:00 AM por defecto
    
    @staticmethod
    def _minutos_a_hora(minutos: int) -> str:
        """Convierte minutos desde medianoche a formato HH:MM."""
        horas = minutos // 60
        mins = minutos % 60
        return f"{horas:02d}:{mins:02d}"
    
    def obtener_fechas_disponibles(self, dias_ahead: int = 30) -> List[Dict[str, Any]]:
        """
        Obtiene fechas disponibles para reservar.
        
        Args:
            dias_ahead: Número de días a futuro a considerar
            
        Returns:
            Lista de diccionarios con fecha y disponibilidad
        """
        fechas = []
        hoy = date.today()
        
        for i in range(dias_ahead):
            fecha = hoy + timedelta(days=i)
            fecha_str = fecha.strftime("%Y-%m-%d")
            
            abierto, _ = self.esta_abierto(fecha_str)
            
            fechas.append({
                "fecha": fecha_str,
                "abierto": abierto,
                "dia_semana": fecha.strftime("%A"),
                "dia_mes": fecha.day,
                "mes": fecha.strftime("%B")
            })
        
        return fechas

print("✅ Clase 'Calendario' definida")