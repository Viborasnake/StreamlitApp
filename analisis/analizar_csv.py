import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

def analizar_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Vista previa de los datos:")
    st.dataframe(df)

    st.subheader("📊 Estadísticas descriptivas:")
    st.dataframe(df.describe())

    columnas = df.columns.tolist()
    if "variante" in columnas:
        variable_numerica = [col for col in columnas if col != "variante"]
        if variable_numerica:
            col_numerica = variable_numerica[0]

            st.subheader(f"📈 Distribución de {col_numerica} por variante")
            fig, ax = plt.subplots()
            sns.boxplot(x="variante", y=col_numerica, data=df, palette="Set2", ax=ax)
            st.pyplot(fig)