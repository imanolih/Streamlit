import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
with st.container():
  st.title("mi pagina web")
# Usamos HTML para alinear el título a la izquierda
with st.container():
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_input = st.sidebar.text_input("Email")
  user_input = st.sidebar.text_input("Contraseña")
  st.markdown("""
    <style>
        /* Cambiar el color de fondo del sidebar */
        .css-1d391kg {
            background-color: #4CAF50; /* Cambia el color aquí */
        }
        
        /* Cambiar el color del texto en el sidebar */
        .css-1d391kg .sidebar .sidebar-content {
            color: white; /* Cambia el color del texto */
        }

        /* Cambiar el color del título en el sidebar */
        .css-1d391kg .sidebar .sidebar-header {
            color: white;
        }

        /* Cambiar el color del borde del sidebar */
        .css-1d391kg {
            border-right: 2px solid #3e8e41;  /* Cambia el color del borde */
        }

        /* Cambiar el color del fondo cuando se hace hover sobre un elemento */
        .css-1d391kg .sidebar .sidebar-content .element-container:hover {
            background-color: #45a049; /* Cambiar el color de hover */
        }
    </style>
""", unsafe_allow_html=True)
  
    
  
  
