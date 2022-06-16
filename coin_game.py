"""
Name: Victor Dong
Purpose: Calculates the optimal way for the current player to beat the other player in a coin game
         ** Algorithm taken from lecture **
         ** Some code was referenced from https://docs.python.org/3/library/csv.html and https://www.w3schools.com/python/python_ref_list.asp (Reading in from csv and python list) **
"""
import csv
import sys
def coin_helper(temp, i, j):
        if i <= j:
            return temp[i][j]
        else:
            return 0

def coin_game(coins):
    
    length = len(coins)
    direction = []

    # Base Cases
    if length  == 1:
        return coins[0], "left"
    
    if length == 2:
        if coins[0] > coins[1]:
            direction = "left"
        else: 
            direction = "right"
        return max(coins[0], coins[1]), direction
    
    else:
    # Create a temp to subproblems
        temp = [[0 for x in range(length)] for y in range(length)]

        for subproblem in range(length):
            i = 0
            for j in range(subproblem, length):

                # Iterative steps from the recursive algorithm from lecture. Tried using recursion but it was significantly slower than using a 
                # iterative solution using a 2D array
                left = coins[i] + min(coin_helper(temp, i + 1, j - 1), coin_helper(temp, i + 2, j))
                right = coins[j] + min(coin_helper(temp, i, j - 2), coin_helper(temp, i + 1, j - 1))

                temp[i][j] = max(left, right)
                
                i += 1

        if left > right:
            direction = "left"
        elif left < right: 
            direction = "right"
        else: 
            direction = "either the left or right" # Current player loses no matter which coin is pick and the margin stays the same no matter which side is picked first
    
        return temp[0][length - 1], direction

numberOfArgs = len(sys.argv)
start = int(sys.argv[2])
end = int(sys.argv[3])

# Checks for correct input
if numberOfArgs < 4 or int(sys.argv[2]) <= 0 and int(sys.argv[3]) > 9999 or int(sys.argv[3]) < int(sys.argv[2]) :
    print("Invalid arguments... \nUsage: python coin_game.py [filename] [start] [end]")

else:
    coins = []

    with open(sys.argv[1], 'r') as file:
        for row in csv.reader(file, skipinitialspace=True):
            coins.append(int(row[0]))

    if len(coins) == 0: 
        print("Input is empty")
    
    else:
        p1Max, direction = coin_game(coins[start:end+1])
        p2Max = sum(coins[start:end+1]) - p1Max

        print('The maximum coins collected by current player is', p1Max, '\nThe margin by which they will win is' , p1Max - p2Max, '\nThe player should pick the', direction, 'coin')