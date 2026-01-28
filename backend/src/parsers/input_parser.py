import re

test_data = ""
with open(r'D:\Projects\MTG-Deck-Engine\backend\src\test_data\test_deck.txt', 'r') as file:
        test_data = file.read().splitlines()

LINE_PATTERN = re.compile(
    r"^\s*(\d+)\s+([A-Za-z ',\-]+)"
)

def format_decklist():
    formatted_deck_list = []

    for line in test_data:
         match = LINE_PATTERN.match(line)
         if match:
              quantity = int(match.group(1))
              name = match.group(2).strip()
              formatted_deck_list.append({"name": name, "quantity": quantity})

    return formatted_deck_list


def main():
    deck_list = format_decklist();
    print(deck_list)

if __name__ == "__main__":
    main()