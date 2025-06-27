import pandas as pd
import streamlit as st

def analizar_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)
    st.write("Vista previa de los datos:")
    st.dataframe(df.head())

    # Aquí podés llamar al test estadístico que quieras, por ejemplo:
    st.write("Estadísticas descriptivas:")
    st.write(df.describe())
