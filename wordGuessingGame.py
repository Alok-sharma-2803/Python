# In this game, there is a list of words present, out of which our interpreter will choose 1 random word. 
# The user first has to input their names and then, will be asked to guess any alphabet. 
# If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. 
# The user will be given 12 turns(which can be changed accordingly) to guess the complete word.


import random as rn

name = input("What is your name? ")
print("Good luck! {} ".format(name))

word_list = ['rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks']
word_rand = rn.choice(word_list)
word_copy = word_rand
temp = "_"

for i in range(0, len(word_copy) - 1):
    temp += "_"

i = 1
while(i <= 12):
    if("_" not in temp):
        print("You win! The word is: " + temp)
        break

    input_char = input("Guess a character: ").lower()

    if(input_char in word_copy):
        
        temp2 = word_rand
        occurance_count = 0
        while(input_char in temp2):
            position = int(temp2.find(input_char)) + occurance_count
            temp = temp[0:position] + temp[position].replace("_", input_char) + temp[position + 1 : len(temp)]
            temp2 = temp2.replace(input_char, "", 1)
            occurance_count += 1
        
        word_copy = word_copy.replace(input_char, "")
        
    else:
        if(i == 12):
            print("You loose!")
            break
        else:
            i+=1
            print("Try Again!")
            print("You have {} attempt(s) left\n".format(13 - i))
    
    for j in temp:
        print(j)
