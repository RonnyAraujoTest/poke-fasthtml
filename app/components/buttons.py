from fasthtml.common import *

def SlimButtonComponent(button_cls):
    return Div(cls=button_cls)

def SlimButtonsContainer():
    return Div(
        # Creamos dos botones usando el componente base
        SlimButtonComponent("buttonComponent"),
        SlimButtonComponent("buttonComponent"),
        cls="buttonsContainer"
    )