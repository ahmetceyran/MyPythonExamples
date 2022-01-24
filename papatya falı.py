#!/usr/bin/python
# D. Vrajitoru, C463/B551 Spring 2008
 
# Game from A. Trautman.

# Implementing a program that will play the Nintendo DS game of
# loves-me / loves-me-not.

# The game starts with a number of petals to pluck from a flower. To
# make the game more interesting, each player can remove up to 4
# petals from the flower and at least 1. In the end the player wins if
# either the game ends with a "loves me" for him or a "loves me not"
# for the adversary. The first move is a "loves me".

# This is a small example of implementing the MinMax and Alpha-Beta
# algorithms.


from random import *

# A function that runs the game starting from a given number of
# petals. The first turn is always left to the player and the first
# petal is always "loves me". The function alternates the moves
# between the player and one algorithm - alpha-beta or minmax - until
# there are no petals left to remove.

def game(number):
    petals = number
    turn = 0 #start with the player
    loves_me = True #first petal is always "loves me"
    while petals:
        for i in range(petals):
            if (i + int(loves_me)) % 2 == 1:
                print ("L"),
            else:
                print ("N"),
        print (" ") # to end the line
        if turn == 0: # player
            print ("Enter your move [1 - 4]:")
            move = int(input())
            if petals <= move:
                move = petals
        else: # our algorithm
            move, score = MAX_AB(petals, loves_me, minus_inf, plus_inf)
            print ("My move: "), move
        if move % 2 == 1: # if we removed an odd number of petals,
                          # the loves_me changes
            loves_me = not loves_me
        turn = 1-turn
        petals = petals - move
    if term_score(0, loves_me, turn):
        print ("I win this round")
    else:
        print ("You win this round")


if __name__ == '__main__':
    game_on = True
    while game_on:
        number = randint(10,20) # intial number of petals
        game(number)
        print ("Would you like to try again? [0: no / 1: yes]")
        game_on = int(input())
