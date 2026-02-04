"""
SALÓN DE BELLEZA - Sistema de Gestión
Interfaz Streamlit con diseño rosa minimalista y encantador
"""
import streamlit as st
import sys
import os
from datetime import datetime, timedelta, date
import pandas as pd

# Agregar el directorio actual al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ============================================
# CONFIGURACIÓN DE ESTILOS ROSA MINIMALISTA
# ============================================

def aplicar_estilos():
    """Aplica los estilos CSS personalizados."""
    st.markdown("""
    <style>
    /* Estilos generales */
    .main {
        background-color: #FFF5F7;
    }
    
    /* Sidebar estilizado */
    [data-testid="stSidebar"] {
        border-radius: 20px;
        background: #870847 ;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stButton button {
        background-color: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white !important;
        border-radius: 10px;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }
    
    /* Encabezados */
    h1 {
        color: white !important;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
                
      h2 {
        color: #870847 !important;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
      h3 {
        color: #870847 !important;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }      
                     
    /* Tarjetas elegantes */
    .tarjeta-rosa {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #870847;
        box-shadow: 0 4px 6px rgba(255, 105, 180, 0.1);
        transition: transform 0.3s ease;
    }
    
    .tarjeta-rosa:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(255, 105, 180, 0.2);
    }
    
    .tarjeta-lila {
        background: linear-gradient(135deg, #870847 0%, #870847 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        color: white;
    }
    
    /* Botones */
    .stButton button {
        background: linear-gradient(135deg, #870847 0%, #870847 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
    }
    
    /* Métricas */
    [data-testid="stMetric"] {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #FFB6C1;
    }
    
    [data-testid="stMetricLabel"] {
        color: #870847 !important;
        font-weight: bold;
    }
    
    [data-testid="stMetricValue"] {
        color: #870847 !important;
        font-size: 24px !important;
    }
    
    /* Dataframes */
    .dataframe {
        border-radius: 10px;
        border: 1px solid #FFB6C1;
    }
    
    /* Pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #870847;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: white;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #870847 !important;
        color: white !important;
    }
    
    /* Inputs */
    .stTextInput input, .stSelectbox select, .stDateInput input {
        border: 2px solid #FFB6C1 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    .stTextInput input:focus, .stSelectbox select:focus, .stDateInput input:focus {
        border-color: #870847 !important;
        box-shadow: 0 0 0 2px rgba(255, 105, 180, 0.2) !important;
    }
    
    /* Iconos decorativos */
    .icono-rosa {
        color: #FF69B4;
        font-size: 24px;
        margin-right: 10px;
    }
    
    /* Separadores */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #FF69B4, transparent);
        margin: 30px 0;
    }
    
    /* Badges de estado */
    .badge-pendiente {
        background-color: #FFF3CD;
        color: #856404;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        display: inline-block;
    }
    
    .badge-confirmado {
        background-color: #D4EDDA;
        color: #155724;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        display: inline-block;
    }
    
    .badge-completado {
        background-color: #D1ECF1;
        color: #0C5460;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        display: inline-block;
    }
    
    .badge-cancelado {
        background-color: #F8D7DA;
        color: #721C24;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================
# CONFIGURACIÓN DE PÁGINA
# ============================================

st.set_page_config(
    page_title=" Salón de Belleza - Sistema de Gestión",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com',
        'Report a bug': None,
        'About': " Sistema de Gestión para Salón de Belleza\nVersión 1.0 "
    }
)

# Aplicar estilos CSS
aplicar_estilos()

# ============================================
# INICIALIZACIÓN DEL SISTEMA
# ============================================

@st.cache_resource
def inicializar_sistema():
    """Inicializa el sistema del salón."""
    try:
        from salon_belleza.core.sistema_salon import SistemaSalon
        sistema = SistemaSalon()
        return sistema
    except Exception as e:
        st.error(f"❌ Error al inicializar el sistema: {e}")
        st.info("💡 Asegúrate de que todos los archivos del sistema estén en su lugar.")
        return None

sistema = inicializar_sistema()

if sistema is None:
    st.stop()

# ============================================
# COMPONENTES REUTILIZABLES
# ============================================

def mostrar_encabezado_pagina(titulo, icono=""):
    """Muestra un encabezado estilizado para cada página."""
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background: #870847; 
                border-radius: 15px; margin-bottom: 30px;'>
        <h1 style='color: white; margin: 0; font-size: 2.5em;'>
            {icono} {titulo}
        </h1>
    </div>
    """, unsafe_allow_html=True)

def crear_tarjeta_servicio(servicio):
    """Crea una tarjeta estilizada para un servicio."""
    color_categoria = {
        'Uñas': '#870847',
        'Cejas': '#870847',
        'Depilación': "#870847",
        'Facial': '#870847',
        'Corporal': '#870847'
    }.get(servicio.categoria, '#870847')
    
    return f"""
    <div class="tarjeta-rosa" style="border-left-color: {color_categoria};">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h4 style="margin: 0; color: {color_categoria};">{servicio.nombre}</h4>
                <p style="margin: 5px 0; color: #666;">
                    <span style="background-color: {color_categoria}20; padding: 2px 8px; border-radius: 10px; font-size: 12px;">
                        {servicio.categoria}
                    </span>
                </p>
            </div>
            <div style="text-align: right;">
                <h3 style="margin: 0; color: {color_categoria};">${servicio.precio_base}</h3>
                <p style="margin: 0; font-size: 14px; color: #888;">⏱️ {servicio.duracion_minutos}min</p>
            </div>
        </div>
        {f'<p style="margin-top: 10px; color: #777; font-size: 14px;">{servicio.descripcion}</p>' if servicio.descripcion else ''}
    </div>
    """

def crear_tarjeta_turno(turno):
    """Crea una tarjeta estilizada para un turno."""
    servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
    servicio_nombre = servicio.nombre if servicio else "N/A"
    
    # Icono según el estado
    iconos_estado = {
        'pendiente': '⏳',
        'confirmado': '✅',
        'completado': '🎉',
        'cancelado': '❌'
    }
    
    color_estado = {
        'pendiente': '#FFA500',
        'confirmado': '#32CD32',
        'completado': '#4169E1',
        'cancelado': '#FF4500'
    }
    
    badge_clase = f"badge-{turno.estado}"
    
    return f"""
    <div class="tarjeta-rosa">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div style="flex: 1;">
                <h4 style="margin: 0 0 10px 0; color: #FF69B4;">{turno.cliente_nombre}</h4>
                <div style="display: flex; gap: 15px; margin-bottom: 10px;">
                    <span style="color: #666;">
                        📅 {turno.fecha} 🕒 {turno.hora}
                    </span>
                </div>
                <p style="margin: 0; color: #555;">
                    💅 <strong>{servicio_nombre}</strong>
                </p>
            </div>
            <div style="text-align: right;">
                <div class="{badge_clase}" style="margin-bottom: 10px;">
                    {iconos_estado.get(turno.estado, '❓')} {turno.estado.upper()}
                </div>
                {f'<p style="margin: 0; color: #666; font-size: 14px;">📞 {turno.telefono}</p>' if turno.telefono else ''}
            </div>
        </div>
    </div>
    """

def crear_metrica(label, valor, icono, color="#E64A98"):
    """Crea una métrica estilizada."""
    return f"""
    <div style="text-align: center; padding: 15px; background: white; border-radius: 15px; 
                border: 2px solid {color}; margin: 5px;">
        <div style="font-size: 24px; color: {color}; margin-bottom: 5px;">
            {icono}
        </div>
        <div style="font-size: 32px; font-weight: bold; color: {color}; margin: 10px 0;">
            {valor}
        </div>
        <div style="font-size: 14px; color: #E64A98;">
            {label}
        </div>
    </div>
    """

# ============================================
# PÁGINA: DASHBOARD PRINCIPAL
# ============================================

def mostrar_dashboard():
    """Dashboard principal con métricas y resumen."""
    mostrar_encabezado_pagina("Dashboard Principal")
    
    # Fila de métricas principales
    stats = sistema.obtener_estadisticas()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(crear_metrica(
            "TOTAL TURNOS",
            stats['total_turnos'],
            "📋",
            "#870847"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(crear_metrica(
            "TURNOS HOY",
            len(sistema.obtener_turnos(fecha=datetime.now().strftime("%Y-%m-%d"))),
            "🎯",
            "#870847"
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(crear_metrica(
            "PENDIENTES",
            stats['estados'].get('pendiente', 0),
            "⏳",
            "#FFA500"
        ), unsafe_allow_html=True)
    
    with col4:
        st.markdown(crear_metrica(
            "PROFESIONALES",
            stats['profesionales_activos'],
            "👩‍💼",
            "#870847"
        ), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sección en dos columnas
    col_left, col_right = st.columns(2)
    
    with col_left:
        # Turnos por estado
        st.subheader("📈 Distribución por Estado")
        
        estados_data = []
        for estado, cantidad in stats['estados'].items():
            porcentaje = (cantidad / stats['total_turnos'] * 100) if stats['total_turnos'] > 0 else 0
            estados_data.append({
                'Estado': estado.upper(),
                'Cantidad': cantidad,
                'Porcentaje': f"{porcentaje:.1f}%"
            })
        
        df_estados = pd.DataFrame(estados_data)
        
        # Mostrar como tabla estilizada
        if not df_estados.empty:
            st.dataframe(
                df_estados,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Estado": st.column_config.TextColumn("📊 Estado"),
                    "Cantidad": st.column_config.NumberColumn("🔢 Cantidad"),
                    "Porcentaje": st.column_config.TextColumn("📶 %")
                }
            )
        
        # Gráfico de barras simple usando Streamlit nativo
        if stats['total_turnos'] > 0:
            st.bar_chart(df_estados.set_index('Estado')['Cantidad'])
    
    with col_right:
        # Turnos de hoy
        st.subheader("📅 Turnos de Hoy")
        
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        turnos_hoy = sistema.obtener_turnos(fecha=fecha_hoy)
        
        if turnos_hoy:
            # Crear contenedor con scroll
            contenedor = st.container(height=400)
            
            with contenedor:
                for turno in turnos_hoy:
                    st.markdown(crear_tarjeta_turno(turno), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="tarjeta-lila" style="text-align: center; padding: 40px;">
                <h1 style="color: white; margin: 0;">¡No hay turnos hoy!🎉</h1>
                <p style="color: white; opacity: 0.9;">Es un buen día para descansar o programar mantenimiento.</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Próximos turnos (3 días)
    st.subheader("📅 Próximos Turnos (3 días)")
    
    proximos_turnos = []
    for i in range(3):
        fecha = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        turnos_dia = sistema.obtener_turnos(fecha=fecha)
        proximos_turnos.extend(turnos_dia)
    
    if proximos_turnos:
        # Crear DataFrame para mostrar
        datos_turnos = []
        for turno in proximos_turnos[:10]:  # Mostrar máximo 10
            servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
            datos_turnos.append({
                'Fecha': turno.fecha,
                'Hora': turno.hora,
                'Cliente': turno.cliente_nombre[:15],
                'Servicio': servicio.nombre[:20] if servicio else "N/A",
                'Teléfono': turno.telefono[:10] if turno.telefono else "-",
                'Estado': turno.estado
            })
        
        df_proximos = pd.DataFrame(datos_turnos)
        
        # Mostrar como tabla
        st.dataframe(
            df_proximos,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Fecha": st.column_config.TextColumn("📅"),
                "Hora": st.column_config.TextColumn("🕒"),
                "Cliente": st.column_config.TextColumn("👤 Cliente"),
                "Servicio": st.column_config.TextColumn("💅 Servicio"),
                "Teléfono": st.column_config.TextColumn("📞"),
                "Estado": st.column_config.TextColumn("📊")
            }
        )
    else:
        st.info("📭 No hay turnos programados para los próximos 3 días")

# ============================================
# PÁGINA: CREAR TURNO
# ============================================

def mostrar_crear_turno():
    """Interfaz para crear nuevos turnos."""
    mostrar_encabezado_pagina("Crear Nuevo Turno", "📝")
    
    # Pestañas para diferentes modos
    tab1, tab2 = st.tabs(["🎯 Creación Guiada", "⚡ Creación Rápida"])
    
    with tab1:
        st.markdown("### 🎯 Sigue estos pasos para crear un turno")
        
        # Paso 1: Seleccionar servicio
        st.markdown("#### 1️⃣ Selecciona un servicio")
        
        servicios = sistema.obtener_servicios()
        if not servicios:
            st.warning("No hay servicios disponibles. Agrega servicios en la configuración.")
            return
        
        # Mostrar servicios en tarjetas
        cols = st.columns(3)
        servicio_seleccionado = None
        
        for idx, servicio in enumerate(servicios):
            col_idx = idx % 3
            with cols[col_idx]:
                if st.button(
                    f"💅 {servicio.nombre}\n⏱️ {servicio.duracion_minutos}min | 💰 ${servicio.precio_base}",
                    key=f"serv_{servicio.id}",
                    use_container_width=True
                ):
                    st.session_state['servicio_seleccionado'] = servicio
                    servicio_seleccionado = servicio
        
        # Si ya hay selección previa, mostrarla
        if 'servicio_seleccionado' in st.session_state:
            servicio = st.session_state['servicio_seleccionado']
            st.success(f"✅ **Servicio seleccionado:** {servicio.nombre}")
            servicio_seleccionado = servicio
        
        if not servicio_seleccionado:
            st.info("👉 Selecciona un servicio para continuar")
            return
        
        st.markdown("---")
        
        # Paso 2: Seleccionar fecha
        st.markdown("#### 2️⃣ Selecciona una fecha")
        
        col_fecha1, col_fecha2 = st.columns(2)
        
        with col_fecha1:
            # Selector de fecha
            fecha_minima = date.today() + timedelta(days=1)
            fecha_maxima = date.today() + timedelta(days=30)
            
            fecha_seleccionada = st.date_input(
                "📅 Fecha deseada",
                min_value=fecha_minima,
                max_value=fecha_maxima,
                value=fecha_minima
            )
        
        with col_fecha2:
            # Verificar disponibilidad
            fecha_str = fecha_seleccionada.strftime("%Y-%m-%d")
            abierto, _ = sistema.calendario.esta_abierto(fecha_str)
            
            if abierto:
                st.success("✅ El salón está abierto este día")
                # Mostrar horarios disponibles
                horarios = sistema.calendario.obtener_horarios_disponibles(
                    fecha_str, 
                    servicio_seleccionado.duracion_minutos
                )
                
                if horarios:
                    st.info(f"⏰ Horarios disponibles: {len(horarios)}")
                else:
                    st.warning("⚠️ No hay horarios disponibles para esta fecha")
            else:
                st.error("❌ El salón está cerrado este día")
                return
        
        st.markdown("---")
        
        # Paso 3: Seleccionar horario
        st.markdown("#### 3️⃣ Selecciona un horario")
        
        if 'fecha_seleccionada' not in st.session_state or st.session_state['fecha_seleccionada'] != fecha_str:
            st.session_state['fecha_seleccionada'] = fecha_str
            horarios = sistema.calendario.obtener_horarios_disponibles(
                fecha_str, 
                servicio_seleccionado.duracion_minutos
            )
            st.session_state['horarios_disponibles'] = horarios
        
        horarios = st.session_state.get('horarios_disponibles', [])
        
        if horarios:
            # Mostrar horarios en una cuadrícula
            st.write("**Horarios disponibles:**")
            
            cols_horarios = st.columns(4)
            horario_seleccionado = None
            
            for idx, horario in enumerate(horarios[:12]):  # Mostrar máximo 12
                col_idx = idx % 4
                with cols_horarios[col_idx]:
                    if st.button(
                        f"🕒 {horario}",
                        key=f"hora_{horario}",
                        use_container_width=True
                    ):
                        horario_seleccionado = horario
                        st.session_state['horario_seleccionado'] = horario
            
            # Si hay horario seleccionado, mostrarlo
            if 'horario_seleccionado' in st.session_state:
                horario_seleccionado = st.session_state['horario_seleccionado']
                st.success(f"✅ **Horario seleccionado:** {horario_seleccionado}")
        else:
            st.warning("⚠️ No hay horarios disponibles para esta fecha")
            return
        
        st.markdown("---")
        
        # Paso 4: Datos del cliente
        st.markdown("#### 4️⃣ Información del cliente")
        
        with st.form("form_cliente"):
            col_cli1, col_cli2 = st.columns(2)
            
            with col_cli1:
                cliente_nombre = st.text_input(
                    "👤 Nombre completo *",
                    placeholder="María González"
                )
                
                telefono = st.text_input(
                    "📞 Teléfono",
                    placeholder="+54 9 11 1234-5678"
                )
            
            with col_cli2:
                email = st.text_input(
                    "📧 Email",
                    placeholder="cliente@ejemplo.com"
                )
                
                # Selección de profesional (opcional)
                profesionales = sistema.obtener_profesionales(activos=True)
                if profesionales:
                    opciones_prof = ["💁‍♀️ Asignar automáticamente"]
                    opciones_prof.extend([f"👩‍💼 {p['nombre']}" for p in profesionales])
                    
                    profesional_sel = st.selectbox(
                        "👩‍💼 Profesional preferido",
                        options=opciones_prof
                    )
                    
                    profesional_id = None
                    if profesional_sel != opciones_prof[0]:
                        for prof in profesionales:
                            if f"👩‍💼 {prof['nombre']}" == profesional_sel:
                                profesional_id = prof['id']
                                break
            
            # Botón de envío
            submitted = st.form_submit_button(
                "✨ Crear Turno",
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                if not cliente_nombre:
                    st.error("❌ El nombre del cliente es obligatorio")
                elif not horario_seleccionado:
                    st.error("❌ Debes seleccionar un horario")
                else:
                    # Crear el turno
                    exito, mensaje, turno = sistema.crear_turno(
                        cliente_nombre=cliente_nombre,
                        fecha=fecha_str,
                        hora=horario_seleccionado,
                        servicio_id=servicio_seleccionado.id,
                        telefono=telefono,
                        email=email,
                        profesional_id=profesional_id
                    )
                    
                    if exito:
                        st.success(f"✅ {mensaje}")
                        st.balloons()
                        
                        # Mostrar confirmación
                        st.markdown(f"""
                        <div class="tarjeta-lila">
                            <h3 style="color: white; text-align: center;">🎉 ¡Turno Creado Exitosamente!</h3>
                            <div style="background: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 10px; margin: 15px 0;">
                                <p style="color: white; margin: 5px 0;">👤 <strong>{cliente_nombre}</strong></p>
                                <p style="color: white; margin: 5px 0;">📅 <strong>{fecha_str} {horario_seleccionado}</strong></p>
                                <p style="color: white; margin: 5px 0;">💅 <strong>{servicio_seleccionado.nombre}</strong></p>
                                <p style="color: white; margin: 5px 0; font-size: 24px; text-align: center;">
                                    🔑 ID: <strong>{turno.id}</strong>
                                </p>
                            </div>
                            <p style="color: white; text-align: center; font-size: 14px;">
                                Guarda este ID para futuras consultas o modificaciones
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Limpiar selecciones
                        for key in ['servicio_seleccionado', 'horario_seleccionado', 'fecha_seleccionada']:
                            if key in st.session_state:
                                del st.session_state[key]
                    else:
                        st.error(f"❌ {mensaje}")
    
    with tab2:
        st.markdown("### ⚡ Creación Rápida")
        st.markdown("Para cuando necesitas agendar rápido sin muchos detalles.")
        
        with st.form("form_rapido"):
            # Campos básicos
            cliente = st.text_input("👤 Nombre del cliente *")
            
            # Servicios en selectbox simple
            servicios_opciones = {s.nombre: s.id for s in servicios}
            servicio_nombre = st.selectbox("💅 Servicio *", options=list(servicios_opciones.keys()))
            
            # Fecha y hora simples
            col_rap1, col_rap2 = st.columns(2)
            with col_rap1:
                fecha_rapida = st.date_input(
                    "📅 Fecha *",
                    min_value=date.today() + timedelta(days=1)
                )
            with col_rap2:
                hora_rapida = st.time_input("🕒 Hora *", value=datetime.strptime("10:00", "%H:%M"))
            
            telefono = st.text_input("📞 Teléfono (opcional)")
            
            # Botón de creación rápida
            creado = st.form_submit_button(
                "🚀 Crear Turno Rápido",
                type="primary",
                use_container_width=True
            )
            
            if creado:
                if not cliente:
                    st.error("❌ El nombre es obligatorio")
                else:
                    exito, mensaje, turno = sistema.crear_turno(
                        cliente_nombre=cliente,
                        fecha=fecha_rapida.strftime("%Y-%m-%d"),
                        hora=hora_rapida.strftime("%H:%M"),
                        servicio_id=servicios_opciones[servicio_nombre],
                        telefono=telefono
                    )
                    
                    if exito:
                        st.success(f"✅ Turno creado! ID: {turno.id}")
                        st.rerun()
                    else:
                        st.error(f"❌ {mensaje}")

# ============================================
# PÁGINA: GESTIÓN DE TURNOS
# ============================================

def mostrar_gestion_turnos():
    """Interfaz para gestionar turnos existentes."""
    mostrar_encabezado_pagina("Gestión de Turnos", "📋")
    
    # Barra de búsqueda y filtros
    with st.container():
        col_busq1, col_busq2, col_busq3 = st.columns([2, 2, 1])
        
        with col_busq1:
            fecha_filtro = st.date_input(
                "📅 Filtrar por fecha",
                value=None
            )
        
        with col_busq2:
            estado_filtro = st.selectbox(
                "📊 Filtrar por estado",
                options=["Todos", "pendiente", "confirmado", "completado", "cancelado"]
            )
        
        with col_busq3:
            st.write("")  # Espaciador
            if st.button("🔍 Buscar", use_container_width=True):
                st.session_state['buscar_turnos'] = True
    
    st.markdown("---")
    
    # Búsqueda por ID específico
    with st.expander("🔍 Buscar turno por ID", expanded=False):
        col_id1, col_id2 = st.columns([3, 1])
        
        with col_id1:
            turno_id_buscar = st.text_input("Ingresa el ID del turno", placeholder="Ej: 1")
        
        with col_id2:
            st.write("")
            if st.button("Buscar ID", use_container_width=True):
                if turno_id_buscar:
                    turno = sistema.turno_repository.obtener_turno(turno_id_buscar)
                    if turno:
                        st.session_state['turno_especifico'] = turno
                    else:
                        st.error("❌ No se encontró un turno con ese ID")
    
    # Mostrar turnos según filtros
    if st.session_state.get('buscar_turnos', False) or 'turno_especifico' in st.session_state:
        
        if 'turno_especifico' in st.session_state:
            turnos = [st.session_state['turno_especifico']]
            mostrar_especifico = True
        else:
            if fecha_filtro:
                fecha_str = fecha_filtro.strftime("%Y-%m-%d")
                turnos = sistema.obtener_turnos(fecha=fecha_str)
            else:
                turnos = sistema.obtener_turnos()
            
            if estado_filtro != "Todos":
                turnos = [t for t in turnos if t.estado == estado_filtro]
            
            mostrar_especifico = False
        
        if not turnos:
            st.info("📭 No se encontraron turnos con los filtros aplicados")
            if 'turno_especifico' in st.session_state:
                del st.session_state['turno_especifico']
        else:
            st.subheader(f"📋 {len(turnos)} Turno{'s' if len(turnos) != 1 else ''} Encontrado{'s' if len(turnos) != 1 else ''}")
            
            # Contador de turnos por estado
            if not mostrar_especifico and len(turnos) > 1:
                conteo_estados = {}
                for turno in turnos:
                    conteo_estados[turno.estado] = conteo_estados.get(turno.estado, 0) + 1
                
                cols_contadores = st.columns(len(conteo_estados))
                for idx, (estado, cantidad) in enumerate(conteo_estados.items()):
                    with cols_contadores[idx]:
                        icono = {'pendiente': '⏳', 'confirmado': '✅', 'completado': '🎉', 'cancelado': '❌'}.get(estado, '❓')
                        st.metric(f"{icono} {estado.capitalize()}", cantidad)
            
            # Mostrar cada turno
            for turno in turnos:
                servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
                
                with st.container():
                    st.markdown(crear_tarjeta_turno(turno), unsafe_allow_html=True)
                    
                    # Botones de acción
                    col_acc1, col_acc2, col_acc3, col_acc4 = st.columns(4)
                    
                    with col_acc1:
                        if st.button(f"👁️ Ver detalles", key=f"det_{turno.id}", use_container_width=True):
                            st.session_state[f'detalle_{turno.id}'] = True
                    
                    with col_acc2:
                        if turno.estado in ["pendiente", "confirmado"]:
                            if st.button(f"✅ Confirmar", key=f"conf_{turno.id}", use_container_width=True):
                                exito, mensaje = sistema.confirmar_turno(str(turno.id))
                                if exito:
                                    st.success(mensaje)
                                    st.rerun()
                    
                    with col_acc3:
                        if turno.estado in ["pendiente", "confirmado"]:
                            if st.button(f"❌ Cancelar", key=f"canc_{turno.id}", use_container_width=True):
                                exito, mensaje = sistema.cancelar_turno(str(turno.id))
                                if exito:
                                    st.success(mensaje)
                                    st.rerun()
                    
                    with col_acc4:
                        if st.button(f"🗑️ Eliminar", key=f"elim_{turno.id}", use_container_width=True):
                            exito = sistema.turno_repository.eliminar_turno(str(turno.id))
                            if exito:
                                st.success("Turno eliminado")
                                st.rerun()
                    
                    # Detalles expandibles
                    if st.session_state.get(f'detalle_{turno.id}', False):
                        with st.expander("📋 Detalles completos", expanded=True):
                            col_det1, col_det2 = st.columns(2)
                            
                            with col_det1:
                                st.write("**👤 Información del Cliente:**")
                                st.write(f"**Nombre:** {turno.cliente_nombre}")
                                st.write(f"**Teléfono:** {turno.telefono}")
                                st.write(f"**Email:** {turno.email}")
                                st.write(f"**ID Turno:** {turno.id}")
                                st.write(f"**Fecha registro:** {turno.timestamp_registro[:19] if turno.timestamp_registro else 'N/A'}")
                            
                            with col_det2:
                                st.write("**💅 Información del Servicio:**")
                                if servicio:
                                    st.write(f"**Servicio:** {servicio.nombre}")
                                    st.write(f"**Duración:** {servicio.duracion_minutos} min")
                                    st.write(f"**Precio base:** ${servicio.precio_base}")
                                st.write(f"**Fecha:** {turno.fecha}")
                                st.write(f"**Hora:** {turno.hora}")
                                st.write(f"**Profesional ID:** {turno.profesional_id or 'Por asignar'}")
                                st.write(f"**Estado pago:** {turno.estado_pago}")
                                if turno.notas_internas:
                                    st.write(f"**Notas:** {turno.notas_internas}")
                    
                    st.markdown("---")
    
    else:
        # Vista por defecto: turnos de hoy y mañana
        col_hoy, col_manana = st.columns(2)
        
        with col_hoy:
            st.subheader("📅 Turnos de Hoy")
            fecha_hoy = datetime.now().strftime("%Y-%m-%d")
            turnos_hoy = sistema.obtener_turnos(fecha=fecha_hoy)
            
            if turnos_hoy:
                for turno in turnos_hoy[:3]:
                    st.markdown(crear_tarjeta_turno(turno), unsafe_allow_html=True)
                if len(turnos_hoy) > 3:
                    st.caption(f"*Y {len(turnos_hoy) - 3} turnos más...*")
            else:
                st.info("🎉 No hay turnos para hoy")
        
        with col_manana:
            st.subheader("📅 Turnos de Mañana")
            fecha_manana = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            turnos_manana = sistema.obtener_turnos(fecha=fecha_manana)
            
            if turnos_manana:
                for turno in turnos_manana[:3]:
                    st.markdown(crear_tarjeta_turno(turno), unsafe_allow_html=True)
                if len(turnos_manana) > 3:
                    st.caption(f"*Y {len(turnos_manana) - 3} turnos más...*")
            else:
                st.info("📭 No hay turnos para mañana")

# ============================================
# PÁGINA: SERVICIOS
# ============================================

def mostrar_servicios():
    """Interfaz para ver y gestionar servicios."""
    mostrar_encabezado_pagina("Servicios Disponibles", "💅")
    
    servicios = sistema.obtener_servicios()
    
    if not servicios:
        st.info("📭 No hay servicios disponibles")
        return
    
    # Mostrar servicios en una cuadrícula
    st.markdown("### 💖 Nuestros Servicios")
    
    cols = st.columns(3)
    
    for idx, servicio in enumerate(servicios):
        col_idx = idx % 3
        with cols[col_idx]:
            st.markdown(crear_tarjeta_servicio(servicio), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Estadísticas de servicios
    st.markdown("### 📊 Estadísticas de Servicios")
    
    turnos = sistema.obtener_turnos()
    
    if turnos:
        # Contar turnos por servicio
        conteo_servicios = {}
        ingresos_servicios = {}
        
        for turno in turnos:
            servicio_id = turno.servicio_id
            conteo_servicios[servicio_id] = conteo_servicios.get(servicio_id, 0) + 1
            
            servicio = sistema.obtener_servicio_por_id(servicio_id)
            if servicio:
                ingresos_servicios[servicio_id] = ingresos_servicios.get(servicio_id, 0) + servicio.precio_base
        
        # Crear DataFrame para mostrar
        datos_servicios = []
        for servicio in servicios:
            cantidad = conteo_servicios.get(servicio.id, 0)
            ingresos = ingresos_servicios.get(servicio.id, 0)
            datos_servicios.append({
                'Servicio': servicio.nombre,
                'Turnos': cantidad,
                'Ingresos': f"${ingresos:.2f}",
                'Popularidad': '★' * min(cantidad, 5)  # Máximo 5 estrellas
            })
        
        df_servicios = pd.DataFrame(datos_servicios)
        df_servicios = df_servicios.sort_values('Turnos', ascending=False)
        
        # Mostrar tabla
        st.dataframe(
            df_servicios,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Servicio": st.column_config.TextColumn("💅 Servicio", width="large"),
                "Turnos": st.column_config.NumberColumn("📊 Turnos"),
                "Ingresos": st.column_config.TextColumn("💰 Ingresos"),
                "Popularidad": st.column_config.TextColumn("⭐ Popularidad")
            }
        )
        
        # Servicios más populares
        st.markdown("#### 🏆 Servicios Más Populares")
        
        top_servicios = df_servicios.head(3)
        
        for idx, (_, row) in enumerate(top_servicios.iterrows()):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.markdown(f"<h2 style='color: #FF69B4; text-align: center;'>#{idx+1}</h2>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<h4 style='color: #FF1493;'>{row['Servicio']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #666;'>{row['Turnos']} turnos | {row['Ingresos']}</p>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div style='color: #FFD700; font-size: 24px; text-align: center;'>{row['Popularidad']}</div>", unsafe_allow_html=True)
            
            st.markdown("---")

# ============================================
# PÁGINA: PROFESIONALES
# ============================================

def mostrar_profesionales():
    """Interfaz para ver y gestionar profesionales."""
    mostrar_encabezado_pagina("Nuestro Equipo", "👩‍💼")
    
    profesionales = sistema.obtener_profesionales(activos=True)
    
    if not profesionales:
        st.info("📭 No hay profesionales activos")
        return
    
    st.markdown("### 💖 Conoce a Nuestro Equipo")
    
    # Mostrar profesionales en tarjetas
    cols = st.columns(3)
    
    for idx, profesional in enumerate(profesionales):
        col_idx = idx % 3
        
        with cols[col_idx]:
            color = profesional.get('color_calendario', '#FF69B4')
            
            st.markdown(f"""
            <div style='background: white; border-radius: 15px; padding: 20px; 
                        text-align: center; box-shadow: 0 4px 6px rgba(255, 105, 180, 0.1); 
                        border-top: 5px solid {color};'>
                <div style='width: 80px; height: 80px; border-radius: 50%; 
                            background: linear-gradient(135deg, {color} 0%, #FFB6C1 100%); 
                            margin: 0 auto 15px; display: flex; align-items: center; 
                            justify-content: center; color: white; font-size: 32px;'>
                    {profesional['nombre'][0]}
                </div>
                <h3 style='color: {color}; margin: 10px 0;'>{profesional['nombre']}</h3>
                <p style='color: #666; margin: 5px 0; font-size: 14px;'>
                    ID: {profesional['id']}
                </p>
                <div style='background-color: {color}20; padding: 8px; 
                            border-radius: 10px; margin-top: 10px;'>
                    <p style='margin: 0; color: {color}; font-size: 13px;'>
                        Especialista en servicios seleccionados
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Agenda de profesionales
    st.markdown("### 📅 Agenda por Profesional")
    
    for profesional in profesionales:
        with st.expander(f"👩‍💼 Agenda de {profesional['nombre']}", expanded=False):
            # Obtener turnos del profesional
            turnos_prof = sistema.obtener_turnos(profesional_id=profesional['id'])
            
            if turnos_prof:
                # Agrupar por fecha
                turnos_por_fecha = {}
                for turno in turnos_prof:
                    if turno.fecha not in turnos_por_fecha:
                        turnos_por_fecha[turno.fecha] = []
                    turnos_por_fecha[turno.fecha].append(turno)
                
                # Mostrar por fecha
                for fecha, turnos in sorted(turnos_por_fecha.items()):
                    fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
                    fecha_formateada = fecha_obj.strftime("%A %d/%m/%Y")
                    
                    st.markdown(f"**{fecha_formateada}:**")
                    
                    for turno in turnos:
                        servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
                        servicio_nombre = servicio.nombre if servicio else "N/A"
                        
                        col1, col2, col3 = st.columns([2, 3, 2])
                        with col1:
                            st.write(f"🕒 {turno.hora}")
                        with col2:
                            st.write(f"👤 {turno.cliente_nombre}")
                        with col3:
                            badge_clase = f"badge-{turno.estado}"
                            st.markdown(f"<div class='{badge_clase}'>{turno.estado}</div>", unsafe_allow_html=True)
                    
                    st.markdown("---")
            else:
                st.info("📭 No tiene turnos asignados")

# ============================================
# PÁGINA: ESTADÍSTICAS
# ============================================

def mostrar_estadisticas():
    """Interfaz para estadísticas."""
    mostrar_encabezado_pagina("Estadísticas y Reportes", "📈")
    
    # Pestañas para diferentes tipos de estadísticas
    tab1, tab2, tab3 = st.tabs(["📊 General", "📅 Temporal", "👥 Clientes"])
    
    with tab1:
        st.markdown("### 📊 Estadísticas Generales")
        
        stats = sistema.obtener_estadisticas()
        
        # Métricas principales
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ingresos_totales = 0
            for servicio_id, cantidad in stats['servicios'].items():
                servicio = sistema.obtener_servicio_por_id(servicio_id)
                if servicio:
                    ingresos_totales += cantidad * servicio.precio_base
            
            st.markdown(crear_metrica(
                "INGRESOS TOTALES",
                f"${ingresos_totales:,.2f}",
                "💰",
                "#FF1493"
            ), unsafe_allow_html=True)
        
        with col2:
            tasa_confirmacion = (stats['estados'].get('confirmado', 0) / stats['total_turnos'] * 100) if stats['total_turnos'] > 0 else 0
            st.markdown(crear_metrica(
                "TASA CONFIRMACIÓN",
                f"{tasa_confirmacion:.1f}%",
                "✅",
                "#32CD32"
            ), unsafe_allow_html=True)
        
        with col3:
            ocupacion_promedio = stats['total_turnos'] / 30  # Asumiendo 30 días
            st.markdown(crear_metrica(
                "OCUPACIÓN PROMEDIO",
                f"{ocupacion_promedio:.1f}/día",
                "📊",
                "#FF69B4"
            ), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Distribución por servicio
        st.markdown("### 💅 Distribución por Servicio")
        
        datos_servicios = []
        for servicio_id, cantidad in stats['servicios'].items():
            servicio = sistema.obtener_servicio_por_id(servicio_id)
            if servicio:
                datos_servicios.append({
                    'Servicio': servicio.nombre,
                    'Turnos': cantidad,
                    'Ingresos': cantidad * servicio.precio_base
                })
        
        if datos_servicios:
            df_servicios = pd.DataFrame(datos_servicios)
            df_servicios = df_servicios.sort_values('Turnos', ascending=False)
            
            # Mostrar como tabla
            st.dataframe(
                df_servicios,
                use_container_width=True,
                hide_index=True
            )
            
            # Gráfico simple de barras
            st.bar_chart(df_servicios.set_index('Servicio')['Turnos'])
    
    with tab2:
        st.markdown("### 📅 Análisis Temporal")
        
        turnos = sistema.obtener_turnos()
        
        if turnos:
            # Convertir a DataFrame
            datos_turnos = []
            for turno in turnos:
                servicio = sistema.obtener_servicio_por_id(turno.servicio_id)
                datos_turnos.append({
                    'Fecha': turno.fecha,
                    'Hora': turno.hora,
                    'Servicio': servicio.nombre if servicio else "N/A",
                    'Estado': turno.estado
                })
            
            df_turnos = pd.DataFrame(datos_turnos)
            df_turnos['Fecha_dt'] = pd.to_datetime(df_turnos['Fecha'])
            
            # Turnos por día
            st.markdown("#### 📈 Turnos por Día")
            turnos_por_dia = df_turnos.groupby('Fecha_dt').size().reset_index(name='Cantidad')
            turnos_por_dia = turnos_por_dia.sort_values('Fecha_dt')
            
            if not turnos_por_dia.empty:
                st.line_chart(turnos_por_dia.set_index('Fecha_dt'))
                
                # Estadísticas por día
                col_dia1, col_dia2, col_dia3 = st.columns(3)
                with col_dia1:
                    st.metric("📅 Días con turnos", len(turnos_por_dia))
                with col_dia2:
                    st.metric("📊 Máximo en un día", turnos_por_dia['Cantidad'].max())
                with col_dia3:
                    st.metric("📈 Promedio diario", f"{turnos_por_dia['Cantidad'].mean():.1f}")
            
            # Turnos por día de la semana
            st.markdown("#### 📅 Turnos por Día de la Semana")
            df_turnos['Dia_Semana'] = df_turnos['Fecha_dt'].dt.day_name()
            
            dias_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            df_turnos['Dia_Semana'] = pd.Categorical(df_turnos['Dia_Semana'], categories=dias_orden, ordered=True)
            
            turnos_por_dia_semana = df_turnos.groupby('Dia_Semana').size().reset_index(name='Cantidad')
            
            # Traducir al español
            dias_espanol = {
                'Monday': 'Lunes',
                'Tuesday': 'Martes',
                'Wednesday': 'Miércoles',
                'Thursday': 'Jueves',
                'Friday': 'Viernes',
                'Saturday': 'Sábado',
                'Sunday': 'Domingo'
            }
            turnos_por_dia_semana['Dia'] = turnos_por_dia_semana['Dia_Semana'].map(dias_espanol)
            
            st.bar_chart(turnos_por_dia_semana.set_index('Dia')['Cantidad'])
    
    with tab3:
        st.markdown("### 👥 Análisis de Clientes")
        
        turnos = sistema.obtener_turnos()
        
        if turnos:
            # Clientes más frecuentes
            clientes_count = {}
            for turno in turnos:
                cliente = turno.cliente_nombre
                clientes_count[cliente] = clientes_count.get(cliente, 0) + 1
            
            # Top 10 clientes
            top_clientes = sorted(clientes_count.items(), key=lambda x: x[1], reverse=True)[:10]
            
            if top_clientes:
                st.markdown("#### 🏆 Top 10 Clientes Más Frecuentes")
                
                for idx, (cliente, visitas) in enumerate(top_clientes, 1):
                    col1, col2, col3 = st.columns([1, 3, 1])
                    with col1:
                        st.markdown(f"<h3 style='color: #FF69B4; text-align: center;'>#{idx}</h3>", unsafe_allow_html=True)
                    with col2:
                        st.markdown(f"<h4 style='color: #FF1493;'>{cliente}</h4>", unsafe_allow_html=True)
                    with col3:
                        st.markdown(f"<h3 style='color: #DDA0DD; text-align: center;'>{visitas}</h3>", unsafe_allow_html=True)
                    
                    # Barra de progreso visual
                    progreso = min(visitas / max([v for _, v in top_clientes]) * 100, 100)
                    st.markdown(f"""
                    <div style='background-color: #FFE4E9; border-radius: 10px; height: 10px; margin: 5px 0 15px 0;'>
                        <div style='background: linear-gradient(90deg, #FF69B4 0%, #FF1493 100%); 
                                    width: {progreso}%; height: 100%; border-radius: 10px;'>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Estadísticas de clientes
                st.markdown("#### 📊 Estadísticas de Clientes")
                
                col_cli1, col_cli2, col_cli3 = st.columns(3)
                
                with col_cli1:
                    st.metric("👥 Clientes únicos", len(clientes_count))
                
                with col_cli2:
                    promedio_visitas = sum(clientes_count.values()) / len(clientes_count)
                    st.metric("📈 Visitas promedio", f"{promedio_visitas:.1f}")
                
                with col_cli3:
                    clientes_recurrentes = sum(1 for v in clientes_count.values() if v > 1)
                    st.metric("🔄 Clientes recurrentes", clientes_recurrentes)

# ============================================
# PÁGINA: CONFIGURACIÓN
# ============================================

def mostrar_configuracion():
    """Interfaz de configuración."""
    mostrar_encabezado_pagina("Configuración del Sistema", "⚙️")
    
    # Pestañas de configuración
    tab1, tab2, tab3 = st.tabs(["📋 Información", "🛠️ Herramientas", "📁 Sistema"])
    
    with tab1:
        st.markdown("### ℹ️ Información del Sistema")
        
        col_info1, col_info2 = st.columns(2)
        
        with col_info1:
            st.markdown("""
            <div class="tarjeta-rosa">
                <h4>📋 Detalles del Sistema</h4>
                <p>🎯 <strong>Versión:</strong> 1.0.0</p>
                <p>👩‍💻 <strong>Desarrollador:</strong> Salón de Belleza System</p>
                <p>📅 <strong>Última actualización:</strong> 2024</p>
                <p>🐍 <strong>Python:</strong> 3.8+</p>
                <p>🎨 <strong>Diseño:</strong> Rosa Minimalista</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_info2:
            stats = sistema.obtener_estadisticas()
            st.markdown(f"""
            <div class="tarjeta-rosa">
                <h4>📊 Estadísticas Actuales</h4>
                <p>📋 <strong>Turnos totales:</strong> {stats['total_turnos']}</p>
                <p>📅 <strong>Turnos futuros:</strong> {stats['turnos_futuros']}</p>
                <p>💅 <strong>Servicios activos:</strong> {stats['servicios_disponibles']}</p>
                <p>👩‍💼 <strong>Profesionales activos:</strong> {stats['profesionales_activos']}</p>
                <p>📈 <strong>Ocupación promedio:</strong> {stats['total_turnos']/30:.1f} turnos/día</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🛠️ Herramientas de Mantenimiento")
        
        col_her1, col_her2, col_her3 = st.columns(3)
        
        with col_her1:
            if st.button("🔄 Recargar Datos", use_container_width=True):
                sistema._cargar_servicios()
                sistema._cargar_profesionales()
                st.success("✅ Datos recargados exitosamente")
                st.rerun()
        
        with col_her2:
            if st.button("🧹 Limpiar Cache", use_container_width=True):
                st.cache_resource.clear()
                st.success("✅ Cache limpiado exitosamente")
                st.rerun()
        
        with col_her3:
            if st.button("📊 Exportar Reporte", use_container_width=True):
                # Crear un reporte simple
                reporte = f"""
                REPORTE DEL SISTEMA - {datetime.now().strftime("%d/%m/%Y %H:%M")}
                ============================================
                
                Estadísticas Generales:
                - Turnos totales: {stats['total_turnos']}
                - Turnos futuros: {stats['turnos_futuros']}
                - Servicios activos: {stats['servicios_disponibles']}
                - Profesionales activos: {stats['profesionales_activos']}
                
                Distribución por estado:
                """
                for estado, cantidad in stats['estados'].items():
                    reporte += f"  - {estado.capitalize()}: {cantidad}\n"
                
                st.download_button(
                    label="⬇️ Descargar Reporte",
                    data=reporte,
                    file_name=f"reporte_salon_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
    
    with tab3:
        st.markdown("### 📁 Archivos del Sistema")
        
        # Mostrar información de archivos
        import os
        
        archivos_data = []
        data_dir = sistema.data_dir
        
        if os.path.exists(data_dir):
            for archivo in os.listdir(data_dir):
                if archivo.endswith('.json'):
                    ruta = os.path.join(data_dir, archivo)
                    tamaño = os.path.getsize(ruta)
                    archivos_data.append({
                        'Archivo': archivo,
                        'Tamaño': f"{tamaño / 1024:.1f} KB"
                    })
        
        if archivos_data:
            st.dataframe(
                pd.DataFrame(archivos_data),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("⚠️ No se encontraron archivos de datos")

# ============================================
# BARRA LATERAL - NAVEGACIÓN
# ============================================

# Logo y título en sidebar
st.sidebar.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="color: white; margin: 0; font-size: 24px;">🌸</h1>
    <h2 style="color: white; margin: 10px 0; font-size: 18px;">Salón de Belleza</h2>
    <p style="color: rgba(255, 255, 255, 0.8); margin: 0; font-size: 12px;">
        Sistema de Gestión
    </p>
</div>
""", unsafe_allow_html=True)

# Separador decorativo
st.sidebar.markdown("<hr style='border-color: rgba(255, 255, 255, 0.2);'>", unsafe_allow_html=True)

# Menú de navegación
menu_opciones = {
    "🏠 Dashboard": mostrar_dashboard,
    "📅 Crear Turno": mostrar_crear_turno,
    "📋 Turnos": mostrar_gestion_turnos,
    "💅 Servicios": mostrar_servicios,
    "👩‍💼 Profesionales": mostrar_profesionales,
    "📈 Estadísticas": mostrar_estadisticas,
    "⚙️ Configuración": mostrar_configuracion
}

seleccion = st.sidebar.radio(
    "Navegación",
    options=list(menu_opciones.keys()),
    label_visibility="collapsed"
)

# Información en sidebar
st.sidebar.markdown("<hr style='border-color: rgba(255, 255, 255, 0.2);'>", unsafe_allow_html=True)

# Mostrar información actual
hoy = datetime.now().strftime("%d/%m/%Y")
turnos_hoy = len(sistema.obtener_turnos(fecha=datetime.now().strftime("%Y-%m-%d")))

st.sidebar.markdown(f"""
<div style="background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;">
    <p style="margin: 0; font-size: 14px; color: white;">📅 {hoy}</p>
    <p style="margin: 5px 0 0 0; font-size: 12px; color: rgba(255, 255, 255, 0.8);">
        🎯 {turnos_hoy} turno{'s' if turnos_hoy != 1 else ''} hoy
    </p>
</div>
""", unsafe_allow_html=True)

# Footer del sidebar
st.sidebar.markdown("""
<div style="position: absolute; bottom: 20px; left: 0; right: 0; padding: 0 20px;">
    <p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 11px; margin: 0;">
        💅 Sistema de Gestión v1.0<br>
        ✨ Diseño Rosa Minimalista
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

def main():
    """Función principal de la aplicación."""
    
    # Ejecutar la función seleccionada
    if seleccion in menu_opciones:
        menu_opciones[seleccion]()
    
    # Footer principal
    st.markdown("""
    <div style="text-align: center; padding: 20px; margin-top: 40px; color: #FF69B4;">
        <hr style="border-color: #FFB6C1;">
        <p style="font-size: 14px;">
            💖 <strong>Salón de Belleza</strong> | Sistema de Gestión v1.0 |
            ✨ Rubi Perez de Alejo
        </p>
        <p style="font-size: 12px; color: #888;">
            📞 Contacto: +53 53328137 | 
            📍 Dirección: Calle C/11 y 13, Vedado
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()