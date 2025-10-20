import reflex as rx
import datetime
from Portfolio.styles.styles import Size as Size
from Portfolio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Copyright © 2025 Luis Sierra Corvalán", 
            font_size=Size.MEDIUM.value
            ),
        rx.text(
            "Todos los derechos reservados", 
            font_size=Size.MEDIUM.value
            ),
        align_items="center",
        text_align="center",
        spacing="1",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value
    )
