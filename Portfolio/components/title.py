from turtle import width
import reflex as rx
import Portfolio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="3",
        style=styles.title_style
    )