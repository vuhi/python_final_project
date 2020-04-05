from card import Face
import matplotlib.pyplot as plt
from matplotlib.image import imread


class Hand:

    def __init__(self):
        print('Init hand ...')
        self.hand_size = 5
        self.cards_in_hand = [None] * self.hand_size
        self.rank = None
        self.score = 0

    def get_score(self):
        return self.score

    def get_rank(self):
        return self.rank

    def place_card_in_hand(self, card, position):
        self.cards_in_hand[position] = card

    def show_hand(self):
        print('Showing hand...')
        fig = plt.figure(figsize=(50, 30))
        for i, card in enumerate(self.cards_in_hand):
            fig.add_subplot(1, 7, i + 2,)
            face = card.face.name
            suit = card.suit.name
            path = './images/{}{}s.png'.format(face, suit)
            plt.imshow(imread(path))
            plt.axis('off')
        plt.show()

    def evaluate(self):
        # sort hand by face
        sorted_cards = sorted(self.cards_in_hand, key=lambda x: x.face.value)

        # More reference: https://en.wikipedia.org/wiki/List_of_poker_hands
        flush_count_occurrence = 1 # number of flush occurred in hand
        straight_count_occurrence = 1 # number of straight occurred in hand
        face_occurrence_dict = dict() # record face occurrence for pair, three of kind, full house & four of kind

        # Check for flush, straight, or both
        for i, card in enumerate(sorted_cards):
            # ignore first card
            if i == 0:
                face_occurrence_dict[card.get_face().name] = 1
                continue
            # count number of card have same suit
            if card.get_suit() == sorted_cards[i - 1].get_suit():
                flush_count_occurrence += 1

            # count number of straight
            if card.get_face().value == (sorted_cards[i - 1].get_face().value + 1):
                straight_count_occurrence += 1

            # special case for baby straight: [ 2, 3, 4, 5, ACE ]
            if (i == len(sorted_cards) - 1) and (card.get_face() == Face.ACE) and (sorted_cards[0].get_face() == Face.TWO):
                straight_count_occurrence += 1

            # update card face occurrence
            if card.get_face().name not in face_occurrence_dict.keys():
                face_occurrence_dict[card.get_face().name] = 1
            else:
                face_occurrence_dict[card.get_face().name] += 1

        pair_count = 0
        three_of_kind = 0
        four_of_kind = 0

        for (face, v) in face_occurrence_dict.items():
            if v == 2:
                pair_count += 1
            if v == 3:
                three_of_kind += 1
            if v == 4:
                four_of_kind += 1

        # Begin evaluation:
        if flush_count_occurrence == 5 and straight_count_occurrence == 5:
            self.rank = 'Straight Flush'
            self.score = 15
            return

        if flush_count_occurrence == 5:
            self.rank = 'Flush'
            self.score = 8
            return

        if straight_count_occurrence == 5:
            self.rank = 'Straight'
            self.score = 6
            return

        if four_of_kind == 1:
            self.rank = 'Four of a kind'
            self.score = 12
            return

        if three_of_kind == 1 and pair_count == 1:
            self.rank = 'Full house'
            self.score = 10
            return

        if three_of_kind == 1:
            self.rank = 'Three of kind'
            self.score = 4
            return

        if pair_count > 0:
            self.rank = '{} pair(s)'.format(pair_count)
            self.score = 2
            return

        self.rank = 'None'
        self.score = -1
        return
