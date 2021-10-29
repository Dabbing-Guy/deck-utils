"""This file contains functions for working with flashcard decks and flashcard files"""
from deck import Deck
import exceptions
from pathlib import Path


def deck_from_file(path: Path) -> Deck:
    """This fuction makes a deck from data in file at path"""
    with path.open('r') as file:
        return Deck(file.read())
    

def get_deck_files(deck_dir: Path) -> list[Path]:
    decks: list[Path] = [] # Contains paths of decks
    for file in deck_dir.iterdir():
        if file.name.endswith("deck"):
            decks.append(file)
        
    return decks


def select_deck(deck_dir: Path) -> Deck:
    """Prompts the user to select a deck from the deck dir
    Returns the deck the user selected."""

    decks: list[Path] # Contains paths of decks

    # Make sure path is actully a dir
    if deck_dir.is_file():
        raise ValueError(deck_dir)
    
    # Get .deck files from deck_dir and add them to decks
    decks = get_deck_files(deck_dir)

    # Print before listing options
    print("Please select a deck: \n")
    # Now print out all of the decks and a coraponding number
    deck: Path
    for deck_index in range(len(decks)):
        deck = decks[deck_index]
        print(f"{deck_index + 1}. {deck.stem}")

    # Contains index of choice, -1 is no choice made yet
    choice: int = -1 

    # Uncheck choice, not checked
    pchoice: int 
    schoice: str

    # Loop until valid choice is made
    while choice == -1:
        schoice = input("Select a deck: ")

        # Convert to int
        try:
            pchoice = int(schoice)
        except ValueError:
            print("Must type number. Try again")
            continue

        # Make sure not out of range
        if not 1 < pchoice < len(decks):
            print("Out of range. Try again")
            continue

        # Exit loop by setting choice
        choice = pchoice
    
    # Decks is just a list of paths of decks
    # Choice is the index of the chosen deck + 1
    return deck_from_file(decks[choice - 1])
