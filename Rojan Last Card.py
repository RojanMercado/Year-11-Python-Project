"""Imports"""
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

"***********************************************************"

club_counter = 0
for i in range(13):
    club = ("{} of {}".format(ranks[i], suits[0]))
    if club not in deck:
        deck.append(club)
        clubs.append(club)


diamond_counter = 0
for i in range(13):
    diamond = ("{} of {}".format(ranks[i], suits[1]))
    if diamond not in deck:
        deck.append(diamond)
        diamonds.append(diamond)

heart_counter = 0
for i in range(13):
    heart = ("{} of {}".format(ranks[i], suits[2]))
    if heart not in deck:
        deck.append(heart)
        hearts.append(heart)

spade_counter = 0
for i in range(13):
    spade = ("{} of {}".format(ranks[i], suits[3]))
    if spade not in deck:
        deck.append(spade)
        spades.append(spade)

print(deck)

