import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
with st.container():
  st.markdown("""
    <style>
        /* Cambiar el color de fondo de la parte principal de la página */
        .main {
            background-color: #f0f0f5; /* Cambia el color de fondo aquí */
        }

        /* Cambiar el color del texto en la parte principal de la página */
        .main .block-container {
            color: #333333; /* Cambia el color del texto */
        }

        /* Cambiar el color del borde de la parte principal (si es necesario) */
        .main {
            border: 1px solid #dcdcdc;
        }
    </style>
""", unsafe_allow_html=True)
  st.title("mi pagina web")
# Usamos HTML para alinear el título a la izquierda
with st.container():
  
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_input = st.sidebar.text_input("Email")
  user_input = st.sidebar.text_input("Contraseña")
  
  
    
  
  
