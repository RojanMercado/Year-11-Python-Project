#Imports
from random import*
from random import shuffle
import sys
import time

"""Basic Functions"""
def gap():
    print("")
def player_print():
    print("Your turn: ")
def bot_move(which_bot_text):
    print("Bot {}'s Turn:".format(which_bot_text))
def one():
    time.sleep(1)
def two():
    time.sleep(2)
def sleep(how_many_seconds_you_want_to_wait):
    time.sleep(how_many_seconds_you_want_to_wait)

arrow = "> "

"""Creating a complete standard deck of cards"""
ranks = ["Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
deck = []

"***********************************************************"

aces = []
twos = []
threes = []
fours = []
fives = []
sixes = []
sevens = []
eights = []
nines = []
tens = []
jacks = []
queens = []
kings = []

"***********************************************************"

clubs = []
diamonds = []
hearts = []
spades = []

"********************************************************************"

suit_list = [clubs, diamonds, hearts, spades]
suit_list2 = ["clubs", "diamonds", "hearts", "spades"]

rank_list = [aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings]
rank_list2 = ["aces", "twos", "threes", "fours", "fives", "sixes", "sevens", "eights", "nines", "tens", "jacks", "queens", "kings"]

"********************************************************************"

power_card_list = []

"********************************************************************"

"separating cards into their ranks and suits"

for e in range(4):
    for i in range(13):
        card = ('{} of {}'.format(ranks[i], suits[e]))
        suit_list[e].append(card)
        rank_list[i].append(card)
        if i == 2 or i == 5 or i == 1:
            power_card_list.append(card)
        if card not in deck:
            deck.append(card)

"********************************************************************"

"Functions to check the rank and suit of any card"

def suit_checker(card_you_want_to_check):
    global returned_suit

    for i in range(4):
        if card_you_want_to_check in suit_list[i-1]:
            suit_check = i
            break
    returned_suit = suit_list2[suit_check]

def rank_checker(f):
    global returned_rank

    for i in range(13):
        if f in rank_list[i-1]:
            rank_check = i
            break
    returned_rank = rank_list2[rank_check]

"********************************************************************"

"""adding to the randomizing"""
def shuffle_deck():
    for p in range(100):
        shuffle(deck)

"********************************************************************"

"""counting how many times a five has been played"""
def power_five_counter():
    global power_five_count

    int(power_five_count)

    if current_card in fives:
        power_five_count += 1

"********************************************************************"

"""Bot one"""
bot_one_list = []
x = 1

shuffle_deck()

while x == 1:
    bot_one_len = len(deck)

    bot_one_list_len = len(bot_one_list)

    if bot_one_list_len == 5:
        x = 1
        break

    bot_one_randint = randint(0, bot_one_len-1)

    bot_one_card = deck[bot_one_randint]

    if bot_one_card not in bot_one_list:
        bot_one_list.append(bot_one_card)

        deck.remove(bot_one_card)


#********************************************************************#

"""adding to the randomizing"""
shuffle_deck()

"""Bot two"""
bot_two_list = []
x = 1
while x == 1:
    bot_two_len = len(deck)

    bot_two_list_len = len(bot_two_list)

    if bot_two_list_len == 5:
        x = 1
        break

    bot_two_randint = randint(0, bot_two_len-1)

    bot_two_card = deck[bot_two_randint]

    if bot_two_card not in bot_two_list:
        bot_two_list.append(bot_two_card)

        deck.remove(bot_two_card)


#********************************************************************#


"""adding to the randomizing"""
shuffle_deck()

"""Player list"""
player_list = []
x = 1
while x == 1:
    player_len = len(deck)

    player_list_len = len(player_list)

    """loop will break when the player list has 5 cards/objects"""
    if player_list_len == 5:
        x = 1
        break

    player_randint = randint(0, player_len-1)

    players_card = deck[player_randint]

    if players_card not in player_list:
        player_list.append(players_card)

        deck.remove(players_card)

"********************************************************************"
#special function which checks if the card is in a power_card list

def power_card_checker(card_you_want_be_checked):
    global power_five
    global power_two
    global power_ace

    """returning the rank of the card"""
    for i in range(13):
        if card_you_want_be_checked in rank_list[i]:
            card_ranker = rank_list2[i]
            break

    if card_ranker == rank_list2[5]:
        power_five = 1
        power_two = 0
        power_ace = 0

    elif card_ranker == rank_list2[2]:
        power_five = 0
        power_two = 1
        power_ace = 0

    elif card_ranker == rank_list2[1]:
        power_five = 0
        power_two = 0
        power_ace = 1

    else:
        power_five = 0
        power_two = 0
        power_ace = 0
"********************************************************************"
current_card = ''

bots_list = [bot_one_list, bot_two_list]

"""function which automates bots and the player picking up"""
def pick_up(which_bot, number):
    current_bot_list = bots_list[which_bot]

    for i in range(number):
        current_bot_list.append(deck[0])
        deck.remove(deck[0])


def pick_up_player(number):

    for i in range(number):
        player_list.append(deck[0])
        deck.remove(deck[0])

"""function which almost completely automates the bots turn"""
def bot_turn(which_bot, last_card_played):
    global playing_card
    global which_bot_string
    global current_card

    """implementing power cards"""
    global power_card

    x = 1

    gap()
    two()

    #making which_bot into a string
    def which_bot_string(which_bot):
        global which_bot_text

        which_bot_list = ["One", "Two"]
        which_bot_text = which_bot_list[which_bot-1]

    which_bot_string(which_bot)

    """returning the rank and suit of the last card played"""
    suit_checker(last_card_played)
    current_suit = returned_suit

    rank_checker(last_card_played)
    current_rank = returned_rank

    """checking which bot_list is the right one to check"""
    current_bot_list = bots_list[which_bot-1]

    bot_list_len = len(current_bot_list)

    """checking if the rank and suit of the card being checked matches with that of the last card played"""
    for i in range(bot_list_len):

        checking_card = current_bot_list[i-1]

        suit_checker(checking_card)
        checking_card_suit = returned_suit

        rank_checker(checking_card)
        checking_card_rank = returned_rank

        """checking if the card is valid card to be played from the current card"""
        if checking_card_rank == current_rank or checking_card_suit == current_suit:

            bot_move(which_bot_text)
            playing_card = checking_card
            print("{}{}".format(arrow, playing_card))
            gap()

            current_card = playing_card
            power_card_checker(current_card)

            current_bot_list.remove(playing_card)

            """if a bot uses all their cards, they win"""

            if len(current_bot_list) == 1:
                print("'Bot {}".format(which_bot_text))
                print(arrow, "LAST CARD!")

            if len(current_bot_list) == 0:
                print("Bot {} Wins".format(which_bot_text))
                sys.exit()

            break

        if i == bot_list_len-1:

            bot_move(which_bot_text)
            print("{}{}".format(arrow, "Picks Up"))
            pick_up(which_bot, 1)
            gap()

            break

#********************************************************************#

"""player's turn as a function"""
def print_player_list():
    print("Your Cards: ")
    print(player_list)

def player_turn(card):

    global power_five_compilation
    global current_card
    one()
    print("********************************************************************")
    gap()
    player_list_len = len(player_list)
    print_player_list()
    gap()
    print("Current Card")
    print(arrow, current_card)
    gap()
    two()

    """implementing power cards"""
    global power_card

    print("Type in the number of the card you want to play in your list")
    print("(If you want to pick up, enter '0')")


    power_card_checker(current_card)

    y = 1
    while y == 1:

        try:
            player_turn_index = int(input(''))

            player_card = player_list[player_turn_index]

            if player_turn_index == 0:
                player_list.append(deck[0])
                deck.remove(deck[0])

                print_player_list()
                break

            if player_turn_index != 0:
                if player_turn_index < 0 or player_turn_index > len(player_list):
                    print("Card cannot be played as you do not have {} cards".format(player_turn_index))
                    print("Please try again")
                    gap()

                if player_turn_index > 0 and player_turn_index < len(player_list)+1:
                    player_turn_card = player_list[player_turn_index-1]



                    """checking starter card rank and suit"""
                    suit_checker(card)
                    starter_suit = returned_suit

                    rank_checker(card)
                    starter_value = returned_rank

                    """checking player card rank and suit"""
                    suit_checker(player_turn_card)
                    player_suit = returned_suit

                    rank_checker(player_turn_card)
                    player_value = returned_rank

#********************************************************************#

                    #implementing power five for the situation
                    if power_five == 1:

                        rank_checker(player_card)
                        five_checker = returned_rank

                        rank_checker(current_card)
                        current_card_rank = returned_rank

                        if five_checker != rank_checker:
                            print("The current card is a {}".format(current_card))
                            print("If you do not have a Five, then you must pick up {} cards from the deck".format(power_five_compilation))
                    
#********************************************************************#

                    #if the last card played was not a power card, then the main bulk of code continues through here
                    if power_five == 0 and power_ace == 0: and power_two == 0:

                        if starter_suit != player_suit and starter_value != player_value:
                            print("Card cannot be played")

                        if starter_suit == player_suit or starter_value == player_value:

                            current_card = player_turn_card

                            player_print()
                            print("{}{}".format(arrow, current_card))
                            player_list.remove(current_card)

                            if player_list_len == 1:
                                print("You")
                                print(arrow, "LAST CARD")
                            if player_list_len == 0:
                                print("You won")
                                sys.exit()

                            break

        """catching a value error"""
        except ValueError:
            gap()
            print("Please type in a valid number")


print("Last Card")
one()
gap()

"""ensuring that the starting card is not a power card"""
for i in range(len(deck)):
    starting_card = deck[i]
    if starting_card not in power_card_list:
        break

print("Starting card")
print(arrow, starting_card)

current_card = starting_card
gap()
two()

player_turn(starting_card)

"""setting the power_five compilation (where you can stack multiple fives) to zero"""
power_five_compilation = 0

while True:
    for i in range(2):
        bot_turn(i-1, current_card)
    print("{}".format(len(deck)))
    player_turn(current_card)






