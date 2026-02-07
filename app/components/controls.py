from fasthtml.common import *

def SearchBar():
    return Div(
        Input(type="text", 
              name="pokemon_name",
              id="pokemon-input",
              placeholder="Search Pokemon",
              # Al presionar Enter, hace un POST a /search
              hx_post="/search", 
              hx_trigger="keyup[key=='Enter']",
              target_id="pokemon-render",
              hx_swap="outerHTML"),
        cls="greenScreen"
    )

def DpadButtons():
    return Div(
        Button("Confirmar", 
               hx_post="/search", 
               hx_include="#pokemon-input", 
               target_id="pokemon-render"),
        cls="dpad-container"
    )

def ConfirmRoundButton(button_clicked_route):
    return Button(
        cls="confirmButton",
        hx_post=button_clicked_route, # La ruta a la que llamará (ej: /search)
        hx_include="#pokemon-input",  # Incluye el valor del input de búsqueda
        target_id="pokemon-render",   # Dónde mostrar el resultado
        hx_swap="outerHTML"
    )

def DpadComponent():
    return Div(
        Img(src="/app/static/PokedexDpad.png", draggable="false"),
        cls="Dpad"
    )

def DpadAndConfirmButtonsContainer(search_route):
    return Div(
        ConfirmRoundButton(search_route),
        DpadComponent(),
        cls="DpadAndConfirmButtonsContainer"
    )