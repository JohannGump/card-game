"""Define the Deck."""

from .card import RANKS, SUITS, Card
import random 


class Deck(list):
    """Deck of cards."""

    def __init__(self):
        """Has some cards."""
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.append(card)
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self)

    def draw_card(self):
        """Draw the top card."""
        try:
            return self.pop()
        except IndexError:
            return None


# deck = Deck()
# deck_draw = Deck.draw_card(deck)
# print(deck_draw)