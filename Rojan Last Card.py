#Imports
from random import*
from random import shuffle

"""Basic Functions"""
def gap():
    print("")
def player_print():
    print("Your turn: ")
def bot_move(which_bot_text):
    print("Bot {}'s Turn:".format(which_bot_text))

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
"separating cards into their ranks and suits"

for e in range(4):
    for i in range(13):
        card = ('{} of {}'.format(ranks[i], suits[e]))
        suit_list[e-1].append(card)
        rank_list[i-1].append(card)
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

    if player_list_len == 5:
        x = 1
        break

    player_randint = randint(0, player_len-1)

    player_card = deck[player_randint]

    if player_card not in player_list:
        player_list.append(player_card)

        deck.remove(player_card)

"********************************************************************"

bots_list = [bot_one_list, bot_two_list]

def pick_up(which_bot):
    current_bot_list = bots_list[which_bot]
    current_bot_list.append(deck[0])
    deck.remove(deck[0])

def bot_turn(which_bot, last_card_played):
    global playing_card
    global which_bot_string

    x = 1

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

        if checking_card_rank == current_rank or checking_card_suit == current_suit:

            bot_move(which_bot_text)
            playing_card = checking_card
            print("{}{}".format(arrow, playing_card))

            current_bot_list.remove(playing_card)
            break

        if i == bot_list_len-1:

            bot_move(which_bot_text)
            print("{}{}".format(arrow, "Picks Up"))
            pick_up(which_bot)
            break

#********************************************************************#

"""player's turn as a function"""
def print_player_list():
    print("Your Cards: ")
    print(player_list)

def player_turn(card):

    global current_card

    print_player_list()
    gap()

    print("What card do you want to play?")
    print("(If you want to pick up, enter '0')")

    y = 1
    while y == 1:
        try:
            player_turn_index = int(input(''))
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

                    if starter_suit != player_suit and starter_value != player_value:
                        print("Card cannot be played")

                    if starter_suit == player_suit or starter_value == player_value:

                        current_card = player_turn_card

                        player_print()
                        print("{}{}".format(arrow, current_card))

                        break


        except ValueError:
            gap()
            print("Please type in a valid number")


print("This is Last Card")

starting_card = deck[0]
print("Starting card")
print(arrow, starting_card)
gap()

player_turn(starting_card)






