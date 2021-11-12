import deckutils
from pathlib import Path
from deck import Deck
import random
from _getch import getch
import colorama
from colorama import Fore as ForeColor

colorama.init(autoreset=True)


def basic_study_type(deck: Deck) -> None:
    """Study a deck by typing the term that matches the definition
    
    deck: the deck that will be studied"""

    card: tuple[str, str] = deck.get_random_card()
    print(card[1])  # Print the defintion

    # Figure out possible answers
    answers: list[str] = deckutils.extract_answers(card[0])

    # Get the user to type the term
    attempt: str = input(ForeColor.CYAN + "Type the term: ").rstrip()

    # If the user typed the correct term
    if attempt in answers:
        print(ForeColor.GREEN + "Correct! Good job!\n")
        return

    print(ForeColor.RED + f"Incorrect. The correct answer is {card[0]}\n")
    return


def basic_study_match(deck: Deck) -> None:
    """Study a deck by matching the term to the definition

    This function just prompts the user once.
    For a study session using this method of study,
    this function should be called in while True loop.
    
    deck: the deck that will be studied"""

    # Define some consts
    AMOUNT_OF_CHOICES: int = 4

    assert AMOUNT_OF_CHOICES > 0

    card = deck.get_random_card()
    print(ForeColor.YELLOW + card[1])  # Print the defintion
    answer: str = card[0]  # Answer is term

    # Populate choices with some fake awnsers
    choices: list[str] = []
    c: str

    while len(choices) < AMOUNT_OF_CHOICES:
        c = deck.get_random_term()
        # If the "fake" choice is the same as real choice
        # Then don't add it as a fake choice
        if c == card[0]: continue
        choices.append(c)

    # Make one of the choices the correct anwser
    answer_location: int = random.randint(0, len(choices) - 1)
    choices[answer_location] = answer

    # Print out the choices
    for choice_location in range(len(choices)):
        print(f"{choice_location + 1}. {choices[choice_location]}")

    # Get the answer from the user
    print(ForeColor.CYAN + "Enter the number for the answer: ", end='')

    t = getch()
    print(ForeColor.MAGENTA + t.decode("utf-8"))
    # if q is typed, quit
    if t.decode("utf-8").lower() == 'q': exit(0)
    try:
        given_answer: int = int(t)
    except ValueError:
        t = t.decode("utf-8")
        print(ForeColor.RED + f"Incorrect! '{t}' is not a number!\n")
        return

    # Compare answers
    if (given_answer - 1) == answer_location:
        print(ForeColor.GREEN +
              f"Correct! {card[0]} means {card[1]}. Good job!\n")
        return

    print(ForeColor.RED + f"Incorrect. The correct answer is {answer}\n")
    return


def main():
    # Get the deck that should be used
    deck_dir = deckutils.get_decks_location()
    deck = deckutils.select_deck(deck_dir)
    print('\n')

    # Get the study type
    study_type: str
    print("""What type of studying do you want to do?
    1. Spelling
    2. Matching""")

    # Check
    while True:
        print(ForeColor.CYAN + "Enter the number that you want: ", end='')
        t = getch()
        print(ForeColor.MAGENTA + t.decode("utf-8"))
        try:
            d = int(t)
        except ValueError:
            print(ForeColor.RED + f"{t} is not an integer!")
            continue
        if d == 1:
            study_type = "typing"
            break
        elif d == 2:
            study_type = "matching"
            break
        print('\n' + ForeColor.RED + "Out of range. Try again.")
        continue

    print('\n')
    if study_type == "typing":
        try:
            while True:
                basic_study_type(deck)
        except KeyboardInterrupt:
            exit(0)
    if study_type == "matching":
        while True:
            basic_study_match(deck)


if __name__ == "__main__":
    main()