from typing import Literal, Union
import deckutils
from deck import Deck 
from pathlib import Path
import os


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


def main():
    deck_dir = get_decks_location()
    deck_path = deckutils.select_deck(deck_dir)


if __name__ == "__main__":
    main()