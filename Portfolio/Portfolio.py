import reflex as rx
from Portfolio.components.navbar import navbar
from Portfolio.views.header.header import header
from Portfolio.views.links.links import links
from Portfolio.components.footer import footer
from Portfolio.components.cuerpo import cuerpo
import Portfolio.styles.styles as styles
from Portfolio.styles.styles import Size as Size
from Portfolio.styles.styles import STYLESHEETS as stylesheets

#class State(rx.State):
#    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                cuerpo(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        rx.center(footer())
    )

app = rx.App(
    enable_state=False,
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Portafolio de Luis Sierra",

)
