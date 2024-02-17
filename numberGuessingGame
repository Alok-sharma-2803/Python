# Objective: Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses


import random as rn
import math as m

range_min = int(input("Enter the lower bound: "))
range_max = int(input("Enter the upper bound: "))
rand_num = rn.randint(range_min, range_max)
guess_max = m.ceil(m.log((range_max - range_min + 1), 2))
guess_count = 0
input_num = range_min - 1

while(input_num != rand_num):
    
    guess_count = guess_count + 1
    if(guess_count > guess_max):
        print("Better Luck Next Time!\n")
        break

    input_num = int(input("Guess an integer: "))

    if(input_num > rand_num):
        print("Try Again! You guessed too big\n")
    elif(input_num < rand_num):
        print("Try Again! You guessed too small\n")
    else:
        print("That's right! Congratulations")
        print("Total Number of Guesses = {}\n".format(guess_count))
        break
