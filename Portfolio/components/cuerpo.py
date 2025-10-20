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
                src="https://app.powerbi.com/view?r=TU_REPORT_ID_AQUI" 
                width="100%" 
                height="600px" 
                frameborder="0" 
                style="border: none; margin: 1em 0;">
            </iframe>
            """
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
