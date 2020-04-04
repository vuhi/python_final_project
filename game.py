from card import Card
from deck import Deck
from hand import Hand
from user import User

deck = Deck()
deck.shuffle()

hand = Hand()

for i in range(5):
    card = deck.deal()
    hand.place_card_in_hand(card, i)

hand.evaluate()
print(hand.cards_in_hand)
