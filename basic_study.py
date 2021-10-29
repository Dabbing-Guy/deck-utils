import deckutils
from pathlib import Path
from deck import Deck 


def main():
    deck_dir = deckutils.get_decks_location()
    deck = deckutils.select_deck(deck_dir)

    
if __name__ == "__main__":
    main()