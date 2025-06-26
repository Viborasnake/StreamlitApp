import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
from analisis import analizar_csv
from visualizaciones.plot_medias import plot_medias
from visualizaciones.plot_proporciones import plot_proporciones
from visualizaciones.plot_ab import plot_ab
from visualizaciones.plot_chi2 import plot_chi2
from visualizaciones.plot_anova import plot_anova

st.set_page_config(page_title="UX Matrix Stats", layout="wide")

st.title("📊 UX Matrix Statistics App")
st.markdown("Analiza automáticamente tu CSV y genera insights con respaldo estadístico.")

uploaded_file = st.file_uploader("📂 Sube tu archivo CSV", type=["csv"])

if uploaded_file:
    st.success("Archivo cargado correctamente.")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = Path(tmp_file.name)

    st.markdown("### ⏳ Ejecutando análisis...")

    try:
        resultado = analizar_csv(tmp_path)
        test = resultado["test"]
        stat = resultado["estadistico"]
        p = resultado["p_valor"]
        conclusion = resultado["conclusion"]
        reflexion = resultado["reflexion"]
        descripcion = resultado["descripcion_grafico"]

        st.subheader(f"🧪 Resultado del test: {test}")
        st.markdown(f"**Estadístico:** {stat:.4f}  \n**p-valor:** {p:.4f}")
        st.markdown(f"### ✅ Conclusión: {conclusion}")
        st.info(reflexion)

        # Visualización según test
        st.markdown("### 📈 Gráfico del análisis")

        df = pd.read_csv(tmp_path)
        fig = None

        if test == "t-test de medias":
            variantes = df["variante"]
            valores = df["valor"]
            fig = plot_medias(variantes, valores)
        elif test == "z-test de proporciones":
            fig = plot_proporciones(df)
        elif test == "chi-cuadrado":
            fig = plot_chi2(df)
        elif test == "test A/B de proporciones":
            fig = plot_ab(df)
        elif test == "ANOVA de medias":
            variantes = df["variante"]
            valores = df["valor"]
            fig = plot_anova(variantes, valores)

        if fig:
            st.pyplot(fig)
            st.caption(descripcion)

    except Exception as e:
        st.error(f"Ocurrió un error durante el análisis: {e}")