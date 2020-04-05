from deck import Deck
from hand import Hand
from datetime import datetime
import sys


def main():
    print('Welcome to POKER Console!')
    prompt_begin()

    point = read_record()
    print('Beginning point is: {}'.format(point))
    print()
    print('___________________________________GAME START___________________________________')
    print()

    while True:
        bet = prompt_bet(point)
        point += play(bet)

        print('Your current point is: {}'.format(point))
        if point <= 0:
            print('You have lost. End game!')
            save_record(point)
            sys.exit()
        print('________________________________________________________________________________')
        print()

        prompt_continue(point)


def prompt_begin():
    confirm = input('Begin? (y/n): ')
    while confirm != 'y' and confirm != 'n':
        confirm = input('please type y for \'yes\' & n for \'no\': ')

    if confirm == 'n':
        print('End game!')
        sys.exit()


def prompt_bet(point):
    while True:
        bet = input('Please enter bet? (integer): ')
        try:
            bet = int(bet)
            if bet > point:
                print('Don\'t lie, you don\'t have that much point!')
                raise Exception
            if bet > (point * 0.8):
                print('This is a bold move!!!. You might bankrupt this time')
            if bet < (point * 0.1):
                print('Don\'t be that cheap!. Try bigger number next time!')
            break
        except:
            continue
    return bet


def prompt_continue(point):
    confirm = input('Continue? (y/n): ')
    while confirm != 'y' and confirm != 'n':
        confirm = input('please type y for \'yes\' & n for \'no\': ')

    if confirm == 'n':
        print('End game!')
        save_record(point)
        sys.exit()
    print()


def play(bet):
    print()
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    for i in range(hand.hand_size):
        hand.place_card_in_hand(deck.deal(), i)
        deck.current_card_count += 1
    hand.show_hand()

    print()
    print('Please select your option: ')
    print('[1] Evaluate now')
    print('[2] Exchange card')
    print('Note: Maximum cards can be exchanged is 5. You only have one turn to do so')
    option = input('=> ')
    while option != '1' and option != '2':
        option = input('please type 1 for option [1] & 2 for option [2]: ')

    print()
    if option == '1':
        return show_result(hand, bet)

    if option == '2':
        positions = []
        while True:
            positions = prompt_exchange()
            print('Exchange card: ', positions)
            print('Confirm or reselect? ')
            print('[1] Confirmed')
            print('[2] Reselect')
            option = input('=> ')
            while option != '1' and option != '2':
                option = input('please type 1 for option [1] & 2 for option [2]: ')
            if option == '1':
                break
            if option == '2':
                continue

        print('Exchanging card at positions: ', positions)
        for i, position in enumerate(positions):
            hand.place_card_in_hand(deck.deal(), position - 1)
            deck.current_card_count += 1
        hand.show_hand()
        return show_result(hand, bet)


def prompt_exchange():
    positions = []
    print('Please enter card position to exchange (1-5): ')
    print('Enter 0 to stop')
    while True:
        position = input('=> ')
        try:
            position = int(position)
            if (len(positions) <= 0 and position == 0) or (position > 5 or position < 0):
                raise Exception
            if position in positions:
                print('you are already enter this position!')
                raise Exception
            if position == 0:
                break
            else:
                positions.append(position)
                if len(positions) == 5:
                    break
        except:
            print('Please enter a valid position')
            continue
    return positions


def show_result(hand, bet):
    print()
    print('Evaluating... ')
    print('___________________________________ Result:  ___________________________________')
    hand.evaluate()
    bet = hand.score * bet
    print('Rank: {}'.format(hand.rank))
    print('User {}: {} point(s)'.format('gain' if hand.score > 0 else 'loss', bet))
    return bet


def read_record():
    try:
        with open('data.txt', 'r') as file:
            last_line = file.readlines()
        return 1000 if not last_line else int(last_line[-1].split(',')[0].strip())
    except:
        return 1000


def save_record(point):
    now = datetime.now()
    with open('data.txt', 'a') as file:
        file.write('{},{} \n'.format(point, now.strftime("%d/%m/%Y %H:%M:%S")))


if __name__ == "__main__":
    main()

