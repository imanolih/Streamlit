import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
paginas_disponibles = [
    "youtube", "whatsapp", "facebook", "twitter", "instagram", 
    "linkedin", "pinterest", "amazon", "ebay", "netflix", "spotify", "wikipedia", "google", "gmail", "outlook", "dropbox", "github",
]
paginas_disponibles = {
    "youtube": "https://www.youtube.com",
    "whatsapp": "https://web.whatsapp.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "tiktok": "https://www.tiktok.com",
    "pinterest": "https://www.pinterest.com",
    "reddit": "https://www.reddit.com",
    "snapchat": "https://www.snapchat.com",
    "amazon": "https://www.amazon.com",
    "ebay": "https://www.ebay.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://www.spotify.com",
    "wikipedia": "https://www.wikipedia.org",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "yahoo": "https://www.yahoo.com",
    "bing": "https://www.bing.com",
    "outlook": "https://outlook.live.com",
    "zoom": "https://zoom.us",
    "dropbox": "https://www.dropbox.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "twitch": "https://www.twitch.tv"
}

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
    st.sidebar.title("SELECCIONAR PAGINA")
    st.sidebar.write("---")
    seleccion_pagina = st.sidebar.selectbox("Selecciona una página disponible:", paginas_disponibles)
    if seleccion_pagina:
        url = paginas_disponibles[seleccion_pagina]
        st.markdown(f"[Ir a {seleccion_pagina.capitalize()}]({url})", unsafe_allow_html=True)
        st.success(f"Has seleccionado la página: '{seleccion_pagina}'.")
        
    
  
