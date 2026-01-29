from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    object: str
    name: str
    color_identity: str
    mana_cost: str
    type: str
    text: str
    image: str
    price: float
    quantity: int
    

    