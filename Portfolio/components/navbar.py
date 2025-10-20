import reflex as rx
import Portfolio.styles.styles as styles
from Portfolio.styles.styles import Size as Size
from Portfolio.styles.colors import Color as Color
from Portfolio.styles.colors import TextColor as TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Análisis de datos en Minería",
            color=Color.PRIMARY.value,
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )