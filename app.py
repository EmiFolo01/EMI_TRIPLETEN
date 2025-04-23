import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis Exploratorio de Datos de Vehículos')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma del Odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre Odometer y Precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odometer y Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
