import exceptions


class Deck:
    def __init__(self, deck_data: str = ""):
        self._cards: dict[str, str] = {}

        # If there is deck data, import it
        if deck_data:
            self._import(deck_data)

    def _import(self, deck_data: str) -> None:
        """Changes deck data into cards and stores cards. 
        Make sure there is no ending or beginning newline!!
        WARNING: Replaces cards when used
        Please use add_cards method to add more cards"""

        card_pairs = deck_data.split('\n')
        cards: list[list[str]] = []
        for pair in card_pairs:
            cards.append(pair.split(','))

        cards = self._sanitize_card_dictlist(cards)
        self._cards = dict(cards)
        return

    def add_card(self, term: str, definition: str) -> None:
        """Adds a single card"""
        # Make sure that card does not already exist
        if term in self._cards:
            raise exceptions.CardAlreadyExists(term)
            return
        self.force_add_card(term, definition)

    def force_add_card(self, term: str, definition: str) -> None:
        """Adds a single card, ignoring if it already exists"""
        self._cards[term] = definition
        return

    def add_cards(self, cards: dict[str, str]):
        """Adds multiple cards to this deck

        Takes cards in a dictionary format of term: definition"""

        for term, definition in cards.keys():
            self.add_card(term, definition)

    def remove_card(self, term: str, allow_missing: bool = False) -> None:
        """Removes a card"""
        try:
            del self._cards[term]
            return
        except KeyError:
            if allow_missing:
                return

        raise exceptions.CardDoesNotExist(term)
        return

    def _sanitize_card_dictlist(self, cards: list[list[str]]) -> list[list[str]]:
        """Takes in a list of lists of card pairs and removes invalid card pairs

        This is importent so that when it is passed to dict(), dict does not raise error."""
        to_del: list[int] = [
        ]  # List of indexs of card pairs in cards to be del-ed
        # Loop for the indexes of the card pairs in cards
        for index in range(len(cards)):
            # Make sure that this card pair is correct len
            # If it is not, then add to to_del
            if not len(cards[index]) == 2:
                to_del.append(index)

        # Delete all indexes in to del
        # But first make sure to_del is not empty
        if len(to_del) == 0:
            return cards

        for _ in range(1, len(to_del) + 1):
            index = to_del[-1]
            del cards[index]
            del to_del[-1]

        return cards
