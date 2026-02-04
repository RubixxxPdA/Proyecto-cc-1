# run.py
"""
Punto de entrada principal del sistema de gestión de salón de belleza.
"""
import sys
import os
from salon_belleza.core.sistema_salon import SistemaSalon

def mostrar_menu_principal():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN - SALÓN DE BELLEZA")
    print("="*60)
    print("1. Crear nuevo turno")
    print("2. Ver turnos del día")
    print("3. Buscar disponibilidad")
    print("4. Cancelar turno")
    print("5. Ver estadísticas")
    print("6. Listar servicios")
    print("7. Listar profesionales")
    print("8. Salir")
    print("="*60)

def crear_turno_interactivo(sistema: SistemaSalon):
    """Guía interactiva para crear un turno."""
    print("\n--- CREAR NUEVO TURNO ---")
    
    # Mostrar servicios
    print("\nServicios disponibles:")
    servicios = sistema.obtener_servicios()
    for servicio in servicios:
        print(f"  {servicio.id}. {servicio.nombre} ({servicio.duracion_minutos}min - ${servicio.precio_base})")
    
    try:
        servicio_id = int(input("\nID del servicio: "))
        
        # Verificar disponibilidad para mañana por defecto
        from datetime import datetime, timedelta
        fecha_ejemplo = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        
        disponibilidad = sistema.obtener_disponibilidad(fecha_ejemplo, servicio_id)
        
        if not disponibilidad.get("abierto", False):
            print(f"\n⚠️  El salón está cerrado el {fecha_ejemplo}")
            return
        
        print(f"\nDisponibilidad para {fecha_ejemplo}:")
        print(f"Horarios: {', '.join(disponibilidad['horarios_disponibles'][:5])}...")
        
        fecha = input(f"Fecha ({fecha_ejemplo}): ") or fecha_ejemplo
        
        # Obtener horarios para la fecha seleccionada
        disponibilidad_real = sistema.obtener_disponibilidad(fecha, servicio_id)
        
        if not disponibilidad_real.get("abierto", False):
            print(f"❌ El salón está cerrado el {fecha}")
            return
        
        print(f"\nHorarios disponibles para {fecha}:")
        for i, hora in enumerate(disponibilidad_real["horarios_disponibles"], 1):
            print(f"  {i}. {hora}")
        
        hora_idx = int(input("\nSeleccione el número del horario: ")) - 1
        hora = disponibilidad_real["horarios_disponibles"][hora_idx]
        
        # Mostrar profesionales disponibles para ese horario
        print("\nProfesionales disponibles:")
        profesionales = disponibilidad_real.get("profesionales_disponibles", [])
        
        if profesionales:
            for prof in profesionales:
                print(f"  {prof['id']}. {prof['nombre']}")
            
            profesional_id = input("\nID del profesional (opcional, Enter para omitir): ")
            profesional_id = int(profesional_id) if profesional_id.strip() else None
        else:
            print("  ⚠️  No hay profesionales disponibles para este horario")
            profesional_id = None
        
        # Datos del cliente
        print("\nDatos del cliente:")
        cliente_nombre = input("Nombre completo: ")
        telefono = input("Teléfono (opcional): ")
        email = input("Email (opcional): ")
        
        # Confirmar
        print(f"\nResumen del turno:")
        print(f"  Cliente: {cliente_nombre}")
        print(f"  Fecha: {fecha} {hora}")
        servicio = sistema.obtener_servicio_por_id(servicio_id)
        print(f"  Servicio: {servicio.nombre if servicio else 'N/A'}")
        
        if profesional_id:
            profesional = sistema.obtener_profesional_por_id(profesional_id)
            print(f"  Profesional: {profesional['nombre'] if profesional else 'N/A'}")
        
        confirmar = input("\n¿Confirmar turno? (s/n): ").lower()
        
        if confirmar == 's':
            exito, mensaje, turno = sistema.crear_turno(
                cliente_nombre=cliente_nombre,
                fecha=fecha,
                hora=hora,
                servicio_id=servicio_id,
                telefono=telefono,
                email=email,
                profesional_id=profesional_id
            )
            
            if exito:
                print(f"\n✅ {mensaje}")
                print(f"   ID del turno: {turno.id}")
            else:
                print(f"\n❌ {mensaje}")
        else:
            print("\n❌ Turno cancelado")
            
    except (ValueError, IndexError) as e:
        print(f"\n❌ Error: {e}")
    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada por el usuario")

def ver_turnos_dia(sistema: SistemaSalon):
    """Muestra los turnos del día actual."""
    from datetime import datetime
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n--- TURNOS PARA HOY ({fecha_actual}) ---")
    
    turnos = sistema.obtener_turnos(fecha=fecha_actual)
    
    if not turnos:
        print("No hay turnos programados para hoy")
        return
    
    for i, turno in enumerate(turnos, 1):
        servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
        servicio_nombre = servicio.nombre if servicio else "N/A"
        
        profesional_nombre = "Por asignar"
        if turno.profesional_id:
            profesional = sistema.obtener_profesional_por_id(turno.profesional_id)
            profesional_nombre = profesional["nombre"] if profesional else "N/A"
        
        print(f"\n{i}. {turno.cliente_nombre}")
        print(f"   Hora: {turno.hora}")
        print(f"   Servicio: {servicio_nombre}")
        print(f"   Profesional: {profesional_nombre}")
        print(f"   Estado: {turno.estado}")
        print(f"   Teléfono: {turno.telefono}")

def buscar_disponibilidad(sistema: SistemaSalon):
    """Busca disponibilidad para un servicio."""
    print("\n--- BUSCAR DISPONIBILIDAD ---")
    
    # Mostrar servicios
    servicios = sistema.obtener_servicios()
    for servicio in servicios:
        print(f"{servicio.id}. {servicio.nombre}")
    
    try:
        servicio_id = int(input("\nID del servicio: "))
        
        from datetime import datetime, timedelta
        fecha_inicio = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        
        fecha = input(f"Fecha a consultar ({fecha_inicio}): ") or fecha_inicio
        
        disponibilidad = sistema.obtener_disponibilidad(fecha, servicio_id)
        
        if not disponibilidad.get("abierto", False):
            print(f"\n❌ El salón está cerrado el {fecha}")
            return
        
        print(f"\n📅 Disponibilidad para {fecha}:")
        print(f"Servicio: {disponibilidad.get('servicio', 'N/A')}")
        print(f"Duración: {disponibilidad.get('duracion_minutos', 0)} minutos")
        print(f"\nHorarios disponibles ({len(disponibilidad['horarios_disponibles'])}):")
        
        # Mostrar horarios en columnas
        horarios = disponibilidad["horarios_disponibles"]
        for i in range(0, len(horarios), 5):
            print("  " + "  ".join(horarios[i:i+5]))
        
        print(f"\nProfesionales disponibles ({len(disponibilidad['profesionales_disponibles'])}):")
        for prof in disponibilidad["profesionales_disponibles"]:
            print(f"  • {prof['nombre']}")
            
    except ValueError as e:
        print(f"\n❌ Error: {e}")

def cancelar_turno(sistema: SistemaSalon):
    """Cancela un turno existente."""
    print("\n--- CANCELAR TURNO ---")
    
    try:
        turno_id = input("ID del turno a cancelar: ")
        
        # Primero buscar el turno
        turno = sistema.turno_repository.obtener_turno(turno_id)
        
        if not turno:
            print("❌ No se encontró el turno")
            return
        
        print(f"\nTurno encontrado:")
        print(f"  Cliente: {turno.cliente_nombre}")
        print(f"  Fecha: {turno.fecha} {turno.hora}")
        
        servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
        print(f"  Servicio: {servicio.nombre if servicio else 'N/A'}")
        print(f"  Estado actual: {turno.estado}")
        
        confirmar = input("\n¿Está seguro de cancelar este turno? (s/n): ").lower()
        
        if confirmar == 's':
            exito, mensaje = sistema.cancelar_turno(turno_id)
            print(f"\n{'✅' if exito else '❌'} {mensaje}")
        else:
            print("\n❌ Cancelación abortada")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")

def mostrar_estadisticas(sistema: SistemaSalon):
    """Muestra estadísticas del sistema."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    
    stats = sistema.obtener_estadisticas()
    
    print(f"\n📊 Resumen general:")
    print(f"  Total de turnos: {stats['total_turnos']}")
    print(f"  Turnos futuros: {stats['turnos_futuros']}")
    print(f"  Servicios disponibles: {stats['servicios_disponibles']}")
    print(f"  Profesionales activos: {stats['profesionales_activos']}")
    
    print(f"\n📈 Turnos por estado:")
    for estado, cantidad in stats['estados'].items():
        print(f"  {estado.capitalize()}: {cantidad}")
    
    if stats['servicios']:
        print(f"\n🎯 Turnos por servicio:")
        for servicio_id, cantidad in stats['servicios'].items():
            servicio = sistema.obtener_servicio_por_id(servicio_id)
            nombre = servicio.nombre if servicio else f"ID {servicio_id}"
            print(f"  {nombre}: {cantidad}")

def listar_servicios(sistema: SistemaSalon):
    """Lista todos los servicios disponibles."""
    print("\n--- SERVICIOS DISPONIBLES ---")
    
    servicios = sistema.obtener_servicios()
    
    for servicio in servicios:
        print(f"\n{servicio.id}. {servicio.nombre}")
        print(f"   Categoría: {servicio.categoria}")
        print(f"   Duración: {servicio.duracion_minutos} minutos")
        print(f"   Precio base: ${servicio.precio_base}")
        print(f"   Requiere camilla: {'Sí' if servicio.requiere_camilla else 'No'}")
        
        if servicio.profesionales_posibles:
            print(f"   Profesionales posibles: {servicio.profesionales_posibles}")

def listar_profesionales(sistema: SistemaSalon):
    """Lista todos los profesionales."""
    print("\n--- PROFESIONALES ---")
    
    profesionales = sistema.obtener_profesionales()
    
    for prof in profesionales:
        estado = "Activo" if prof.get("activo", True) else "Inactivo"
        print(f"\n{prof['id']}. {prof['nombre']} ({estado})")
        print(f"   Especialidades: {prof.get('especialidades', [])}")
        print(f"   Preferencia de recurso: {prof.get('preferencia_recurso', 'N/A')}")
        print(f"   Recursos posibles: {prof.get('recursos_posibles', [])}")
        print(f"   Color en calendario: {prof.get('color_calendario', '#000000')}")

def main():
    """Función principal."""
    print("🚀 Inicializando Sistema de Gestión de Salón de Belleza...")
    
    try:
        # Inicializar sistema
        sistema = SistemaSalon()
        print("✅ Sistema cargado exitosamente")
        
        # Bucle principal
        while True:
            mostrar_menu_principal()
            
            try:
                opcion = input("\nSeleccione una opción (1-8): ")
                
                if opcion == "1":
                    crear_turno_interactivo(sistema)
                elif opcion == "2":
                    ver_turnos_dia(sistema)
                elif opcion == "3":
                    buscar_disponibilidad(sistema)
                elif opcion == "4":
                    cancelar_turno(sistema)
                elif opcion == "5":
                    mostrar_estadisticas(sistema)
                elif opcion == "6":
                    listar_servicios(sistema)
                elif opcion == "7":
                    listar_profesionales(sistema)
                elif opcion == "8":
                    print("\n👋 ¡Gracias por usar el sistema! Hasta pronto.")
                    break
                else:
                    print("\n❌ Opción no válida. Intente de nuevo.")
                
                input("\nPresione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Operación interrumpida por el usuario")
                continuar = input("¿Desea salir del sistema? (s/n): ").lower()
                if continuar == 's':
                    print("\n👋 ¡Hasta pronto!")
                    break
    
    except Exception as e:
        print(f"\n❌ Error fatal al inicializar el sistema: {e}")
        print("Verifique que todos los archivos necesarios existan.")
        input("\nPresione Enter para salir...")
        return 1
    
    return 0

if __name__ == "__main__":
    # Agregar el directorio actual al path para importaciones
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main())