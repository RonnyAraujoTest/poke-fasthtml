from fasthtml.common import *

def PokemonDisplay(name="", picture="", types=""):
    # Lógica de formateo (el upperCasedWord de tu React)
    display_name = name.capitalize() if name else ""
    display_types = types.title() if types else ""
    
    return Div(
        Img(src=picture, draggable="false"),
        Div(display_types, cls="pokemonType"),
        Div(display_name, cls="pokemonName"),
        cls="pokemonDisplayContainer",
        id="pokemon-render"
    )

def PokedexFooter():
    return Footer(
        Div(
            Div(
                Span("Diseño original por "),
                A("@Gilbert Matos", 
                  href="hhttps://github.com/treblig-punisher", 
                  target="_blank",
                  cls="footerLink"),
                cls="footerSection"
            ),
            # Link a TU código fuente
            Div(
                Span("Código fuente en "),
                A("GitHub", 
                  href="https://github.com/RonnyAraujoTest/poke-fasthtml", 
                  target="_blank",
                  cls="githubLink"),
                cls="footerSection"
            ),
            cls="footerContainer"
        ),
        cls="mainFooter"
    )