#!/usr/bin/python env
import random

highest = 20
answer = random.randrange(highest)
guess = raw_input("Guess a number from 0 to %d: " %highest)

while(int(guess) != answer):
    if(int(guess) < answer):
        print "You guess lower"
    else:
        print "You Guess Higher"

    guess = raw_input("Guess a number from 0 to %d: " %highest)

raw_input("You are a winner")
