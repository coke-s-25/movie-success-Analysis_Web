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
success_prediction_button = st.sidebar.button("Movie Predictions")

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
    st.write("")
    st.write("Sources:")
    st.markdown("[The Numbers](https://www.the-numbers.com/)")
    st.image("graficos2/The Numbers.png",  width=300 )
    st.write("")
    st.markdown("[IMDb](https://www.imdb.com/es/)")
    st.image("graficos2/IMDb.png",  width=200 )

elif st.session_state.page == "Variable Analysis":
    st.markdown("""
        <div class="title">
            Variable Analysis & Box Office Trends
        </div>
    """, unsafe_allow_html=True)
    
    # Crear los dos dropdowns
    opcion1 = st.selectbox("What to study?", ["Profitability (> 0 ROI)", "Success (> 1.5 ROI)"])
    opcion2 = st.selectbox("What variable?", ["Budget","Creative Type","Distributor Type","Franchise","Genre","Month","Mpaa Rating","Release Year","Running Time"])
    
    # Diccionario que mapea combinaciones a rutas de gráficos
    graficos = {
        ("Profitability (> 0 ROI)", "Budget"): "graficos2/Budget1.png",
        ("Success (> 1.5 ROI)", "Budget"): "graficos2/Budget.png",
        ("Profitability (> 0 ROI)", "Creative Type"): "graficos2/Creative Type1.png",
        ("Success (> 1.5 ROI)", "Creative Type"): "graficos2/Creative Type.png",
        ("Profitability (> 0 ROI)", "Distributor Type"): "graficos2/Distributor Type1.png",
        ("Success (> 1.5 ROI)", "Distributor Type"): "graficos2/Distributor Type.png",
        ("Profitability (> 0 ROI)", "Franchise"): "graficos2/Franchise1.png",
        ("Success (> 1.5 ROI)", "Franchise"): "graficos2/Franchise.png",
        ("Profitability (> 0 ROI)", "Genre"): "graficos2/Genre1.png",
        ("Success (> 1.5 ROI)", "Genre"): "graficos2/Genre.png",
        ("Profitability (> 0 ROI)", "Month"): "graficos2/Month1.png",
        ("Success (> 1.5 ROI)", "Month"): "graficos2/Month.png",
        ("Profitability (> 0 ROI)", "Mpaa Rating"): "graficos2/Mpaa Rating1.png",
        ("Success (> 1.5 ROI)", "Mpaa Rating"): "graficos2/Mpaa Rating.png",
        ("Profitability (> 0 ROI)", "Release Year"): "graficos2/Release Year1.png",
        ("Success (> 1.5 ROI)", "Release Year"): "graficos2/Release Year.png",
        ("Profitability (> 0 ROI)", "Running Time"): "graficos2/Running Time1.png",
        ("Success (> 1.5 ROI)", "Running Time"): "graficos2/Running Time.png",
    }
    
    # Obtener la ruta del gráfico según la selección
    grafico_path = graficos.get((opcion1, opcion2))
    
    # Mostrar el gráfico seleccionado
    if grafico_path:
        st.image(grafico_path,  use_container_width=True )
    else:
        st.write("No hay gráfico disponible para esta combinación.")
    

elif st.session_state.page == "Success Prediction":
    st.markdown("""
        <div class="title">
            Movie Predictions
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("About our model:")
    st.image("graficos2/predictions_variables.png",  use_container_width=True )
    opcion1 = st.selectbox("What movie do you want to study?", ["Profitability (> 0 ROI)", "Success (> 1.5 ROI)"])

