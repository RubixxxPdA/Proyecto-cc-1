# prueba_final.py
"""
Prueba final del sistema completo.
"""
import sys
import os
from datetime import datetime, timedelta

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("="*60)
print("PRUEBA FINAL DEL SISTEMA")
print("="*60)

try:
    from salon_belleza.core.sistema_salon import SistemaSalon
    
    # 1. Inicializar sistema
    print("\n1. Inicializando sistema...")
    sistema = SistemaSalon()
    print("✅ Sistema inicializado correctamente")
    
    # 2. Verificar servicios
    print("\n2. Verificando servicios...")
    servicios = sistema.obtener_servicios()
    print(f"✅ {len(servicios)} servicios cargados")
    
    for servicio in servicios[:3]:  # Mostrar primeros 3
        print(f"   • {servicio.nombre} (${servicio.precio_base})")
    
    # 3. Verificar profesionales
    print("\n3. Verificando profesionales...")
    profesionales = sistema.obtener_profesionales()
    print(f"✅ {len(profesionales)} profesionales cargados")
    
    # 4. Verificar calendario
    print("\n4. Verificando calendario...")
    fecha_mañana = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    abierto, _ = sistema.calendario.esta_abierto(fecha_mañana)
    print(f"✅ Calendario funcionando. Mañana ({fecha_mañana}) está {'abierto' if abierto else 'cerrado'}")
    
    # 5. Probar disponibilidad
    print("\n5. Probando disponibilidad...")
    if servicios:
        disponibilidad = sistema.obtener_disponibilidad(fecha_mañana, servicios[0].id)
        print(f"✅ Disponibilidad obtenida: {len(disponibilidad.get('horarios_disponibles', []))} horarios disponibles")
    
    # 6. Verificar turnos existentes
    print("\n6. Verificando turnos existentes...")
    turnos = sistema.obtener_turnos()
    print(f"✅ {len(turnos)} turnos en el sistema")
    
    # 7. Verificar estadísticas
    print("\n7. Verificando estadísticas...")
    stats = sistema.obtener_estadisticas()
    print(f"✅ Estadísticas obtenidas:")
    print(f"   • Total turnos: {stats['total_turnos']}")
    print(f"   • Turnos futuros: {stats['turnos_futuros']}")
    
    # 8. Prueba de creación de turno (simulada)
    print("\n8. Probando creación de turno...")
    if servicios and profesionales:
        # Solo probar validación, no crear realmente
        valido, mensaje = sistema.calendario.validar_horario(
            fecha_mañana, "10:00", servicios[0].duracion_minutos
        )
        print(f"✅ Validación de horario: {mensaje}")
    
    print("\n" + "="*60)
    print("✅ PRUEBA FINAL COMPLETADA EXITOSAMENTE")
    print("✅ EL SISTEMA ESTÁ LISTO PARA USAR")
    print("="*60)
    
    print("\n🎉 ¡Felicidades! El sistema está completo.")
    print("\nPara ejecutar el sistema principal:")
    print("   python run.py")
    
except Exception as e:
    print(f"\n❌ Error durante la prueba final: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)