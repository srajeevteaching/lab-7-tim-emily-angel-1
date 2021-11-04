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
    histogram = create_histogram()
    sum = roll_dice()

    count = 0
    while count <= numberofrolls:
        if sum == 2:
            list[0]+=1
        elif sum == 3:
            list[1]+=1
        elif sum == 4:
            list[2]+=1
        elif sum == 5:
            list[3]+=1
        elif sum == 6:
            list[4]+=1
        elif sum == 7:
            list[5]+=1
        elif sum == 8:
            list[6]+=1
        elif sum == 9:
            list[7]+=1
        elif sum == 10:
            list[8]+=1
        elif sum == 11:
            list[9]+=1
        elif sum == 12:
            list[10]+=1
