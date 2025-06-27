
import streamlit as st
from analisis.analizar_csv import analizar_csv
#Esto es un mensaje
st.title("UX Matrix Statistics - Análisis de Experimentos")

uploaded_file = st.file_uploader("Sube un archivo CSV de datos", type=["csv"])
if uploaded_file is not None:
    analizar_csv(uploaded_file)
