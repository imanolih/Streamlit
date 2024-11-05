import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with st.container():
  st.markdown("""
    <style>
        .header {
            background-image: url('images.png'); /* URL de la imagen */
            background-size: cover; /* La imagen cubrirá toda la zona */
            background-position: center; /* Centrar la imagen */
            height: 300px; /* Altura de la imagen (ajusta según lo que necesites) */
            width: 100%; /* Asegura que la imagen ocupe todo el ancho */
        }
    </style>
""", unsafe_allow_html=True)
  titulo = st.text_input("Escribe el título de la página:", "Título predeterminado")
  st.title("mi pagina web")
with st.container():
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_input = st.sidebar.text_input("Email")
  user_input = st.sidebar.text_input("Contraseña")
  
  
    
  
  
