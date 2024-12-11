import streamlit as st

# Estilo para el título y el subtítulo
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 45px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            font-style: italic;
        }
    </style>
""", unsafe_allow_html=True)

# Crear el sidebar con botones para navegar
st.sidebar.title("Navigation")
home_button = st.sidebar.button("Home")
variable_analysis_button = st.sidebar.button("Variable Analysis")
success_prediction_button = st.sidebar.button("Success Prediction")

# Usar una variable de estado para mantener la página activa
if 'page' not in st.session_state:
    st.session_state.page = "Home"  # Inicializar la página en Home por defecto

# Cambiar la página según el botón presionado
if home_button:
    st.session_state.page = "Home"
elif variable_analysis_button:
    st.session_state.page = "Variable Analysis"
elif success_prediction_button:
    st.session_state.page = "Success Prediction"

# Páginas del Dashboard
if st.session_state.page == "Home":
    st.markdown("""
        <div class="title">
            Movie Success Prediction
        </div>
        <div class="subtitle">
            Created by: Ali Alhaj Hassan, Ana Real, Amelia Lane, Jorge Saurina
        </div>
    """, unsafe_allow_html=True)
    
    # Contenido de la página Home
    st.write("")
    st.write("")
    st.write("Welcome to the home page! Here you can navigate to different analyses.")

elif st.session_state.page == "Variable Analysis":
    st.markdown("""
        <div class="title">
            Variable Analysis & Box Office Success Trends
        </div>
    """, unsafe_allow_html=True)
    
    # Crear los dos dropdowns
    opcion1 = st.selectbox("What to study?", ["Profitability (> 0 ROI)", "Success (> 1.5 ROI)"])
    opcion2 = st.selectbox("What variable?", ["Budget","Creative Type","Distributor Type","Franchise","Genre","Month","Mpaa Rating","Release Year","Running Time"])
    
    # Diccionario que mapea combinaciones a rutas de gráficos
    graficos = {
        ("Profitability (> 0 ROI)", "Budget"): "graficos/Budget1.png",
        ("Success (> 1.5 ROI)", "Budget"): "graficos/Budget.png",
        # Añade más combinaciones según tus gráficos
    }
    
    # Obtener la ruta del gráfico según la selección
    grafico_path = graficos.get((opcion1, opcion2))
    
    # Mostrar el gráfico seleccionado
    if grafico_path:
        st.image(grafico_path, caption=f"Gráfico para {opcion1} y {opcion2}",  width=500 )
    else:
        st.write("No hay gráfico disponible para esta combinación.")
    

elif st.session_state.page == "Success Prediction":
    st.title("Success Prediction")
    st.write("Contenido de predicción de éxito...")

