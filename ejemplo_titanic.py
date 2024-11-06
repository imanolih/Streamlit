import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with st.container():
    st.title("REDIRIGIDOR DE PAGINAS WEB")
    st.subheader("Podras dirigirte a las paginas mas utilizadas")
with st.container():
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("youtube-logo-youtube-icon-transparent-free-png.webp")
    st.write("YOUTUBE")
with col2:
    st.image("whatsapp-logo-whatsapp-icon-whatsapp-transparent-free-png.webp")
    st.write("WHATSAPP")
with col3:
    st.image("facebook-logo-facebook-icon-transparent-free-png.webp")
    st.write("FACEBOOK")
with col4:
    st.image("")
    st.write("GITHUB")
      
  
    
  
  
