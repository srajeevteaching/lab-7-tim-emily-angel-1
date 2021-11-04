# Programmers: Tim Hunt, Emily Catanzariti, Angel Scott
# Course: CS151, Dr. Rajeev
# Date: 11/4/21
# Lab Number: 7
# Program Inputs: The number of times to roll the dice
# Program Outputs: List of sums that were rolled

# Import random module
import random

# Function to get number of rolls
def get_number_of_rolls():
    rolls = input("How many rolls?")
    while not rolls.isdigit():
        print("Sorry. Invalid input")
        rolls = input("How many rolls?")
    return int(rolls)

# Function to roll dice
def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum = roll1 + roll2
    return sum

# Function to create a histogram
def create_histogram():
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return list

# Main Function
def main():
    numberofrolls = get_number_of_rolls()
    sum = roll_dice()

    count = 0
    while count < numberofrolls:
