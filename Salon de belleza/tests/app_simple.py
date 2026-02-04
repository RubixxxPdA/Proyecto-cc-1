# app_simple.py - Versión sin Plotly
"""
Aplicación Streamlit SIMPLIFICADA para el Sistema de Gestión de Salón de Belleza
NO requiere Plotly
"""
import streamlit as st
import sys
import os
from datetime import datetime, timedelta, date
import pandas as pd

# Agregar el directorio actual al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configuración de la página
st.set_page_config(
    page_title="Salón de Belleza - Sistema de Gestión",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.markdown("""
    <h1 style='text-align: center; color: #FF6B8B;'>
        💅 Sistema de Gestión - Salón de Belleza
    </h1>
""", unsafe_allow_html=True)

# Inicializar el sistema
@st.cache_resource
def inicializar_sistema():
    """Inicializa el sistema y lo mantiene en cache."""
    try:
        from salon_belleza.core.sistema_salon import SistemaSalon
        sistema = SistemaSalon()
        return sistema
    except Exception as e:
        st.error(f"Error al inicializar el sistema: {e}")
        return None

# Inicializar sistema
sistema = inicializar_sistema()

if sistema is None:
    st.stop()

# Menú lateral
st.sidebar.markdown("## 📊 Navegación")

menu = st.sidebar.radio(
    "Seleccione una sección:",
    ["🏠 Dashboard", "📅 Crear Turno", "👥 Gestión de Turnos", "💅 Servicios", 
     "👩‍💼 Profesionales", "📈 Estadísticas", "⚙️ Configuración"]
)

# Función para mostrar fecha y hora actual
def mostrar_encabezado():
    """Muestra el encabezado con información actual."""
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"### 📍 **Salón de Belleza - Gestión Inteligente**")
    
    with col2:
        hoy = datetime.now().strftime("%d/%m/%Y")
        st.metric("📅 Hoy", hoy)
    
    with col3:
        turnos_hoy = len(sistema.obtener_turnos(fecha=datetime.now().strftime("%Y-%m-%d")))
        st.metric("🎯 Turnos Hoy", turnos_hoy)

# Función para mostrar dashboard
def mostrar_dashboard():
    """Muestra el dashboard principal."""
    mostrar_encabezado()
    
    st.markdown("---")
    
    # Estadísticas rápidas
    col1, col2, col3, col4 = st.columns(4)
    
    stats = sistema.obtener_estadisticas()
    
    with col1:
        st.metric(
            "📋 Total Turnos",
            stats['total_turnos'],
            f"{stats['turnos_futuros']} futuros"
        )
    
    with col2:
        st.metric(
            "✅ Confirmados",
            stats['estados'].get('confirmado', 0),
            delta=None
        )
    
    with col3:
        st.metric(
            "⏳ Pendientes",
            stats['estados'].get('pendiente', 0),
            delta=None
        )
    
    with col4:
        st.metric(
            "👩‍💼 Profesionales",
            stats['profesionales_activos'],
            delta=None
        )
    
    st.markdown("---")
    
    # Dos columnas principales
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de turnos por estado
        st.subheader("📊 Turnos por Estado")
        
        # Mostrar como métricas con colores
        estados = stats['estados']
        
        # Crear columnas dinámicamente
        cols_estados = st.columns(len(estados))
        
        for idx, (estado, cantidad) in enumerate(estados.items()):
            with cols_estados[idx]:
                color = {
                    'pendiente': '#FFA726',
                    'confirmado': '#66BB6A',
                    'completado': '#42A5F5',
                    'cancelado': '#EF5350'
                }.get(estado, '#000000')
                
                st.markdown(f"""
                    <div style='background-color: {color}20; padding: 10px; border-radius: 5px; 
                                text-align: center; border-left: 4px solid {color}; margin-bottom: 10px;'>
                        <h4 style='margin: 0; color: {color}; text-transform: uppercase;'>{estado}</h4>
                        <h2 style='margin: 5px 0; color: {color};'>{cantidad}</h2>
                    </div>
                """, unsafe_allow_html=True)
    
    with col2:
        # Turnos de hoy
        st.subheader("📅 Turnos de Hoy")
        
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        turnos_hoy = sistema.obtener_turnos(fecha=fecha_hoy)
        
        if turnos_hoy:
            # Crear tarjetas para cada turno
            for turno in turnos_hoy[:5]:  # Mostrar máximo 5
                servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
                servicio_nombre = servicio.nombre if servicio else "N/A"
                
                profesional_nombre = "Por asignar"
                if turno.profesional_id:
                    profesional = sistema.obtener_profesional_por_id(turno.profesional_id)
                    profesional_nombre = profesional['nombre'] if profesional else "N/A"
                
                # Color según estado
                color_estado = {
                    'pendiente': '#FFA726',
                    'confirmado': '#66BB6A',
                    'completado': '#42A5F5',
                    'cancelado': '#EF5350'
                }.get(turno.estado, '#000000')
                
                st.markdown(f"""
                    <div style='border: 1px solid #ddd; border-radius: 8px; padding: 12px; 
                                margin-bottom: 10px; border-left: 4px solid {color_estado};'>
                        <div style='display: flex; justify-content: space-between;'>
                            <div>
                                <strong>{turno.cliente_nombre}</strong>
                                <br>
                                <small>🕒 {turno.hora} | 💅 {servicio_nombre[:20]}</small>
                            </div>
                            <div style='text-align: right;'>
                                <small>👩‍💼 {profesional_nombre}</small>
                                <br>
                                <small style='color: {color_estado};'><strong>{turno.estado}</strong></small>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            if len(turnos_hoy) > 5:
                st.info(f"*Y {len(turnos_hoy) - 5} turnos más...*")
        else:
            st.info("🎉 ¡No hay turnos programados para hoy!")
    
    st.markdown("---")
    
    # Próximos turnos (7 días)
    st.subheader("📅 Próximos Turnos (7 días)")
    
    # Obtener turnos de los próximos 7 días
    proximos_turnos = []
    for i in range(7):
        fecha = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        turnos_dia = sistema.obtener_turnos(fecha=fecha)
        
        for turno in turnos_dia:
            servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
            servicio_nombre = servicio.nombre if servicio else "N/A"
            
            proximos_turnos.append({
                'Fecha': fecha,
                'Hora': turno.hora,
                'Cliente': turno.cliente_nombre,
                'Servicio': servicio_nombre,
                'Estado': turno.estado
            })
    
    if proximos_turnos:
        df_proximos = pd.DataFrame(proximos_turnos)
        df_proximos = df_proximos.sort_values(['Fecha', 'Hora'])
        
        # Mostrar como tabla
        st.dataframe(
            df_proximos,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Fecha": st.column_config.DateColumn("📅 Fecha"),
                "Hora": st.column_config.TextColumn("🕒 Hora"),
                "Cliente": st.column_config.TextColumn("👤 Cliente"),
                "Servicio": st.column_config.TextColumn("💅 Servicio"),
                "Estado": st.column_config.TextColumn("📊 Estado")
            }
        )
    else:
        st.info("📭 No hay turnos programados para los próximos 7 días")

# NOTA: Las funciones restantes son las mismas que en la versión original
# pero sin usar Plotly. Te recomiendo usar la versión adaptada anterior.

# Función principal
def main():
    """Función principal de la aplicación Streamlit."""
    
    if menu == "🏠 Dashboard":
        mostrar_dashboard()
    else:
        st.info("🔧 Esta sección está en desarrollo. Primero usa el Dashboard.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()