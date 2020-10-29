"""Imports"""
from random import*
from random import shuffle
import sys
import time

"""Basic Functions"""


def gap():
    print("")


def player_print():
    print("Your turn: ")


def bot_move(bot_string):
    print("Bot {}'s Turn:".format(bot_string))


def sleep(how_many_seconds_you_want_to_wait):
    time.sleep(how_many_seconds_you_want_to_wait)


def processing(string):
    sys.stdout.write(string)

    def ellipsis():
        time.sleep(0.55)
        sys.stdout.write(".")

    for i in range(4):
        ellipsis()


"*********************************************************************************************************************************************************************************"

arrow = "> "

"""Creating a complete standard deck of cards"""
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
deck = []

"*********************************************************************************************************************************************************************************"

# Admin Password: (if you don't want to be confused by this, read on)
admin_answer = randint(5,12)

admin_checker2_decider = randint(1,3)
admin_checker2_list = [2,3,4]
admin_checker2 = admin_checker2_list[admin_checker2_decider-1]

admin_checker1 = admin_answer*admin_checker2
print("{},{}".format(admin_checker1, admin_checker2))
gap()
print("**************************")
print("LET'S PLAY LAST CARD!")
print("**************************")
gap()
admin_loop = 1
while admin_loop == 1:
    try:
        global test
        global auto_tester
        global five_tester

        print("Press ENTER to play")
        admin_password = int(input(arrow))
        if admin_password == admin_answer:
            print("'test' value (integer)")
            test = int(input(arrow))
            print("'five_tester' value? (yes or no)")
            five_tester = input(arrow)
            print("'auto_tester' tester value? (yes or no)")
            auto_tester = input(arrow)
            print("'time1 value' (integer)")
            time1 = float(input(arrow))
            print("'time2 value' (integer)")
            time2 = float(input(arrow))
        if admin_password != admin_answer:
            test = 0
            auto_tester = "no"
            five_tester = "no"
            time1 = 1
            time2 = 2
        break

    except ValueError:
        test = 0
        auto_tester = "no"
        five_tester = "no"
        time1 = 1
        time2 = 2
        break


"*********************************************************************************************************************************************************************************"


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
        if i == 4 or i == 0:
            power_card_list.append(card)
        if card not in deck:
            deck.append(card)

# tester variable (test = 1 for testing)
if test == 1:
    gap()
    print("ENTIRE DECK")
    print("{}".format(deck))
    gap()
    print("power_card_list = {}".format(power_card_list))

"********************************************************************"

"Functions to check the rank and suit of any card"


def suit_checker(card_you_want_to_check):
    global returned_suit
    global suit_checker

    returned_suit = ''

    for i in range(4):
        if card_you_want_to_check in suit_list[i-1]:
            suit_check = i
            break
    returned_suit = suit_list2[suit_check-1]


def rank_checker(f):
    global returned_rank
    global rank_check

    returned_rank = ''

    for i in range(13):
        if f in rank_list[i-1]:
            rank_check = i
            break
    returned_rank = rank_list2[rank_check-1]

# ********************************************************************"

# adding to the randomizing"""


def shuffle_deck():
    for p in range(100):
        shuffle(deck)

# ********************************************************************"
# Bot one


bot_one_list = []
x = 1

shuffle_deck()
if five_tester == "yes":
    for i in range(2):
        bot_one_list.append(fives[i])

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


# ********************************************************************#

"""adding to the randomizing"""
shuffle_deck()

"""Bot two"""
bot_two_list = []
x = 1

if five_tester == "yes":
    for i in range(2):
        bot_two_list.append(fives[i+2])

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

# ********************************************************************#


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

# tester variable (test = 1 for testing)
if test == 1:
    print("bot_one_list = {}".format(bot_one_list))
    print("bot_two_list = {}".format(bot_two_list))

# ********************************************************************"
# special function which checks if the card is in a power_card list


def power_card_checker(card_you_want_be_checked):
    global test

    global power_five
    global power_ace
    global power_mod
    global card_rank_number

    card_rank_number = 0

    """returning the rank of the card"""
    for i in range(13):
        if card_you_want_be_checked in rank_list[i]:
            card_rank_number = i

            # tester variable (test = 1 for testing)
            if test == 1:
                print("card_rank_number = {}".format(card_rank_number))
            break

    if card_rank_number == 4:
        power_five = 1
        power_ace = 0

    elif card_rank_number == 0:
        power_five = 0
        power_ace = 1

    else:
        power_five = 0
        power_ace = 0
# ********************************************************************"


current_card = ''
bots_list = [bot_one_list, bot_two_list]

"""function which automates bots and the player picking up"""


def pick_up(bot_number, number_of_cards):
    global bots_list
    global auto_tester

    current_bot_list = bots_list[bot_number-1]

    # tester variable (test = 1 for testing)
    if test == 1:
        if auto_tester == "no":
            print("current_bot_list = {}".format(current_bot_list))
        if auto_tester == "yes":
            print("Player list = {}".format(current_bot_list))

    for i in range(number_of_cards):

        # tester variable (test = 1 for testing)
        if test == 1:
            print("TRYING TO PICK UP A CARD FOR THE BOT")
        current_bot_list.append(deck[0])
        deck.remove(deck[0])


def pick_up_player(number_of_cards):

    for i in range(number_of_cards):
        player_list.append(deck[0])
        deck.remove(deck[0])


"""************************************************************************************************************************************************************************************************************"""

"""function which almost completely automates the bots turn"""

# making which_bot into a string (printing out "Bot One/Bot Two)


def bot_number_string(bot_number):
    global which_bot_text

    bot_number_list = ["One", "Two"]
    which_bot_text = bot_number_list[bot_number-1]


def bot_turn(which_bot, last_card_played):
    global test

    global bot_number_string  # function
    global current_card
    global power_five_count_compilation
    global power_five

    """implementing power cards"""
    global power_card

    gap()
    sleep(time2)
    print("********************************************************************")
    gap()

    """Checking if the card is a power card"""
    power_card_checker(current_card)

    # tester variable (test = 1 for testing)
    if test == 1:
        print("power five = {}".format(power_five))

    # ********************************************************************#

    bot_number_string(which_bot)

    """returning the rank and suit of the last card played"""
    suit_checker(last_card_played)
    current_suit = returned_suit

    rank_checker(last_card_played)
    current_rank = returned_rank

    """checking which bot_list is the right one to check"""
    current_bot_list = bots_list[which_bot-1]

    bot_list_len = len(current_bot_list)

    # tester variable (test = 1 for testing)
    if test == 1:
        gap()
        print("Bot {} List = {}".format(which_bot_text, current_bot_list))
        gap()

    power_five_count_compilation += 1

    """checking if the rank and suit of the card being checked matches with that of the last card played"""
    for i in range(bot_list_len):

        checking_card = current_bot_list[i-1]

        suit_checker(checking_card)
        checking_card_suit = returned_suit

        rank_checker(checking_card)
        checking_card_rank = returned_rank

        # ********************************************************************#

        # implementing power five for the situation
        if power_five == 1:

            power_five_compilation = power_five_count_compilation*5
            # tester variable (test = 1 for testing)
            if test == 1:
                gap()
                print("A FIVE HAS BEEN PLAYED!!!!!!!!!")
                gap()
            # tester variable (test = 1 for testing)
            if test == 1:
                print("power_five_count_compilation  = {}".format(power_five_count_compilation))
                print("power_five_compilation = {}".format(power_five_compilation))
                gap()

            if checking_card_rank == current_rank:
                bot_move(which_bot_text)
                current_card = checking_card
                print("{}{}".format(arrow, current_card))
                gap()

                power_card_checker(current_card)

                current_bot_list.remove(current_card)

                # tester variable (test = 1 for testing)
                if test == 1:
                    gap()
                    print(current_bot_list)
                    gap()
                break

            if i == bot_list_len-1:

                bot_move(which_bot_text)
                print("{}{}{} {}".format(arrow, "Picks Up ", power_five_compilation, "cards"))
                pick_up(which_bot, power_five_compilation)
                gap()

                # tester variable (test = 1 for testing)
                if test == 1:
                    gap()
                    print(current_bot_list)
                    gap()
                power_five_count_compilation = 0
                fives.remove(current_card)
                break

        # ********************************************************************#

        """checking if the card is valid card to be played from the current card"""
        if power_five == 0:
            power_five_count_compilation = 0

            if checking_card_rank == current_rank or checking_card_suit == current_suit:

                bot_move(which_bot_text)
                current_card = checking_card
                print("{}{}".format(arrow, current_card))
                gap()

                # tester variable (test = 1 for testing)
                if test == 1:
                    gap()
                    sleep(time1)
                    print("BOT_CURRENT_SUIT = {}, BOT_CURRENT_RANK = {}".format(current_suit, current_rank))
                    print("BOT_CHECKING_CARD_SUIT = {}, BOT_CHECKING_CARD_RANK = {}".format(checking_card_suit, checking_card_rank))
                    gap()
                    sleep(time1)
                power_card_checker(current_card)

                current_bot_list.remove(current_card)

                # tester variable (test = 1 for testing)
                if test == 1:
                    gap()
                    print(current_bot_list)
                    gap()

                """if a bot uses all their cards, they win"""

                if len(current_bot_list) == 1:
                    print("Bot {}".format(which_bot_text))
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

                # tester variable (test = 1 for testing)
                if test == 1:
                    gap()
                    print(current_bot_list)
                    gap()
                break

# ********************************************************************##********************************************************************##********************************************************************#


"""player's turn as a function"""


def print_player_list():
    print("Your Cards: ")
    print(player_list)


def player_turn(card):
    global test

    global power_five_count_compilation
    global power_five_compilation
    global current_card
    global auto_tester

    global tutorial

    sleep(time1)
    print("********************************************************************")
    gap()

    print_player_list()

    gap()
    print("Current Card")
    print(arrow, current_card)
    gap()
    sleep(time2)

    """implementing power cards"""
    global power_card

    print("Type in the number of the card you want to play in your list")
    if tutorial == 1:
        sleep(time2)
        print("('1' would be {}, '2' would be {} and so on.)".format(player_list[0], player_list[1]))
        sleep(time2)
    print("(If you want to pick up, enter '0')")
    sleep(time2)
    power_card_checker(current_card)

    "********************************************************************"
    if power_five == 1:
        """variable counts how many times a Five has been played"""
        power_five_count_compilation += 1
    if power_five == 0:
        power_five_count_compilation = 0
    "********************************************************************"

    while True:
        try:
            player_turn_index = int(input(''))

            if player_turn_index != 0:

                # tester variable (test = 1 for testing)
                if test == 1:
                    gap()
                    print("if player_turn_index != 0:")
                    print("power_five_count_compilation  = {}".format(power_five_count_compilation))

                if player_turn_index < 0 or player_turn_index > len(player_list):
                    print("Card cannot be played as you do not have {} cards".format(player_turn_index))
                    print("Please try again")
                    gap()

                "********************************************************************"

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

                    # tester variable (test = 1 for testing)
                    if test == 1:
                        gap()
                        sleep(time1)
                        print("STARTER_SUIT = {}, STARTER_RANK = {}".format(starter_suit, starter_value))
                        print("PLAYER_SUIT = {}, PLAYER_RANK = {}".format(player_suit, player_value))
                        gap()
                        sleep(time1)

                    # ********************************************************************#

                    # implementing power five for the situation
                    if power_five == 1:

                        # tester variable (test = 1 for testing)
                        if test == 1:
                            gap()
                            print("A FIVE HAS BEEN PLAYED!!!!!!!!!")
                            gap()
                        """Gives the total of cards that the player would have to pick up if they don't have a five, relative to how many fives have been played"""
                        power_five_compilation = power_five_count_compilation*5

                        if test == 1:
                            print("power_five_count_compilation  = {}".format(power_five_count_compilation))
                            print("power_five_compilation = {}".format(power_five_compilation))
                            gap()
                            print("right before 'rank_checker(current_card)'")
                        rank_checker(current_card)
                        if test == 1:
                            print("right after 'rank_checker(current_card)'")
                            gap()
                            gap()
                            print("right before 'current_card_rank = returned_rank'")
                        current_card_rank = returned_rank
                        if test == 1:
                            gap()
                            print("right after 'current_card_rank = returned_rank'")
                            print("player suit == {}, current_card_rank == {}".format(player_suit, current_card_rank))
                        if player_value == current_card_rank:
                            if test == 1:
                                print("CURRENTLY IN THE IF STATEMENT")
                            current_card = player_turn_card

                            if test == 1:
                                print("********************************************************************")
                                print("if player_suit == current_card_rank:")
                                print("********************************************************************")

                            player_print()
                            print("{}{}".format(arrow, current_card))
                            player_list.remove(current_card)

                            if len(player_list) == 1:
                                sleep(time1)
                                gap()
                                print("You")
                                print(arrow, "LAST CARD")
                                break
                            break
                        if player_value != current_card_rank:
                            print("The current card is a {}".format(current_card))
                            print("If you do not have a Five, then you must pick up {} cards from the deck".format(power_five_compilation))
                            gap()
                    if power_five == 0:
                        power_five_count_compilation = 0

                    # *******************************************************************

                    # if the last card played was not a power card, then the main bulk of code continues through here"""
                    if power_five == 0:
                        if test == 1:
                            print("if power_five == 0 and power_ace == 0 and power_two == 0:")

                        if starter_suit != player_suit and starter_value != player_value:
                            print("Card cannot be played as neither the suit or the rank match")

                        if starter_suit == player_suit or starter_value == player_value:
                            current_card = player_turn_card

                            player_print()
                            print("{}{}".format(arrow, current_card))
                            player_list.remove(current_card)

                            if len(player_list) == 1:
                                sleep(time1)
                                gap()
                                print("You")
                                print(arrow, "LAST CARD")

                            if len(player_list) == 0:
                                gap()
                                print("YOU WON!!!")
                                sys.exit()

                            break
            # ********************************************************************#

            if player_turn_index == 0:

                if power_five == 1:

                    power_five_compilation = power_five_count_compilation*5

                    if test == 1:
                        print("power_five_count_compilation  = {}".format(power_five_count_compilation))
                        print("power_five_compilation = {}".format(power_five_compilation))

                    pick_up_player(power_five_compilation)
                    fives.remove(current_card)

                if power_five == 0:
                    player_print()
                    print("{}{}".format(arrow, "Picks up"))
                    pick_up_player(1)
                    gap()

                print_player_list()
                break

        # catching a value error from the player
        except ValueError:
            gap()
            print("Please type in a valid number")

# ************************************************************************************************************************************************************************************************************


processing("Loading")
gap()
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
sleep(time2)

"""Setting up a little help suggestion"""
tutorial = 1
if auto_tester == "no":
    player_turn(starting_card)

tutorial = 0

"""setting the power_five_count_compilation (where you can stack multiple fives) to zero"""
power_five_count_compilation = 0

# ************************************************************************************************************************************************************************************************************#

"""running all the functions"""
if auto_tester == "no":
    while True:
        for i in range(2):
            if test == 1:
                print("power five = {}".format(power_five))
            bot_turn(i-1, current_card)
            gap()
            if test == 1:
                print("numbers of cards in 'deck' = {}".format(len(deck)))
            gap()
        if test == 1:
            print("power five = {}".format(power_five))
        player_turn(current_card)

# ************************************************************************************************************************************************************************************************************#

if auto_tester == "yes":
    while True:
        for i in range(2):
            bot_turn(i-1, current_card)
            gap()
            if test == 1:
                print("numbers of cards in 'deck' = {}".format(len(deck)))
            gap()
        if test == 1:
            print("power five = {}".format(power_five))

# ************************************************************************************************************************************************************************************************************#



