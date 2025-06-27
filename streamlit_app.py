import streamlit as st
from analisis.analizar_csv import analizar_csv, generar_informe_html
import tempfile
from weasyprint import HTML

st.title("UX Matrix Statistics - Análisis de Experimentos")

uploaded_file = st.file_uploader("Sube un archivo CSV de datos", type=["csv"])
if uploaded_file:
    df, resumen, nombre_grafico = analizar_csv(uploaded_file)

    # Generar HTML del informe
    html_informe = generar_informe_html(df, resumen, nombre_grafico)

    # Mostrar informe en pantalla
    st.markdown("### 📄 Informe automatizado")
    st.components.v1.html(html_informe, height=800, scrolling=True)

    # Generar PDF temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        HTML(string=html_informe, base_url=".").write_pdf(tmp_pdf.name)
        tmp_pdf_path = tmp_pdf.name

    # Descargar
    with open(tmp_pdf_path, "rb") as f:
        pdf_bytes = f.read()
        st.download_button(
            label="⬇️ Descargar informe en PDF",
            data=pdf_bytes,
            file_name="informe_ux_automatizado.pdf",
            mime="application/pdf"
        )
