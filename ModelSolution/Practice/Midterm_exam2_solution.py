###########################################
# EECS1015 - York University
# Midterm Exam #2 - Example solution
# (c) Michael S. Brown
# This code cannot be distributed without 
# permission from the author.
###########################################

import random             # <- needed for task 4

#
# Define functions for task 4 here
#
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2

def compute_score(dice1, dice2):
    sum = dice1 + dice2
    if (dice1 == dice2):
        sum = 20
    return sum

def print_dice_result(dice1, dice2, score):
    print(f"[{dice1:2d}] [{dice2:2d}] - Result {score:2d}")

def task4():
    print("\n--- Task 4 ---")
    # write your code below
    YN = input("Roll Dice [Y/N]?  ").strip().upper()
    global amount
    while YN=="Y":
         dice1, dice2 = roll_dice()
         score = compute_score(dice1, dice2)
         print_dice_result(dice1, dice2, score)
         YN = input("Again [Y/N]? ").strip().upper()

def task3():
    print("\n--- Task 3 ---")
    # write your code below
    N = int(input("Maximum N: "))
    for i in range(0, N, 1):
        line = "*" * i + "\\"
        print(line)
    for i in range(N, -1, -1):
        line = "*" * i + "/"
        print(line)

def task2():
    print("\n--- Task 2 ---")
    menu = "Select: [P]izza ($5) or [W]ater ($2)"
    print(menu)
    x = input("Choice: ").strip().upper()
    item = ""
    cost = 0
    if x == "P":
        cost = 5
        item = "Pizza"
    elif x == "W":
        cost = 2
        item = "Water"
    x = input("Upgrade size [Y/N]? ").upper().strip()
    if x == "Y":
        cost = cost * 1.5
        item = "Large " + item
    else:
        item = "Regular " + item
    print(f"Item: {item:20s}${cost:5.2f}\n")

def task1():
    print("\n--- Task 1 ---")
    w = float(input("Input the width  : "))
    h = float(input("Input the height : "))
    l = float(input("Input the length : "))
    volume = w * h * l
    surface_area = 2 * (l * w + l * h + h * w)
    print(f"Cuboid Volume\\Surface area\t\t'{volume:8.2f}'\\'{surface_area:8.2f}'")


def task0():
    # Please don't forget this section. You'll lose 10 points if you forget!
    print("\n--- Task 0 ---")
    print("Name: XXXXXXXXXX")
    print("Student ID: XXXX")
    print("Section: A or B ")
    print("Lab Section: EXAMPLE - LAB01B or LAB04A")

def main():
    task0()
    task1()        
    task2()      
    task3()
    task4()
    input("\nPress enter to end.")

if __name__ == "__main__":
    main()