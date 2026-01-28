from dataclasses import dataclass
from typing import List
from src.models.card import Card

MAX_CARDS = 99
MIN_CARDS = 99 

lands = ["island", "swamp", "plains", "forest", "mountain"]

@dataclass()
class Deck:
    commander: Card
    cards: List[Card]
    
    def validate_deck(self):
        errors = []

        card_count = 0
        for card in self.cards:
            card_count += card.quantity

        if(self.commander is None):
            errors.append(f"Deck must have a commander\n")

        if(card_count > MAX_CARDS or card_count < MIN_CARDS):
            errors.append(f"Deck must contain exactly 99 cards, found {card_count}\n")

        found_names = set()
        for card in self.cards:
            if(card.name in found_names or card.quantity > 1):
                if((card.text and not Card.allow_any_number(card.text)) and card.name.lower() not in lands):
                    errors.append(f"Multiple copies of the same card found: {card.name}\n")
            else:
                found_names.add(card.name)

        return errors
    
    ##Need to map everything out on paper for archtiecture moving forward!

    #Goal is to get everything setup (input, validations, hit api, setup parsers, layout groundwork) so that 
    #I can rope in andy for his MTG expertise when trying to tokenize and create keyword mappings
    #Want to clean up everything, make sure util functions are in util folder and everything is neat.

        