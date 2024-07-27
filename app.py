import streamlit as st
import pandas as pd
import plotly_express as px

df_car_data = pd.read_csv('../vehicles_us.csv')
hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(df_car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión plotly-express. 
# Nuevamente, considera utilizar las funciones st.write() y st.plotly_chart().