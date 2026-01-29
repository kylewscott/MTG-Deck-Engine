from dataclasses import dataclass
from typing import List
from src.models.card import Card

@dataclass()
class Deck:
    commander: Card
    cards: List[Card]