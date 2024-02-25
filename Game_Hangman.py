# The Hangman program randomly selects a secret word from a list of secret words.
# The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
# When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
# For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

# Algorithm:
# 1. Randomly select a word from a list of words
# 2. Ask user to guess an alphabet
# 3. If that alphabet is in the word, replace the blank space(s) with the alphabet
# 4. If the alphabet isn't in the word, strike once character in HANGMAN
# 5. If the user guesses the word before the last character in HANGMAN is striked out, he wins
# 6. Else, he loses!



import random as rn

hangman = "HANGMAN"
txt = "Apple Banana Guava Grapes Pineapple Papaya"
word_list = txt.lower().split(" ")

word_rand = rn.choice(word_list)
word_copy = word_rand
wrong_guess = 0

guess = "_"
for i in range(0, len(word_rand) - 1):
    guess += "_"

hangman_const = 0
while(1 == 1):
    if(hangman[len(hangman) - 1] == u'\u0336'):
        print("You lose!")
        break
    if("_" not in guess):
        print("The word was {}".format(guess))
        print("You Win!")
        break
    
    print("\n" + hangman)
    print(guess)
    input_usr = input("Guess an alphabet: ").lower()

    temp = word_rand
    count = 0

    if(input_usr in word_copy):
        while(input_usr in temp):

            position = int(temp.find(input_usr)) + count
            guess = guess[0:position] + input_usr + guess[position + 1: len(guess)]
            temp = temp.replace(input_usr, "", 1)
            
            word_copy = word_copy.replace(input_usr, "", 1)
            count += 1
    else:
        wrong_guess += 1
        print(wrong_guess)
        hangman = hangman[0:wrong_guess + hangman_const] + u'\u0336' + hangman[wrong_guess + hangman_const : len(hangman)]
        hangman_const += 1
