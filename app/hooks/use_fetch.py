import os
import requests
from dotenv import load_dotenv

load_dotenv()

POKEAPI_BASE_URL = os.getenv("POKEAPI_URL")

# Este es nuestro "Logic Hook"
def get_pokemon_data(name_or_id: str):
    if not name_or_id: return None
    
    try:
        url = f"{POKEAPI_BASE_URL}{name_or_id.lower().strip()}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Devolvemos un diccionario limpio (como tu objeto de estado en React)
            return {
                "name": data['name'],
                "picture": data['sprites']['front_default'],
                "types": " | ".join([t['type']['name'] for t in data['types']]),
                "success": True
            }
    except Exception as e:
        print(f"Error fetching pokemon: {e}")
        
    return {"picture": "/static/noMatch.png", "success": False}