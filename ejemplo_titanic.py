import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
paginas_disponibles = [
    "youtube", "whatsapp", "facebook", "twitter", "instagram", 
    "linkedin", "pinterest", "amazon", "ebay", "netflix", "spotify", "wikipedia", "google", "gmail", "outlook", "dropbox", "github",
]

with st.container():
    st.title("REDIRIGIDOR DE PAGINAS WEB")
    st.subheader("Podras dirigirte a las paginas mas utilizadas")

with st.container():
    st.write("---")
    col1, col2, col3 = st.columns(3)
with col1:
    st.image("youtube-logo-youtube-icon-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>YOUTUBE</div>", unsafe_allow_html=True)

with col2:
    st.image("whatsapp-logo-whatsapp-icon-whatsapp-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>WHATSAPP</div>", unsafe_allow_html=True)

with col3:
    st.image("facebook-logo-facebook-icon-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>FACEBOOK</div>", unsafe_allow_html=True)
with st.container():
    st.sidebar.title("MAS OPCIONES")
    st.sidebar.write("---")
    buscar = st.sidebar.text_input("Buscar página:", placeholder="Escribe el nombre de la página...")
if buscar:
    if buscar.lower() in paginas_disponibles:
        st.success(f"La página está disponible.")
    else:
        st.error(f"La página no está en la lista de páginas disponibles.")
with st.container():
    st.sidebar.write("---")
    seleccion_pagina = st.selectbox("Selecciona una página disponible:", paginas_disponibles)
    
    
  
