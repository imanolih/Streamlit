import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with st.container():
    st.title("REDIRIGIDOR DE PAGINAS WEB")
    st.subheader("Podras dirigirte a las paginas mas utilizadas")

with st.container():
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)

# Agregar contenido a cada columna
with col1:
    st.image("youtube-logo-youtube-icon-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>YOUTUBE</div>", unsafe_allow_html=True)

with col2:
    st.image("whatsapp-logo-whatsapp-icon-whatsapp-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>WHATSAPP</div>", unsafe_allow_html=True)

with col3:
    st.image("facebook-logo-facebook-icon-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>FACEBOOK</div>", unsafe_allow_html=True)

with col4:
    st.image("twitter-logo-twitter-icon-transparent-free-png.webp")
    st.markdown("<div style='text-align: center;'>TWITTER</div>", unsafe_allow_html=True)

    
  
  
