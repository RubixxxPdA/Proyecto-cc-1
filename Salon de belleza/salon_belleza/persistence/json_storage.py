# salon_belleza/persistence/json_storage.py
"""
Clase base para almacenamiento en JSON.
"""
import json
import os
from typing import List, Dict, Any, Optional
from pathlib import Path

class JSONStorage:
    """Maneja lectura/escritura segura de archivos JSON."""
    
    def __init__(self, file_path: str):
        """
        Inicializa el almacenamiento.
        
        Args:
            file_path: Ruta al archivo JSON
        """
        self.file_path = Path(file_path)
        
        # Crear directorio si no existe
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Crear archivo si no existe
        if not self.file_path.exists():
            self._guardar([])
    
    def _cargar(self) -> List[Dict[str, Any]]:
        """Carga todos los datos del archivo."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Si el archivo está corrupto o no existe, devolver lista vacía
            return []
    
    def _guardar(self, data: List[Dict[str, Any]]):
        """Guarda datos en el archivo."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def obtener_todos(self) -> List[Dict[str, Any]]:
        """Obtiene todos los registros."""
        return self._cargar()
    
    def agregar(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Agrega un nuevo registro."""
        data = self._cargar()
        
        # Generar ID si no tiene
        if "id" not in item or not item["id"]:
            # Encontrar máximo ID
            max_id = 0
            for d in data:
                try:
                    item_id = int(d.get("id", 0))
                    max_id = max(max_id, item_id)
                except (ValueError, TypeError):
                    pass
            
            item["id"] = max_id + 1
        
        data.append(item)
        self._guardar(data)
        return item
    
    def buscar_por_id(self, item_id: Any) -> Optional[Dict[str, Any]]:
        """Busca un registro por ID."""
        data = self._cargar()
        
        for item in data:
            if str(item.get("id")) == str(item_id):
                return item
        
        return None
    
    def actualizar(self, item_id: Any, nuevos_datos: Dict[str, Any]) -> bool:
        """Actualiza un registro."""
        data = self._cargar()
        encontrado = False
        
        for i, item in enumerate(data):
            if str(item.get("id")) == str(item_id):
                # Actualizar campos (excepto ID)
                for key, value in nuevos_datos.items():
                    if key != "id":  # No cambiar el ID
                        item[key] = value
                encontrado = True
                break
        
        if encontrado:
            self._guardar(data)
        
        return encontrado
    
    def eliminar(self, item_id: Any) -> bool:
        """Elimina un registro por ID."""
        data = self._cargar()
        nueva_data = []
        eliminado = False
        
        for item in data:
            if str(item.get("id")) == str(item_id):
                eliminado = True
            else:
                nueva_data.append(item)
        
        if eliminado:
            self._guardar(nueva_data)
        
        return eliminado
    
    def contar(self) -> int:
        """Cuenta el número de registros."""
        return len(self._cargar())
    
    def buscar_por_campo(self, campo: str, valor: Any) -> List[Dict[str, Any]]:
        """Busca registros por campo y valor."""
        data = self._cargar()
        resultados = []
        
        for item in data:
            if item.get(campo) == valor:
                resultados.append(item)
        
        return resultados

print("✅ Clase 'JSONStorage' definida")