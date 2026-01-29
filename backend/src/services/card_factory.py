from src.models.card import Card

def create_card(card_input: dict, quantity: int):
    usd_price = card_input.get("prices").get("usd") 
    return Card(
        object = card_input.get("object"),
        name = card_input.get("name"),
        color_identity = card_input.get("color_identity", []),
        mana_cost = card_input.get("mana_cost"),
        type = card_input.get("type_line"),
        text = card_input.get("oracle_text"),
        image = card_input.get("image_uris").get("normal"),
        price = float(usd_price) if usd_price else None,
        quantity = quantity
    )
