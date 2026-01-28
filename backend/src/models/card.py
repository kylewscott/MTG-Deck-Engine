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

    @classmethod
    def from_scryfall(cls, card: dict, quantity: int) -> "Card":
        usd_price = card.get("prices").get("usd") 
        return cls(
            object = card.get("object"),
            name = card.get("name"),
            color_identity = card.get("color_identity", []),
            mana_cost = card.get("mana_cost"),
            type = card.get("type_line"),
            text = card.get("oracle_text"),
            image = card.get("image_uris").get("normal"),
            price = float(usd_price) if usd_price else None,
            quantity = quantity
        )
    
    def allow_any_number(text) -> bool:
        text.lower().replace("\n", " ")
        return multiple_allowed_text in text