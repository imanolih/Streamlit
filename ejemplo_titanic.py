import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
with st.container():
  st.title("mi pagina web")
# Usamos HTML para alinear el título a la izquierda
with st.container():
  st.sidebar.title("mi titulo lateral")
  st.sidebar.image('2021_Facebook_icon.svg.png')
  user_imput = st.sidebar.text_input("Ingrese su Email")
  st.sidebar.write("ingrese su email", user_imput)
    
  
  
