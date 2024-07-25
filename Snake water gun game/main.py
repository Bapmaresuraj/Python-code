import random

# Define constants for game choices
# 1 for snake, -1 for water, 0 for gun
SNAKE = 1
WATER = -1
GUN = 0

# Computer randomly chooses one option
computer = random.choice([SNAKE, WATER, GUN])

# Dictionary to map user input to the game choices
youDict = {"s": SNAKE, "w": WATER, "g": GUN}

# Dictionary to map game choices to their string representation
reverseDict = {SNAKE: "Snake", WATER: "Water", GUN: "Gun"}

# User inputs their choice
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

# Convert user input to game choice using the dictionary
you = youDict[youstr]

# Print choices of both the user and the computer
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Determine the result
if computer == you:
    print("It's a draw")
else:
    # Logic to determine who wins
    if (computer == WATER and you == SNAKE) or (computer == GUN and you == WATER) or (computer == SNAKE and you == GUN):
        print("You win!")
    else:
        print("You lose!")
