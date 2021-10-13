class CardAlreadyExists(Exception):
    """For when a card already exists."""
    def __init__(self, term: str) -> None:
        self.message = f'The card with the term "{term}" already exists in this deck'
        super.__init__(self.message)

class CardDoesNotExist(Exception):
    """For if a card does not exist"""
    def __init__(self, term: str) -> None:
        self.message = f'The card with the term "{term}" does not exist in this deck'
