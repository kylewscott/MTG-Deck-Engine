from dataclasses import dataclass

multiple_allowed_text = "a deck can have any number of cards named"

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
    
    
    def allow_any_number(self) -> bool:
        if not self.text:
            return False
        
        normalized_text = self.text.lower().replace("\n", " ")
        return multiple_allowed_text in normalized_text