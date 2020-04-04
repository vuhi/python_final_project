from enum import Enum


class Face(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4


class Card:

    def __init__(self, card_face=None, card_suit=None):
        self.face = card_face
        self.suit = card_suit

    def get_face(self):
        return self.face

    def get_suit(self):
        return self.suit
