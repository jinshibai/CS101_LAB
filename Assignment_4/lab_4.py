
## CS 101 Lab
## Program # Slot Machine
## Name : Michael Bai
## Email : mbnmr@umkc.edu

import random
from os import sys

# this is a play again function which ask the user if wants to play again.
def play_again():
    user_input = input('Do you want to play again?==>')
    if user_input == 'Y' or user_input == 'YES' or user_input == 'y' or user_input == 'yes':
        return True
    elif user_input == 'N' or user_input == 'NO' or user_input == 'n' or user_input == 'no':
        print('Have a nice day.')
        sys.exit(0)
    else:
        print('You must enter Y/YES/N/NO to begin, please try again')
        play_again()


bank = 100
i = 0
max_v = bank

# ask the user to input correct chips to start with
while True:
    wager = int(input('How many chips do you want to play with?==>'))
    if wager < 1:
        print('Too low a value, you can only choose from 1 to 100 chips')

    elif wager > 100:
        print('Too high a value, you can only choose from 1 to 100 chips')
# set the value of random numbers, and ask user how much to bet
    while 0 < wager < 101:
        reel1 = random.randint(0, 10)
        reel2 = random.randint(0, 10)
        reel3 = random.randint(0, 10)
        num_list = (reel1, reel2, reel3)
        bet = int(input('How many chips do you want to start with?==>'))
        if bet < 1:
            print('The wager amount must be greater than zero,please enter again')
            continue
        elif bet > wager:
            print('The wager amount can not be greater than what you have', wager)
            continue
        else:
            # get the results and compare the results and calculate win or lost.
            False
            print('Round', i + 1, ':', num_list)
            count = 3 - len(set([reel1, reel2, reel3]))
            if count == 0:
                print("You matched 0 reels\n")
                print('You lost', bet)
                print('Current bank', wager - bet)
                wager = wager - bet
                i += 1
            if wager > max_v:
                max_v = wager
            elif count == 1:
                print("You matched 2 reels")
                print('You won', bet)
                print('Current bank', wager + bet * 2)
                wager = wager + bet * 2
                i += 1
            if wager > max_v:
                max_v = wager
            elif count == 2:
                print("You matched 3 reels")
                print('You won', bet * 9, 'chips')
                print('Current bank', wager + bet * 9)
                wager = wager + bet * 9
                i += 1
            if wager > max_v:
                max_v = wager
            # when user lost all the money, give user the result and ask user if want to play  again
            if wager == 0:
                print('You lost all', bet, 'chips in', i, 'rounds')
                print('The most chip you had was', max_v)
                play_again()