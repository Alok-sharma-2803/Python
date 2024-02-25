# Objective: Design a 2048 game you have played very often in your smartphone.

# Algorithm:
# 1. There is a 4*4 grid which can be filled with any number. Initially two random cells are filled with 2 in it. Rest cells are empty.
# 2. We have to press any one of four keys to move up, down, left, or right. 
#       When we press any key, the elements of the cell move in that direction such that if any two identical numbers are contained in that particular row 
#       (in case of moving left or right) or column (in case of moving up and down) they get add up and extreme cell in that direction fill itself with 
#       that number and rest cells goes empty again.
# 3. After this grid compression any random empty cell gets itself filled with 2.
# 4. Following the above process we have to double the elements by adding up and make 2048 in any of the cell. If we are able to do that we wins.
# 5. But if during the game there is no empty cell left to be filled with a new 2, then the game goes over.

import random as rn

rows, cols = (4, 4)
grid = [[0 for i in range(rows)] for i in range(cols)] # Deep copy of 1 list to make a 2d structure


# Initial position assignment
position = [0,1,2,3]
rand_pos1 = rn.choices(position, k=2)
rand_pos2 = rn.choices(position, k=2)

while(rand_pos1 == rand_pos2):
    rand_pos2 = rn.choices(position, k=2)

grid[rand_pos1[0]][rand_pos1[1]] = 2
grid[rand_pos2[0]][rand_pos2[1]] = 2

# Left

def shiftLeft(x): # x is a list
    list_temp = []

    for i in x:
        if(i != 0):
            list_temp.append(i) 
    
    while(len(list_temp) < len(x)):
        list_temp.append(0)
    
    return list_temp

def sumLeft(x):
    for i in range(0, len(x) - 2):
        if(x[i] == x[i + 1]):
            x[i] = x[i] + x[i + 1]
            x[i + 1] = 0


# Right

def shiftRight(x): # x is a list
    list_temp = []
    count = 0

    for i in range(0, len(x)):
        list_temp.append(0)

    for i in range(len(x) - 1, -1, -1):
        if(x[i] != 0):
            list_temp[len(list_temp) -1 - count] = x[i]
            count += 1
    
    return list_temp

def sumRight(x):
    for i in range(len(x) - 1, 1, -1):
        if(x[i] == x[i - 1]):
            x[i] = x[i] + x[i - 1]
            x[i - 1] = 0

# Up

def shiftUp(x): # x will be a 2d list

    list_temp = [[0 for i in range(len(x[0]))] for i in range(len(x[0]))]

    for i in range(0, len(x[0])): # i = column
        count = 0
        for j in range(0, len(x[0])): # j = row
            if(x[j][i] != 0):
                list_temp[count][i] = x[j][i]
                count += 1
    
    return list_temp

def sumUp(x):
    for i in range(0, len(x[0])):
        for j in range(0, len(x[0]) - 2):
            if(x[j][i] == x[j + 1][i]):
                x[j][i] = x[j][i] + x[j + 1][i]
                x[j + 1][i] = 0

# Down

def shiftDown(x): # x is a 2d list

    list_temp = [[0 for i in range(len(x[0]))] for i in range(len(x[0]))]

    for i in range(0, len(x[0])):
        count = len(x[0]) - 1
        for j in range(len(x[0]) - 1, -1, -1):
            if(x[j][i] != 0):
                list_temp[count][i] = x[j][i]
                count -= 1

    return list_temp

def sumDown(x): # x is a 2d list
    for i in range(0, len(x[0])):
        for j in range(len(x[0]) - 1, 0, -1):
            if(x[j][i] == x[j - 1][i]):
                x[j][i] = x[j][i] + x[j - 1][i]
                x[j - 1][i] = 0

# assign 2 to a random space

def randomAssignment(x):
    x1, y1 = rn.choices(position, k = 2)
    while(x[x1][y1] != 0):
        x1, y1 = rn.choices(position, k = 2)

    x[x1][y1] = 2

# Game end condition

def winCondition(x):
    for i in range(0, len(x[0])):
        for j in range(0, len(x[0])):
            if(x[j][i] == 2048):
                return True


def loseCondition(x):
    noZero = True
    for i in range(0, len(x[0])):
        for j in range(0, len(x[0])):
            if(x[j][i] == 0):
                noZero = False
    return noZero

print("""Commands are as follows : 
        'W' or 'w' : Move Up
        'S' or 's' : Move Down
        'A' or 'a' : Move Left
        'D' or 'd' : Move Right""")

while(1 == 1):

    [print(x) for x in grid].pop()

# User input
    user_input = input("Press a command: ").lower()
    
# User input processing
    if(user_input == 'w'):
        grid = shiftUp(grid)
        sumUp(grid)
        grid = shiftUp(grid)
        randomAssignment(grid)

    elif(user_input == 's'):
        grid = shiftDown(grid)
        sumDown(grid)
        grid = shiftDown(grid)
        randomAssignment(grid)

    elif(user_input == 'a'):
        for i in range(0, len(grid[0])):
            grid[i] = shiftLeft(grid[i])
            sumLeft(grid[i])
            grid[i] = shiftLeft(grid[i])
        randomAssignment(grid)
        
    elif(user_input == 'd'):
        for i in range(0, len(grid[0])):
            grid[i] = shiftRight(grid[i])
            sumRight(grid[i])
            grid[i] = shiftRight(grid[i])
        randomAssignment(grid)
        
    else:
        print("Invalid input! Try again")

# Exit condition
    if(winCondition(grid) == True):
        print("You win")
        break
    elif(loseCondition(grid) == True):
        print("You lose")
        break
    else:
        print("GAME NOT OVER")
