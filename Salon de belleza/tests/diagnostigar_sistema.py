# diagnosticar_sistema.py
"""
Diagnóstico del SistemaSalon actual
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("="*60)
print("DIAGNÓSTICO DEL SISTEMA SALON")
print("="*60)

try:
    # 1. Importar el sistema
    from salon_belleza.core.sistema_salon import SistemaSalon
    print("✅ SistemaSalon importado")
    
    # 2. Crear instancia
    sistema = SistemaSalon()
    print("✅ Instancia creada")
    
    # 3. Ver qué métodos tiene
    print("\n📋 MÉTODOS DISPONIBLES:")
    metodos = [m for m in dir(sistema) if not m.startswith('_')]
    for metodo in sorted(metodos):
        print(f"  • {metodo}")
    
    # 4. Probar métodos específicos
    print("\n🧪 PROBANDO MÉTODOS CLAVE:")
    
    # Intentar obtener servicios
    try:
        servicios = sistema.obtener_servicios()
        print(f"  ✅ obtener_servicios(): {len(servicios) if servicios else 'None'} servicios")
    except Exception as e:
        print(f"  ❌ obtener_servicios(): Error - {e}")
    
    # Intentar obtener profesionales
    try:
        profesionales = sistema.obtener_profesionales()
        print(f"  ✅ obtener_profesionales(): {len(profesionales) if profesionales else 'None'} profesionales")
    except Exception as e:
        print(f"  ❌ obtener_profesionales(): Error - {e}")
    
    # Intentar obtener turnos
    try:
        turnos = sistema.obtener_turnos()
        print(f"  ✅ obtener_turnos(): {len(turnos) if turnos else 'None'} turnos")
    except Exception as e:
        print(f"  ❌ obtener_turnos(): Error - {e}")
    
    # Intentar obtener estadísticas
    try:
        stats = sistema.obtener_estadisticas()
        print(f"  ✅ obtener_estadisticas(): OK")
    except Exception as e:
        print(f"  ❌ obtener_estadisticas(): Error - {e}")
    
    # 5. Verificar estructura interna
    print("\n🔍 ESTRUCTURA INTERNA:")
    try:
        print(f"  • data_dir: {sistema.data_dir if hasattr(sistema, 'data_dir') else 'No tiene'}")
        print(f"  • calendario: {'✅' if hasattr(sistema, 'calendario') else '❌'}")
        print(f"  • turno_repository: {'✅' if hasattr(sistema, 'turno_repository') else '❌'}")
    except:
        print("  ❌ No se pudo verificar estructura")
    
    print("\n" + "="*60)
    print("DIAGNÓSTICO COMPLETADO")
    print("="*60)
    
except Exception as e:
    print(f"\n❌ ERROR GENERAL: {e}")
    import traceback
    traceback.print_exc()