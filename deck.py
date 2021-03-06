from card import Card
from card import Face
from card import Suit
import random


class Deck:

    __deck_size = 52

    def __init__(self):
        print('Init desk ...')
        self.deck = [None]*self.__deck_size
        self.current_card_count = 0
        count = 0
        for suit in Suit:
            for face in Face:
                self.deck[count] = Card(face, suit)
                count += 1

    def shuffle(self):
        random.shuffle(self.deck)
        self.current_card_count = 0

    def deal(self):
        return self.deck[self.current_card_count] if self.current_card_count < len(self.deck) else None
