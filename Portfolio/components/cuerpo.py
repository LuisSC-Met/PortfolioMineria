from Portfolio.styles.styles import Size
from Portfolio.styles.colors import Color, TextColor
import reflex as rx

def cuerpo() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Proyectos", 
            font_size=Size.LARGE.value,
            color=TextColor.HEADER.value
        ),
        rx.text(
            "Reportabilidad de minerales de óxidos",
            color=TextColor.HEADER.value
        ),
        rx.text("""
            Proyecto de reportabilidad de minerales de óxidos provenientes de la correa de alimentación,
            realizado en Power BI. Se realiza una transformación de datos proveniente de un archivo Excel historico
            que se utilizaba como reporte de datos diario, el cual consiste fundamentalmente en el p80 obtenido de un
            análisis granulométrico y el Cobre total y soluble obtenido de un análisis químico.
        """,
            color=TextColor.HEADER.value
        ),
                
                # Visualización de Power BI embebida usando HTML
        rx.html(
            """
            <iframe 
                title="Reportabilidad Oxidos" 
                width="800" 
                height="541.25"
                src="https://app.powerbi.com/reportEmbed?reportId=c8038ee6-c282-40ad-980f-f9c998a97e38&autoAuth=true&ctid=d027c8a2-216a-47c0-b70b-0788758751c1" 
                frameborder="0" 
                allowFullScreen="true">
            </iframe>
            """,
            dangerously_set_inner_html=True
        ),

        rx.text("""
            El objetivo principal fue transformar grandes volúmenes de datos en una herramienta visual y dinámica 
            que facilite el seguimiento de indicadores clave y la identificación de tendencias operativas.
        """,
            color=TextColor.HEADER.value
        ),
        rx.text("""
            La estructura se diseñó con un enfoque donde la tabla de hechos concentra los registros 
            diarios de p80, CuT y CuS, mientras que los graficos extras contienen información complementaria entre ellos,
            como fechas, turnos día y noche o cantidad de muestra, las cuales son añadidadas, además, como herramiantes. 
        """,
            color=TextColor.HEADER.value
        ),
        margin_top=Size.LARGE.value
    )

