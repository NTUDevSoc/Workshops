# DevSoc Workshop 2020 - Jarad JB
import random

for x in range(0, 3):
    userChoice = 0  # This keep track of our users choice
    pcChoice = 0
    result = "Lose"

    userChoice = int(input("Rock(1), Paper(2), Scissors(3)? "))

    pcChoice = random.randint(1, 3)
    print("PC chose ", pcChoice)

    if userChoice == pcChoice:
        result = "Draw"

    elif userChoice == 1 and pcChoice == 3:
        result = "Win"
    elif userChoice > pcChoice:
        result = "Win"

    else:
        result = "Lose"

    print("Game Over, you " + result + "!")