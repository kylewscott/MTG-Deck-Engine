from src.parsers.decklist_parser import format_decklist
from src.services.scryfall_service import get_card_by_name
from src.services.card_factory import create_card
from src.validations.commander_rules import validate_deck
from src.models.card import Card
from src.models.deck import Deck
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEST_DECK_PATH = BASE_DIR / "test_data" / "test_deck.txt"

def run():
    #TODO Take real input
    with open(TEST_DECK_PATH, 'r') as file:
         raw_decklist = file.read().splitlines()

    decklist = format_decklist(raw_decklist)
    cards = []

    for card in decklist:
        card_json = get_card_by_name(card["name"])
        card = create_card(card_json, card["quantity"])
        cards.append(card)

    #TODO: Setup real commander input
    deck = Deck(commander=cards[0], cards=cards)
    errors = validate_deck(deck)

    if(errors):
        print(errors)
    else:
        print('valid')

    print(deck)

if __name__ == "__main__":
    run()
