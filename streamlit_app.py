import streamlit as st
import pandas as pd
from analisis.analizar_csv import analizar_csv

st.set_page_config(page_title="UX Matrix Statistics", layout="wide")
st.title("UX Matrix Statistics - Análisis de Experimentos")

uploaded_file = st.file_uploader("📁 Sube un archivo CSV de datos", type=["csv"])
if uploaded_file is not None:
    st.success("✅ Archivo recibido. Procesando...")
    analizar_csv(uploaded_file)