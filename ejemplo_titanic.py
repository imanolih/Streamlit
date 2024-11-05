import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with st.container():
    imagen = "images.png"
    st.image(imagen, use_column_width=True)
    st.title("Página con Imagen de Portada")
    st.write("Este es un ejemplo de cómo colocar una imagen en la parte superior que ocupe toda la anchura de la página.")

with st.container():
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_input = st.sidebar.text_input("Email")
  user_input = st.sidebar.text_input("Contraseña")
  
  
    
  
  
