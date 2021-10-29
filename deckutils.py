"""This file contains functions for working with flashcard decks and flashcard files"""
from deck import Deck
import exceptions
from pathlib import Path
import os
from typing import Literal, Union


def deck_from_file(path: Path) -> Deck:
    """This fuction makes a deck from data in file at path"""
    with path.open('r') as file:
        return Deck(file.read())
    

def get_deck_files(deck_dir: Path) -> list[Path]:
    """Returns a list with paths to all .deck files in a dir"""
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


def find_dropbox() -> Union[Path, Literal[False]]:
    """Try to find dropbox.
    If it exists: return the Path for it
    If it does not exist: return None"""

    try: # Check for dropbox env var
        return Path(os.environ["DROPBOX"])
    except KeyError: pass # If DROPBOX not set 

    # Look in defualt Dropbox location
    if (Path.home() / "Dropbox").exists():
        return Path.home() / "Dropbox" 

    return False


def get_decks_location(force_prompt: bool = False, check_path: bool = True) -> Path:
    """Returns the dir that the decks are in
    
    force_prompt: Do not check, just ask user to type path
    check_path: Make sure path exists and is folder
    
    Note: path is automaticlly check if dir is found automaticlly"""

    # Just ask if force prompt
    if force_prompt:
        return ask_for_decks_location(to_check_path=check_path)
    
    # Look for dropbox
    dropbox: Union[Path, Literal[False]] = find_dropbox()
    # If no dropbox, give up. dropbox being False breaks below code
    if not dropbox: return ask_for_decks_location(to_check_path=check_path)

    # Look for names of deck folders
    item: Path
    for item in dropbox.iterdir():
        if item.stem.lower() == "decks": 
            # Make sure it is acually a folder first
            if item.is_dir(): return item

        if item.stem.lower() == "flashcards":
            # Make sure it is acually a folder first
            if item.is_dir(): return item

    # If this runs, we could not find it in dropbox:
    return ask_for_decks_location(to_check_path=check_path)


def ask_for_decks_location(to_check_path: bool = True) -> Path:
    """Just ask user for decks location"""
    while True:
        path = Path(input("Enter path to folder with deck files: "))
        if to_check_path: 
            if check_path(path): return path
            continue
        return path


def check_path(path: Path) -> bool:
    """Makes sure that the given path points is a folder that exists.

    if passes tests: return True
    if not passes tests: return False"""
    
    # Make sure it is a valid path
    try:
        if not path.exists(): return False
    except OSError:
        # This means that an invalid path was passed
        return False
    
    # Make sure it is a folder
    if not path.is_dir: return False
    
    # Passed all tests
    return True