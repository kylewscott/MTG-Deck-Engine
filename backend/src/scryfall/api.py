import requests
from src.parsers.input_parser import format_decklist
from src.models.card import Card
from src.models.deck import Deck

SCRYFALL_URL = "https://api.scryfall.com"

def get_card_by_name(name: str):
    url = f"{SCRYFALL_URL}/cards/named?exact={name.replace(' ', '%20')}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def main(): 
    deck_list = format_decklist()
    deck_data = []

    for card in deck_list:
        card_bulk_data = get_card_by_name(card["name"])
        card_data = Card.from_scryfall(card_bulk_data, card["quantity"])
        deck_data.append(card_data)

    deck = Deck(commander=deck_data[0], cards=deck_data)
    errors = deck.validate_deck()
    if(errors):
        print(errors)
    else:
        print('valid')

    print(f"\n\n\n\n")
    print(deck)

    return deck_data

if __name__ == "__main__":
    main()