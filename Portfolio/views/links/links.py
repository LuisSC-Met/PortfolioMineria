import reflex as rx
from Portfolio.components.link_button import link_button
from Portfolio.components.title import title

def links() -> rx.Component:
    return rx.hstack(
        link_button(
            "Curriculum Vitae",
            "https://drive.google.com/file/d/1dDBAeZwi_r91NJ5inGTuSAvmRuGVdARN/view?usp=drive_link",
            "icons/cv.svg"
        ),
        link_button(
            "Certificados",
            "https://drive.google.com/drive/folders/1RXgJ7sCzKJI0Qj-_fZ-qcEJUowF63_2U?usp=drive_link",
            "icons/certificados.svg"
        ),
        link_button(
            "LinkedIn",
            "https://www.linkedin.com/in/luissierrac",
            "icons/linkedin.svg"
        ),
        width="100%"
    )