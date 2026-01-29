import re

LINE_PATTERN = re.compile(
    r"^\s*(\d+)\s+([A-Za-z ',\-]+)"
)

#TODO Make the input more flexible with this parser
def format_decklist(decklist: list[str]):
    formatted_deck_list = []

    for line in decklist:
         match = LINE_PATTERN.match(line)
         if match:
              quantity = int(match.group(1))
              name = match.group(2).strip()
              formatted_deck_list.append({"name": name, "quantity": quantity})

    return formatted_deck_list