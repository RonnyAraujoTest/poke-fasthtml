"""
Pokedex FastHTML - Port de Next.js a FastHTML
Basado en el diseño original de Gilbert Matos
Repo original: https://github.com/treblig-punisher/pokedex-nextjs
"""
from fasthtml.common import *
from app.components.display import PokemonDisplay, PokedexFooter
from app.components.controls import SearchBar, DpadAndConfirmButtonsContainer
from app.components.buttons import SlimButtonsContainer
from app.hooks.use_fetch import get_pokemon_data
import requests

hdrs = (
    # Favicon
    Link(rel="icon", href="/app/static/pokeball.ico"),
    # Metadatos SEO y Social Media
    Meta(property="og:title", content="Pokedex by Gilbert Matos"),
    Meta(name="description", content="A web based pokedex that allows you to look up for pokemons."),
    Meta(name="twitter:site", content="@punisherx6"),
    Meta(name="twitter:title", content="Punisherx6 web developer"),
    Meta(name="twitter:description", content="Game/Web Dev and everything tech!"),
    # Estilos (reemplaza los .module.css con un archivo unificado)
    Link(rel="stylesheet", href="/app/static/css/globals.css"),
)

app, rt = fast_app(pico=False,hdrs=hdrs)

@rt("/")
def get():
    return (
        Title("Pokedex - FastHtml"), # Título de la pestaña
        # Contenedor del título (titleContainer)
        Div(
            Div("Pokedex", cls="pokedexTitle"),
            cls="titleContainer"
        ),
        # Contenedor principal (pokedexContainer)
        Div(
            # Aquí vive el BackgroundComponent que unifica la UI
            Div(
                PokemonDisplay(),
                DpadAndConfirmButtonsContainer(search_route="/search"),
                SlimButtonsContainer(),
                SearchBar(),
                cls="bgImage" # Este es el estilo de BackgroundComponent
            ),
            cls="pokedexContainer"
        ),
        PokedexFooter()
    )

@rt("/search")
async def post(pokemon_name: str):
    pokemon = get_pokemon_data(pokemon_name)

    return PokemonDisplay(
        name=pokemon["name"],
        picture=pokemon["picture"],
        types=pokemon["types"]
    )
    
    # Si falla, devolvemos el estado de "No Match"
    return PokemonDisplay(picture="/app/static/noMatch.png")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    serve(host="0.0.0.0", port=port)
