import requests

SCRYFALL_URL = "https://api.scryfall.com"

def get_card_by_name(name: str):
    url = f"{SCRYFALL_URL}/cards/named?exact={name.replace(' ', '%20')}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()
        