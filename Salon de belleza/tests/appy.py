"""
SALÓN DE BELLEZA - Interfaz Minimalista Rosa
Versión compatible con SistemaSalon
"""
import streamlit as st
import sys
import os
from datetime import datetime, timedelta, date

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ============================================
# ESTILOS CSS - ROSA MINIMALISTA
# ============================================

def aplicar_estilos():
    st.markdown("""
    <style>
    /* Fondo minimalista */
    .main {
        background-color: #FFF8FB;
    }
    
    /* Sidebar minimalista */
    [data-testid="stSidebar"] {
        background-color: #FFE4EC;
        border-right: 1px solid #FFC1D6;
    }
    
    [data-testid="stSidebar"] * {
        color: #7A4A58 !important;
    }
    
    /* Títulos minimalistas */
    .titulo-minimalista {
        color: #D44D7A;
        font-weight: 400;
        margin-bottom: 30px;
        text-align: center;
        font-size: 28px;
    }
    
    /* Tarjetas minimalistas */
    .tarjeta-minimalista {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid #FFC1D6;
        box-shadow: 0 2px 8px rgba(255, 182, 193, 0.1);
        transition: all 0.2s ease;
    }
    
    .tarjeta-minimalista:hover {
        box-shadow: 0 4px 12px rgba(255, 182, 193, 0.15);
        transform: translateY(-1px);
    }
    
    /* Botones minimalistas */
    .stButton button {
        background: linear-gradient(135deg, #FFB6C1 0%, #FF8FAB 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 400;
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #FF8FAB 0%, #FFB6C1 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(255, 182, 193, 0.2);
    }
    
    /* Inputs minimalistas */
    .stTextInput input, .stSelectbox select, .stDateInput input, .stTimeInput input {
        background: white !important;
        border: 1px solid #FFC1D6 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        color: #7A4A58 !important;
    }
    
    .stTextInput input:focus, .stSelectbox select:focus, 
    .stDateInput input:focus, .stTimeInput input:focus {
        border: 2px solid #FF8FAB !important;
        box-shadow: 0 0 0 2px rgba(255, 143, 171, 0.1) !important;
    }
    
    /* Métricas minimalistas */
    [data-testid="stMetric"] {
        background: white;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #FFC1D6;
    }
    
    [data-testid="stMetricLabel"] {
        color: #D44D7A !important;
        font-size: 14px !important;
    }
    
    [data-testid="stMetricValue"] {
        color: #FF69B4 !important;
        font-size: 24px !important;
    }
    
    /* Dataframes minimalistas */
    .dataframe {
        border-radius: 8px;
        border: 1px solid #FFC1D6;
        background: white;
    }
    
    /* Pestañas minimalistas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: white;
        padding: 8px;
        border-radius: 8px;
        border: 1px solid #FFC1D6;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #FFE4EC;
        border-radius: 6px;
        padding: 10px 20px;
        color: #D44D7A;
        transition: all 0.2s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FFB6C1 0%, #FF8FAB 100%) !important;
        color: white !important;
    }
    
    /* Separadores minimalistas */
    .separador-minimalista {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #FFC1D6, transparent);
        margin: 30px 0;
    }
    
    /* Badges minimalistas */
    .badge-minimalista {
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 400;
        display: inline-block;
    }
    
    .badge-pendiente {
        background: #FFF3E0;
        color: #FF8F00;
        border: 1px solid rgba(255, 143, 0, 0.2);
    }
    
    .badge-confirmado {
        background: #E8F5E9;
        color: #2E7D32;
        border: 1px solid rgba(46, 125, 50, 0.2);
    }
    
    .badge-completado {
        background: #E3F2FD;
        color: #1565C0;
        border: 1px solid rgba(21, 101, 192, 0.2);
    }
    
    .badge-cancelado {
        background: #FFEBEE;
        color: #C62828;
        border: 1px solid rgba(198, 40, 40, 0.2);
    }
    
    /* Footer minimalista */
    .footer-minimalista {
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        color: #7A4A58;
        font-size: 14px;
        opacity: 0.7;
    }
    
    /* Scrollbar minimalista */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: #FFE4EC;
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FFB6C1;
        border-radius: 3px;
    }
    
    </style>
    """, unsafe_allow_html=True)

# ============================================
# CONFIGURACIÓN DE PÁGINA
# ============================================

st.set_page_config(
    page_title="Salón de Belleza - Sistema",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        st.error(f"Error al inicializar el sistema: {e}")
        return None

sistema = inicializar_sistema()

# ============================================
# COMPONENTES REUTILIZABLES
# ============================================

def mostrar_titulo(titulo):
    """Muestra un título minimalista."""
    st.markdown(f'<h1 class="titulo-minimalista">{titulo}</h1>', unsafe_allow_html=True)

def crear_metrica_rosa(label, valor, icono):
    """Crea una métrica con diseño rosa minimalista."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric(label=f"{icono} {label}", value=valor)

def crear_tarjeta_turno_minimalista(turno):
    """Crea una tarjeta minimalista para un turno."""
    servicio = sistema.obtener_servicio_por_id(turno.servicio_id) if sistema else None
    
    color_estado = {
        'pendiente': '#FF8F00',
        'confirmado': '#2E7D32',
        'completado': '#1565C0',
        'cancelado': '#C62828'
    }.get(turno.estado, '#7A4A58')
    
    return f"""
    <div class="tarjeta-minimalista">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div style="flex: 1;">
                <div style="color: #D44D7A; font-weight: 500; margin-bottom: 8px;">
                    {turno.cliente_nombre}
                </div>
                <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                    {turno.fecha} · {turno.hora}
                </div>
                <div style="color: #7A4A58; font-size: 14px; opacity: 0.8;">
                    {servicio.nombre if servicio else 'Servicio'}
                </div>
            </div>
            <div style="text-align: right;">
                <div class="badge-minimalista badge-{turno.estado}" style="color: {color_estado}; border-color: {color_estado}40;">
                    {turno.estado.upper()}
                </div>
            </div>
        </div>
    </div>
    """

def crear_tarjeta_servicio_minimalista(servicio):
    """Crea una tarjeta minimalista para un servicio."""
    colores_categoria = {
        'Uñas': '#FF69B4',
        'Pestañas': '#4169E1',
        'Cejas': '#8A2BE2',
        'Depilación': '#32CD32',
        'Combo': '#FF4500'
    }
    
    color = colores_categoria.get(servicio.categoria, '#FFB6C1')
    
    return f"""
    <div class="tarjeta-minimalista">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div style="flex: 1;">
                <div style="color: {color}; font-weight: 500; margin-bottom: 8px;">
                    {servicio.nombre}
                </div>
                <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                    {servicio.duracion_minutos}min · ${servicio.precio_base}
                </div>
                <div style="display: flex; gap: 8px; margin-top: 8px;">
                    <span style="background: {color}15; color: {color}; padding: 2px 8px; border-radius: 10px; font-size: 12px;">
                        {servicio.categoria}
                    </span>
                    {f'<span style="background: #FFF3E0; color: #FF8F00; padding: 2px 6px; border-radius: 10px; font-size: 11px;">Camilla</span>' if servicio.requiere_camilla else ''}
                </div>
            </div>
        </div>
    </div>
    """

# ============================================
# SIDEBAR MINIMALISTA
# ============================================

# Logo y título
st.sidebar.markdown("""
<div style="text-align: center; padding: 30px 0 20px 0;">
    <div style="font-size: 40px; color: #D44D7A; margin-bottom: 10px;">
        💅
    </div>
    <div style="color: #D44D7A; font-size: 20px; font-weight: 400;">
        Salón de Belleza
    </div>
    <div style="color: #7A4A58; font-size: 12px; margin-top: 4px; opacity: 0.7;">
        Sistema de Gestión
    </div>
</div>
""", unsafe_allow_html=True)

# Separador
st.sidebar.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)

# Menú de navegación
menu_opciones = [
    "🏠 Inicio",
    "📅 Nuevo Turno", 
    "📋 Turnos",
    "💅 Servicios",
    "👩‍💼 Profesionales",
    "📊 Estadísticas",
    "⚙️ Configuración"
]

seleccion = st.sidebar.radio(
    "Navegación",
    options=menu_opciones,
    label_visibility="collapsed",
    index=0
)

# Información del día
st.sidebar.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)

hoy = datetime.now().strftime("%d/%m/%Y")
st.sidebar.markdown(f"""
<div style="text-align: center; padding: 12px; background: white; border-radius: 8px; border: 1px solid #FFC1D6;">
    <div style="color: #D44D7A; font-size: 14px;">
        {hoy}
    </div>
    <div style="color: #7A4A58; font-size: 12px; margin-top: 2px;">
        {datetime.now().strftime('%A')}
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# PÁGINAS PRINCIPALES
# ============================================

def mostrar_inicio():
    """Página de inicio."""
    mostrar_titulo("Inicio")
    
    if not sistema:
        st.error("El sistema no está disponible")
        return
    
    # Estadísticas rápidas
    try:
        stats = sistema.obtener_estadisticas()
        turnos_hoy = len(sistema.obtener_turnos(fecha=datetime.now().strftime("%Y-%m-%d")))
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Turnos Hoy", turnos_hoy)
        
        with col2:
            st.metric("Total Turnos", stats['total_turnos'])
        
        with col3:
            st.metric("Profesionales", stats['profesionales_activos'])
        
        with col4:
            st.metric("Servicios", stats['servicios_disponibles'])
    except:
        pass
    
    st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
    
    # Acciones rápidas
    st.subheader("Acciones Rápidas")
    
    col_acc1, col_acc2, col_acc3 = st.columns(3)
    
    with col_acc1:
        if st.button("Nuevo Turno", use_container_width=True):
            st.session_state['menu_selection'] = "📅 Nuevo Turno"
            st.rerun()
    
    with col_acc2:
        if st.button("Ver Turnos", use_container_width=True):
            st.session_state['menu_selection'] = "📋 Turnos"
            st.rerun()
    
    with col_acc3:
        if st.button("Ver Servicios", use_container_width=True):
            st.session_state['menu_selection'] = "💅 Servicios"
            st.rerun()
    
    # Turnos de hoy
    st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
    st.subheader("Turnos de Hoy")
    
    try:
        turnos_hoy = sistema.obtener_turnos(fecha=datetime.now().strftime("%Y-%m-%d"))
        if turnos_hoy:
            for turno in turnos_hoy[:5]:
                st.markdown(crear_tarjeta_turno_minimalista(turno), unsafe_allow_html=True)
            if len(turnos_hoy) > 5:
                st.caption(f"Y {len(turnos_hoy) - 5} turnos más...")
        else:
            st.info("No hay turnos programados para hoy")
    except:
        st.info("No se pudieron cargar los turnos")

def mostrar_nuevo_turno():
    """Página para crear nuevos turnos."""
    mostrar_titulo("Nuevo Turno")
    
    if not sistema:
        st.error("El sistema no está disponible")
        return
    
    # Formulario en pestañas
    tab1, tab2 = st.tabs(["Turno Individual", "Reserva Múltiple"])
    
    with tab1:
        with st.form("form_turno_individual"):
            st.subheader("Datos del Cliente")
            
            col1, col2 = st.columns(2)
            with col1:
                cliente = st.text_input("Nombre *", placeholder="Nombre completo")
                telefono = st.text_input("Teléfono", placeholder="Número de teléfono")
            
            with col2:
                fecha = st.date_input("Fecha *", min_value=date.today())
                email = st.text_input("Email", placeholder="correo@ejemplo.com")
            
            st.subheader("Servicio")
            
            servicios = sistema.obtener_servicios()
            if servicios:
                # Mostrar servicios por categoría
                categorias = {}
                for servicio in servicios:
                    if servicio.categoria not in categorias:
                        categorias[servicio.categoria] = []
                    categorias[servicio.categoria].append(servicio)
                
                for categoria, servicios_cat in categorias.items():
                    with st.expander(categoria, expanded=True):
                        for servicio in servicios_cat:
                            if st.button(
                                f"{servicio.nombre} (${servicio.precio_base} - {servicio.duracion_minutos}min)",
                                key=f"serv_{servicio.id}",
                                use_container_width=True,
                                type="secondary"
                            ):
                                st.session_state['servicio_seleccionado'] = servicio.id
                                servicio_id = servicio.id
                
                servicio_id = st.session_state.get('servicio_seleccionado')
                
                if servicio_id:
                    servicio = sistema.obtener_servicio_por_id(servicio_id)
                    if servicio:
                        st.success(f"Servicio seleccionado: {servicio.nombre}")
                        
                        # Horario
                        st.subheader("Horario")
                        hora = st.time_input("Hora *", value=datetime.strptime("10:00", "%H:%M"))
                        
                        # Profesional (opcional)
                        st.subheader("Profesional (Opcional)")
                        profesionales = sistema.obtener_profesionales(activos=True)
                        if profesionales:
                            opciones = ["Asignar automáticamente"] + [p['nombre'] for p in profesionales]
                            profesional_sel = st.selectbox("Seleccionar profesional", options=opciones)
            
            # Botón de envío
            if st.form_submit_button("Crear Turno", use_container_width=True, type="primary"):
                if not cliente:
                    st.error("El nombre es obligatorio")
                elif not servicio_id:
                    st.error("Debes seleccionar un servicio")
                else:
                    try:
                        exito, mensaje, turno = sistema.crear_turno(
                            cliente_nombre=cliente,
                            fecha=fecha.strftime("%Y-%m-%d"),
                            hora=hora.strftime("%H:%M"),
                            servicio_id=servicio_id,
                            telefono=telefono,
                            email=email
                        )
                        
                        if exito:
                            st.success(mensaje)
                            st.info(f"ID del turno: {turno.id}")
                            # Limpiar selección
                            if 'servicio_seleccionado' in st.session_state:
                                del st.session_state['servicio_seleccionado']
                        else:
                            st.error(mensaje)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    with tab2:
        st.info("La funcionalidad de reservas múltiples estará disponible próximamente.")

def mostrar_turnos():
    """Página para ver y gestionar turnos."""
    mostrar_titulo("Turnos")
    
    if not sistema:
        st.error("El sistema no está disponible")
        return
    
    # Filtros
    with st.container():
        col_f1, col_f2, col_f3 = st.columns([2, 2, 1])
        
        with col_f1:
            fecha_filtro = st.date_input("Filtrar por fecha", value=None)
        
        with col_f2:
            estado_filtro = st.selectbox(
                "Estado",
                ["Todos", "pendiente", "confirmado", "completado", "cancelado"]
            )
        
        with col_f3:
            st.write("")
            buscar = st.button("Buscar", use_container_width=True)
    
    # Obtener turnos
    try:
        if fecha_filtro:
            turnos = sistema.obtener_turnos(fecha=fecha_filtro.strftime("%Y-%m-%d"))
        else:
            turnos = sistema.obtener_turnos()
        
        if estado_filtro != "Todos":
            turnos = [t for t in turnos if t.estado == estado_filtro]
        
        if not turnos:
            st.info("No se encontraron turnos")
        else:
            # Contadores
            estados_count = {}
            for turno in turnos:
                estados_count[turno.estado] = estados_count.get(turno.estado, 0) + 1
            
            col_c1, col_c2, col_c3, col_c4 = st.columns(4)
            with col_c1: st.metric("Total", len(turnos))
            with col_c2: st.metric("Pendientes", estados_count.get('pendiente', 0))
            with col_c3: st.metric("Confirmados", estados_count.get('confirmado', 0))
            with col_c4: st.metric("Completados", estados_count.get('completado', 0))
            
            st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
            
            # Lista de turnos
            for turno in turnos:
                col_t1, col_t2 = st.columns([4, 1])
                
                with col_t1:
                    st.markdown(crear_tarjeta_turno_minimalista(turno), unsafe_allow_html=True)
                
                with col_t2:
                    # Acciones
                    if turno.estado == "pendiente":
                        if st.button("✅", key=f"conf_{turno.id}", help="Confirmar"):
                            try:
                                exito, mensaje = sistema.confirmar_turno(str(turno.id))
                                if exito:
                                    st.success(mensaje)
                                    st.rerun()
                            except:
                                pass
                        
                        if st.button("❌", key=f"canc_{turno.id}", help="Cancelar"):
                            try:
                                exito, mensaje = sistema.cancelar_turno(str(turno.id))
                                if exito:
                                    st.success(mensaje)
                                    st.rerun()
                            except:
                                pass
                    
                    if st.button("🗑️", key=f"del_{turno.id}", help="Eliminar"):
                        try:
                            # Eliminar turno
                            st.warning("Eliminar turno")
                        except:
                            pass
                
                # Detalles expandibles
                with st.expander("Detalles", expanded=False):
                    col_d1, col_d2 = st.columns(2)
                    with col_d1:
                        st.write("**Cliente:**", turno.cliente_nombre)
                        st.write("**Teléfono:**", turno.telefono)
                        st.write("**Email:**", turno.email)
                    with col_d2:
                        st.write("**Fecha:**", turno.fecha)
                        st.write("**Hora:**", turno.hora)
                        st.write("**ID:**", turno.id)
                
                st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Error al cargar turnos: {str(e)}")

def mostrar_servicios():
    """Página para ver servicios."""
    mostrar_titulo("Servicios")
    
    if not sistema:
        st.error("El sistema no está disponible")
        return
    
    try:
        servicios = sistema.obtener_servicios()
        
        if not servicios:
            st.info("No hay servicios disponibles")
            return
        
        # Agrupar por categoría
        categorias = {}
        for servicio in servicios:
            if servicio.categoria not in categorias:
                categorias[servicio.categoria] = []
            categorias[servicio.categoria].append(servicio)
        
        # Mostrar por categoría
        for categoria, servicios_cat in categorias.items():
            st.subheader(categoria)
            for servicio in servicios_cat:
                st.markdown(crear_tarjeta_servicio_minimalista(servicio), unsafe_allow_html=True)
        
        # Estadísticas
        st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
        
        col_s1, col_s2, col_s3 = st.columns(3)
        
        with col_s1:
            st.metric("Total Servicios", len(servicios))
        
        with col_s2:
            st.metric("Categorías", len(categorias))
        
        with col_s3:
            duracion_promedio = sum(s.duracion_minutos for s in servicios) / len(servicios)
            st.metric("Duración Promedio", f"{duracion_promedio:.0f} min")
    
    except Exception as e:
        st.error(f"Error al cargar servicios: {str(e)}")

def mostrar_profesionales():
    """Página para ver profesionales."""
    mostrar_titulo("Profesionales")
    
    if not sistema:
        st.error("El sistema no está disponible")
        return
    
    try:
        profesionales = sistema.obtener_profesionales(activos=True)
        
        if not profesionales:
            st.info("No hay profesionales activos")
            return
        
        for profesional in profesionales:
            color = profesional.get('color_calendario', '#FFB6C1')
            
            col1, col2 = st.columns([1, 3])
            
            with col1:
                # Avatar simple
                st.markdown(f"""
                <div style="text-align: center;">
                    <div style="width: 60px; height: 60px; border-radius: 50%; 
                                background: {color};
                                display: flex; align-items: center; justify-content: center;
                                margin: 0 auto; color: white; font-size: 24px; font-weight: 300;">
                        {profesional['nombre'][0]}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="tarjeta-minimalista">
                    <div style="color: {color}; font-weight: 500; margin-bottom: 8px;">
                        {profesional['nombre']}
                    </div>
                    <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                        ID: {profesional['id']}
                    </div>
                    <div style="color: #7A4A58; font-size: 14px; opacity: 0.8;">
                        {len(profesional.get('especialidades', []))} especialidades
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Error al cargar profesionales: {str(e)}")

def mostrar_estadisticas():
    """Página de estadísticas."""
    mostrar_titulo("Estadísticas")
    
    if not sistema:
        st.error("El sistema no está disponible")
        return
    
    try:
        stats = sistema.obtener_estadisticas()
        
        # Métricas principales
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Turnos Totales", stats['total_turnos'])
        
        with col2:
            st.metric("Turnos Futuros", stats['turnos_futuros'])
        
        with col3:
            st.metric("Servicios Activos", stats['servicios_disponibles'])
        
        st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
        
        # Distribución por estado
        st.subheader("Distribución por Estado")
        
        if stats['estados']:
            col_e1, col_e2, col_e3, col_e4 = st.columns(4)
            
            estados = stats['estados']
            with col_e1: st.metric("Pendientes", estados.get('pendiente', 0))
            with col_e2: st.metric("Confirmados", estados.get('confirmado', 0))
            with col_e3: st.metric("Completados", estados.get('completado', 0))
            with col_e4: st.metric("Cancelados", estados.get('cancelado', 0))
        
        st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
        
        # Servicios más populares
        st.subheader("Servicios Más Populares")
        
        if stats.get('servicios'):
            servicios_populares = []
            for servicio_id, cantidad in stats['servicios'].items():
                servicio = sistema.obtener_servicio_por_id(servicio_id)
                if servicio:
                    servicios_populares.append((servicio.nombre, cantidad))
            
            servicios_populares.sort(key=lambda x: x[1], reverse=True)
            
            for nombre, cantidad in servicios_populares[:5]:
                st.write(f"• {nombre}: {cantidad} turnos")
    
    except Exception as e:
        st.error(f"Error al cargar estadísticas: {str(e)}")

def mostrar_configuracion():
    """Página de configuración."""
    mostrar_titulo("Configuración")
    
    st.info("Configuración del sistema")
    
    # Información del sistema
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown("""
        <div class="tarjeta-minimalista">
            <div style="color: #D44D7A; font-weight: 500; margin-bottom: 12px;">
                Sistema
            </div>
            <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                Versión: 1.0.0
            </div>
            <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                Diseño: Minimalista Rosa
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_info2:
        try:
            if sistema:
                stats = sistema.obtener_estadisticas()
                st.markdown(f"""
                <div class="tarjeta-minimalista">
                    <div style="color: #D44D7A; font-weight: 500; margin-bottom: 12px;">
                        Estadísticas
                    </div>
                    <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                        Turnos: {stats['total_turnos']}
                    </div>
                    <div style="color: #7A4A58; font-size: 14px; margin-bottom: 4px;">
                        Servicios: {stats['servicios_disponibles']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        except:
            pass
    
    # Herramientas
    st.markdown('<div class="separador-minimalista"></div>', unsafe_allow_html=True)
    st.subheader("Herramientas")
    
    col_her1, col_her2 = st.columns(2)
    
    with col_her1:
        if st.button("Recargar Datos", use_container_width=True):
            st.rerun()
    
    with col_her2:
        if st.button("Limpiar Cache", use_container_width=True):
            st.cache_resource.clear()
            st.rerun()

# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

def main():
    """Función principal."""
    
    # Mapeo de páginas
    paginas = {
        "🏠 Inicio": mostrar_inicio,
        "📅 Nuevo Turno": mostrar_nuevo_turno,
        "📋 Turnos": mostrar_turnos,
        "💅 Servicios": mostrar_servicios,
        "👩‍💼 Profesionales": mostrar_profesionales,
        "📊 Estadísticas": mostrar_estadisticas,
        "⚙️ Configuración": mostrar_configuracion
    }
    
    # Ejecutar página seleccionada
    if seleccion in paginas:
        paginas[seleccion]()
    else:
        mostrar_inicio()
    
    # Footer
    st.markdown("""
    <div class="footer-minimalista">
        Salón de Belleza · Sistema de Gestión · Versión 1.0
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()