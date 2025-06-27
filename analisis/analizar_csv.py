from weasyprint import HTML
from jinja2 import Template
import tempfile
import base64

def generar_informe_html(df, resumen, nombre_grafico):
    template = Template("""
    <html>
    <head>
        <style>
            body { font-family: sans-serif; padding: 40px; color: #333; }
            h1 { color: #004080; }
            .bloque { margin-bottom: 20px; }
            .grafico img { max-width: 100%; height: auto; }
        </style>
    </head>
    <body>
        <h1>Análisis automático de datos UX</h1>
        <div class="bloque"><strong>Estadístico:</strong> {{ resumen["estadistico"] }}</div>
        <div class="bloque"><strong>Valor p:</strong> {{ resumen["p_valor"] }}</div>
        <div class="bloque"><strong>Conclusión:</strong> {{ resumen["conclusion"] }}</div>
        <hr>
        <div class="bloque"><h3>Reflexión automatizada del análisis</h3>{{ resumen["reflexion"] }}</div>
        <div class="bloque"><h3>¿Qué significa este test?</h3>{{ resumen["significado"] }}</div>
        <div class="bloque"><h3>Descripción del gráfico</h3>{{ resumen["descripcion_grafico"] }}</div>
        <div class="grafico"><img src="{{ nombre_grafico }}"></div>
    </body>
    </html>
    """)
    return template.render(resumen=resumen, nombre_grafico=nombre_grafico)
