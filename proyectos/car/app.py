import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 
if st.button("Generar Gráfico de Dispersión"): # Código para generar el gráfico de dispersión aquí
    # Genera datos aleatorios para el gráfico de dispersión
    df = px.car_data.iris()

    # Crea el gráfico de dispersión
    scatter_fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Gráfico de Dispersión")

    # Muestra el gráfico utilizando st.plotly_chart()
    st.plotly_chart(scatter_fig)