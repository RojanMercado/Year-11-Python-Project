#Imports
from random import*
from random import shuffle

"""Basic Functions"""
def gap():
    print("")
def player_print():
    print("Your turn: ")
def bot_one_print():
    print("Bot One's Turn: ")
def bot_two_print():
    print("Bot Two's Turn: ")

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
        suit_list[e].append(card)
        rank_list[i].append(card)
        if card not in deck:
            deck.append(card)

print(deck)
deck = len(deck)

"********************************************************************"

"Functions to check the rank and suit of any card"

def suit_checker(suit_you_want_to_check):
    global suit_sorter

    for i in range(4):
        print(i)
        if suit_you_want_to_check in suit_list(i):
            suit_check = i
            break
    print(suit_check)
    suit_sorter = suit_list2[suit_check]

def rank_checker(rank_you_want_to_check):
    global rank_sorter

    for i in range(13):
        if rank_you_want_to_check in rank_list[i]:
            rank_check = i
            break
    rank_sorter = rank_list2[rank_check]

suit_checker("5 of Hearts")
print(suit_sorter)

rank_checker("5 of Hearts")
print(rank_sorter)









