from ctypes import alignment
from Portfolio.styles.fonts import FontWeight
import reflex as rx
from Portfolio.components.link_icon import link_icon
from Portfolio.components.info_text import info_text
from Portfolio.components.title import title
from Portfolio.styles.styles import Size as Size, Spacing
from Portfolio.styles.colors import Color as Color
from Portfolio.styles.colors import TextColor as TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Luis Sierra",
                    src="/avatar.jpg",
                    size=Spacing.MEDIUM_BIG.value, 
                    radius="full",
                ),
            border=f"4px solid {Color.PRIMARY.value}",
            border_radius="9999px",
            padding="2px",  # Espacio entre el avatar y el borde
            width="fit-content"
            ),
            rx.vstack(
                rx.heading(
                    "Luis Sierra Corvalán",
                    size=Spacing.BIG.value,
                    font_weight=FontWeight.BOLD.value,
                    color=TextColor.BODY.value,
                    bg=Color.BACKGROUND.value,
                    )
                ),
                align_items="center",
                spacing=Spacing.SMALL.value
            ),
        rx.text("Soy Ingeniero de Ejecución en Metalurgía desde hace más de 6 años. Actualmente trabajo como Supervisor de un Laboratorio Metalúrgico. Además, desarrollo proyectos de análisis y visualización de datos enfocados en minería.",
        color=TextColor.BODY.value,
        font_size=Size.MEDIUM.value),
        rx.text("Aquí podras encontrar todos los enlaces de interés, así como también algunos proyectos que he realizado, saludos!",
        color=TextColor.BODY.value,
        font_size=Size.MEDIUM.value),
        spacing="3",
        align_items="start"
    )