from card import Card
from card import Face
from card import Suit
from enum import Enum
import numpy


class Rank(Enum):
    NoPair = 1
    LowPair = 2
    HighPair = 3
    TwoPair = 4
    ThreeOfAKind = 5
    Straight = 6
    Flush = 7
    FullHouse = 8
    FourOfAKind = 9
    StraightFlush = 10


class Hand:
    __hand_size = 5

    def __init__(self):
        self.cards_in_hand = numpy.empty(self.__hand_size, dtype=Card)
        self.rank = None
        self.score = 0

    def get_score(self):
        return self.score

    def get_rank(self):
        return self.rank

    def place_card_in_hand(self, card, position):
        self.cards_in_hand[position] = card

    def evaluate(self):
        # sort hand by face
        self.cards_in_hand = sorted(self.cards_in_hand, key=lambda x: x.face.value)


hand = Hand()
hand.place_card_in_hand(Card(Face.ACE, Suit.HEART), 0)
hand.place_card_in_hand(Card(Face.KING, Suit.CLUB), 1)
hand.place_card_in_hand(Card(Face.QUEEN, Suit.CLUB), 2)
hand.place_card_in_hand(Card(Face.EIGHT, Suit.CLUB), 3)
hand.place_card_in_hand(Card(Face.ACE, Suit.DIAMOND), 4)

# hand.evaluate()

for card in hand.cards_in_hand:
    print(card.face)
    print(card.suit)
    print('-------------')

hand.evaluate()
print('++++++++++++++++++++++++++')

for card in hand.cards_in_hand:
    print(card.face)
    print(card.suit)
    print('-------------')


