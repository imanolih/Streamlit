import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with st.container():
import streamlit as st

# Inyectar CSS para colocar la imagen de portada en la parte superior
st.markdown("""
    <style>
        .header {
            background-image: url(''); /* URL de la imagen */
            background-size: cover; /* La imagen cubrirá toda la zona */
            background-position: center; /* Centrar la imagen */
            height: 300px; /* Altura de la imagen (ajusta según lo que necesites) */
            width: 100%; /* Asegura que la imagen ocupe todo el ancho */
        }
    </style>
""", unsafe_allow_html=True)

# Crear un contenedor para la imagen de portada
st.markdown('<div class="header"></div>', unsafe_allow_html=True)

# Agregar más contenido a la página
st.title("Página con Imagen de Portada")
st.write("Este es un ejemplo de cómo colocar una imagen en la parte superior que ocupe toda la anchura de la página.")

with st.container():
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_input = st.sidebar.text_input("Email")
  user_input = st.sidebar.text_input("Contraseña")
  
  
    
  
  
