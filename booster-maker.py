#!/usr/bin/python
import random

green_index = int(raw_input('\n# of Green cards: '))
white_index = int(raw_input('# of White cards: ')) + green_index
blue_index = int(raw_input('# of Blue cards: ')) + white_index
black_index = int(raw_input('# of Black cards: ')) + blue_index
red_index = int(raw_input('# of Red cards: ')) + black_index
gold_index = int(raw_input('# of Gold/Hybrid cards: ')) + red_index
colorless_index = int(raw_input('# of colorless cards: ')) + gold_index
boost_size = int(raw_input('# of cards per booster pack: '))

booster_index = 0
booster_counter = 0
boost_again = True
boost_success = True
while boost_again:
    booster_counter += 1

    print ("\nGenerating booster pack #" + str(booster_counter) + "\n")
    boost_query = ' '
    for booster_index in range(0, boost_size):
        if colorless_index == 0:
            boost_success = False
            print("Insufficient cards to complete booster pack.\n")
            break
        card_selected = random.randint(1, colorless_index)

        if card_selected <= green_index:
            print(str(booster_index + 1) + ".) Green")
            green_index -= 1
            white_index -= 1
            blue_index -= 1
            black_index -= 1
            red_index -= 1
            gold_index -= 1
            colorless_index -= 1
        else:
            if (card_selected > green_index and card_selected <= white_index):
                print(str(booster_index + 1) + ".) White")
                white_index -= 1
                blue_index -= 1
                black_index -= 1
                red_index -= 1
                gold_index -= 1
                colorless_index -= 1
            else:
                if (card_selected > white_index and
                        card_selected <= blue_index):
                    print(str(booster_index + 1) + ".) Blue")
                    blue_index -= 1
                    black_index -= 1
                    red_index -= 1
                    gold_index -= 1
                    colorless_index -= 1
                else:
                    if (card_selected > blue_index and
                            card_selected <= black_index):
                        print(str(booster_index + 1) + ".) Black")
                        black_index -= 1
                        red_index -= 1
                        gold_index -= 1
                        colorless_index -= 1
                    else:
                        if (card_selected > black_index and
                                card_selected <= red_index):
                            print(str(booster_index + 1) + ".) Red")
                            red_index -= 1
                            gold_index -= 1
                            colorless_index -= 1
                        else:
                            if (card_selected > red_index and
                                    card_selected <= gold_index):
                                print(str(booster_index + 1) + ".) Gold")
                                gold_index -= 1
                                colorless_index -= 1
                            else:
                                if (card_selected > gold_index and
                                        card_selected <= colorless_index):
                                    print str(booster_index + 1) + \
                                          ".) Colorless"
                                    colorless_index -= 1
    if boost_success:
        print("\nBooster pack complete.\n")
    while boost_query.lower() != 'y' and boost_query.lower() != 'n':
        boost_query = raw_input('Create a new booster pack? (y/n)')

        if (boost_query.lower() == 'n'):
            boost_again = False
