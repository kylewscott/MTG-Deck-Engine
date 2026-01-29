from src.models.deck import Deck
from src.models.card import Card

MAX_CARDS = 99
MIN_CARDS = 99 
lands = ["island", "swamp", "plains", "forest", "mountain"]

def validate_deck(deck: Deck):
    errors = []

    card_count = 0
    for card in deck.cards:
        card_count += card.quantity

    if(deck.commander is None):
        errors.append(f"Deck must have a commander\n")

    if(card_count > MAX_CARDS or card_count < MIN_CARDS):
        errors.append(f"Deck must contain exactly 99 cards, found {card_count}\n")

    found_names = set()
    for card in deck.cards:
        if(card.name in found_names or card.quantity > 1):
            if((card.text and not card.allow_any_number()) and card.name.lower() not in lands):
                errors.append(f"Multiple copies of the same card found: {card.name}\n")
        else:
            found_names.add(card.name)

    return errors