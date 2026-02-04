# prueba_intermedia.py
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("="*60)
print("PRUEBA INTERMEDIA - Verificación de estructura")
print("="*60)

# 1. Verificar que podemos importar el paquete
try:
    import salon_belleza
    print("✅ 1. Paquete 'salon_belleza' importado")
except ImportError as e:
    print(f"❌ 1. Error importando paquete: {e}")
    sys.exit(1)

# 2. Verificar modelos
try:
    from salon_belleza.models import Turno, Servicio
    print("✅ 2. Modelos 'Turno' y 'Servicio' importados")
    
    # Probar crear instancias
    turno = Turno("Cliente Test", "2024-01-20", "10:00", 1)
    print(f"✅   Turno creado: {turno}")
    
    servicio = Servicio(1, "Servicio Test", 60, 10.0, "Test")
    print(f"✅   Servicio creado: {servicio}")
    
except ImportError as e:
    print(f"❌ 2. Error importando modelos: {e}")

# 3. Verificar JSONStorage
try:
    from salon_belleza.persistence.json_storage import JSONStorage
    print("✅ 3. 'JSONStorage' importado")
    
    # Probar instancia
    storage = JSONStorage("data/turnos.json")
    print(f"✅   JSONStorage creado. Registros: {storage.contar()}")
    
except ImportError as e:
    print(f"❌ 3. Error importando JSONStorage: {e}")

# 4. Verificar archivos JSON
print("\n📂 Verificando archivos JSON en data/:")
json_files = ["servicios.json", "profesionales.json", "turnos.json", "config.json"]

for file in json_files:
    path = os.path.join("data", file)
    if os.path.exists(path):
        print(f"✅   {file} existe")
    else:
        print(f"❌   {file} NO existe")

print("\n" + "="*60)
print("PRUEBA COMPLETADA")
print("="*60)