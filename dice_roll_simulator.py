"""
# Import random
# define a function to roll the dice
# create a dictionary holds the drawings of dice
"""
import random


def roll_dice():
    dice_drawing = {
        1: (
            "-----"
            "|   |"
            "| o |"
            "|   |"
            "-----"
        ),
        2: (
            "-----"
            "|o  |"
            "|   |"
            "|  o|"
            "-----"
        ),
        3: (
            "-----"
            "|o  |"
            "| o |"
            "|  o|"
            "-----"
        ),
        4: (
            "-----"
            "|o o|"
            "|   |"
            "|o o|"
            "-----"
        ),
        5: (
            "-----"
            "|o o|"
            "| o |"
            "|o o|"
            "-----"
        ),
        6: (
            "-----"
            "|o o|"
            "|o o|"
            "|o o|"
            "-----"
        )
    }
    option = input("Roll dice? (Y/N)")

    while option.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"dice rolled {dice1} and {dice2}")
        print(dice_drawing[dice1])
        print(dice_drawing[dice2])
        option = input('Roll dice? (Y/N): ')

roll_dice()