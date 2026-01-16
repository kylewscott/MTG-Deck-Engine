import requests
from src.parsers.input_parser import format_decklist

SCRYFALL_URL = "https://api.scryfall.com"

def get_card_by_name(name: str):
    url = f"{SCRYFALL_URL}/cards/named?exact={name.replace(' ', '%20')}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def main(): 
    deck_price = 0.0
    deck_list = format_decklist()
    
    for card in deck_list:
        card_data = get_card_by_name(card["name"])
        if(card_data["prices"]["usd"] != None):
            deck_price += float(card_data["prices"]["usd"])
        else:
            print(card_data["name"] + ": no price found :(")

    print(f"${round(deck_price, 2)}")

if __name__ == "__main__":
    main()