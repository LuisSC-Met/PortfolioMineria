import reflex as rx
import Portfolio.styles.styles as styles
from Portfolio.styles.styles import Size as Size

def link_button(text: str, url: str, image: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    align_items="start",
                    justify_content="center",
                    spacing="1",
                    margin="1",
                    padding_right="1"
                ),
                width="100%",
                align_items="center",
                justify_content="start"
            ),
            style={"text_align": "left"}
        ),
        href=url,
        is_external=True,
        width="100%"
    )