import deckutils
from pathlib import Path
from deck import Deck
import random


def basic_study_type(deck: Deck) -> None:
    """Study a deck by typing the term that matches the definition
    
    deck: the deck that will be studied"""

    card: tuple[str, str] = deck.get_random_card()
    print(card[1])  # Print the defintion

    # Get the user to type the term
    attempt: str = input("\nType the term: ")

    # If the user typed the correct term
    if attempt == card[0]:
        print("Correct! Good job!\n")
        return
    
    print(f"Incorrect. The correct answer is {card[0]}\n")
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
    print(card[1])  # Print the defintion
    print('\n')
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
    t = input("Enter the number for the answer: ")
    try:
        given_answer: int = int(t)
    except ValueError:
        print(f"Incorrect! {t} is not a number!")
        return

    # Compare answers
    if (given_answer - 1) == answer_location:
        print("Correct! Good job!\n")
        return

    print(f"Incorrect. The correct answer is {answer}\n")
    return


def main():
    # Get the deck that should be used
    print
    deck_dir = deckutils.get_decks_location()
    deck = deckutils.select_deck(deck_dir)
    print('\n')

    try:
        while True:
            basic_study_type(deck)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()