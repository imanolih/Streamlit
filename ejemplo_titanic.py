import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
with st.container():
  titulo = st.text_input("Escribe el título de la página:", "Título predeterminado")
  st.title("mi pagina web")
with st.container():
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_input = st.sidebar.text_input("Email")
  user_input = st.sidebar.text_input("Contraseña")
  
  
    
  
  
