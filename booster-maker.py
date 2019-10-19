#!/usr/bin/python3

import random
from itertools import chain, repeat


def prompt_user(**cards):
    for color in cards:
        prompt_string = '# of {} cards: '.format(color.capitalize())

        prompts = chain([prompt_string], repeat("Not a valid number. Try again: "))
        replies = map(input, prompts)
        valid_response = next(filter(str.isdigit, replies))

        cards[color] = int(valid_response)

    return cards


def generate_booster_pack(user_cards, **boost):
    while boost['again']:
        boost['counter'] += 1

        print ("\nGenerating booster pack #" + str(boost['counter']) + "\n")
        boost_query = ' '
        for boost['index'] in range(0, boost['size']):
            card_total = sum(user_cards.values())
            if card_total == 0 :
                boost['success']= False
                print("Insufficient cards to complete booster pack.\n")
                break

            card_selected = random.choice([color for color in user_cards if user_cards[color] > 0])
            user_cards[card_selected] -= 1

            print( str(boost['index'] + 1) + ". ) " + card_selected.capitalize())

        if boost['success']:
            print("\nBooster pack complete.\n")

        while (boost_query.lower() != 'y' and boost_query.lower() != 'n'):

            if card_total == 0:
                print('Not enough remaining cards to complete a booster pack')
                print('\nExiting program.')
                boost_query = 'n'
            else:
                boost_query = input('Create a new booster pack? (y/n)')

            if boost_query.lower() == 'n':
                boost['again'] = False


def main():
    cards = {
        'green': 0,
        'white': 0,
        'blue': 0,
        'red': 0,
        'gold': 0,
        'colorless': 0
    }
    user_cards = prompt_user(**cards)

    booster_index = 0
    booster_counter = 0
    boost_again = True
    boost_success = True

    boost = {
        'index': 0,
        'counter': 0,
        'again': True,
        'success': True
    }
    boost['size'] = int(input('# of cards per booster pack: '))

    generate_booster_pack(user_cards, **boost)


if __name__ == '__main__':
    main()
