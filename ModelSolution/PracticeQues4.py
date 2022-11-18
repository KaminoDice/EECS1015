############################
# EECS1015, York University
# Practice questions #4
# Functions
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be copied or distributed without permision from the author.
# These examples provide at least *one way* of answering the questions.
# 
############################

import random
import time
# a global variable
Width = 30

# NOTE: Normally we would put all functions at the top of our code.
# But, to help make the solutions more readable,
# I'll keep the functions next to the questions.
# All functions should be written outside other functions.
# -> That is, you should not nest your functions (i.e., a function inside a function)
# -> unless asked to do so.
#

#--------------------------------------------------
# Question 1:
# function for Q1
def max_or_zero(a, b):
    if a == b:
        return 0
    elif a > b:
        return a
    else:
        return b

print("---Q1. Max or Zero---")
x = input("input x: ")
y = input("input y: ")
result = max_or_zero(x, y)
print(f"The max is: {result}")

#--------------------------------------------------
# Question 2:
# function for Q2
def divide_and_remainder(dividend, divisor):
    quotient  = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder      # returning two items

print("\n ---Q2. Quotient and remainder---")
YN = "Y"
while YN.upper()=="Y":
    x = int(input("Input a number : "))
    y = int(input("Input a divisor: "))
    quotient, remainder = divide_and_remainder(x, y)    # receiving two items from return
    print(f"({y} x {quotient}) + {remainder} = {x}")
    YN = input("Try again (y/n)? ")


#--------------------------------------------------
# Question 3
# functions for Q3
def get_card():
    card = random.randint(2, 13)
    return card

def print_card(card):
    if card <= 10:
        print(f"[{card:2}]")
    elif card==11:
        print("[ J]")
    elif card==12:
        print("[ Q]")
    elif card==13:
        print("[ K]")
    elif card==14:
        print("[ A]")

# assume that check_condition is either "H" or "L"
def did_i_win(card1, card2, check_condition):
    if card1 == card2:
        return False
    if check_condition.upper()=="H":  # see if card2 is "higher" in value
        if card2 > card1:
            return True
        else:
            return False
    if check_condition.upper()=="L": # see if card2 id "lower" in value
        if card2 < card1:
            return True
        else:
            return False

print("\n --- Q3. High/Low card game ---")
YN = "Y"
while YN=="Y":
    card1 = get_card()        # get first card using function
    print_card(card1)         # print it
    HL = input("Guess: high or low? [H/L] ").strip() # get input
    card2 = get_card()        # get second card using function
    print_card(card2)         # print it
    if did_i_win(card1, card2, HL):   # check if you won, this function returns a boolean
        print("You WON!")            
    else:
        print("YOU LOSE!")
    YN = input("Try again? [Y/N] ").upper()


# Question 4
#
print("\n----Q4. Bouncing ball----")
def input_range(prompt, min, max):     # just like your lab question
    num = int(input(prompt))
    while num < min or num > max:
        num = int(input(prompt))
    return num

def move_ball(pos, velocity):         # move and change direction
    global Width                      # width is global
    pos = pos + velocity
    if pos > Width:
        pos = Width
        velocity *= -1  # change direction
    if pos < 0:
        pos = 0
        velocity *= -1  # change direction
    # Print the string that draws the ball between the two | |
    print("|" + (pos)*" " + "*" + (Width-pos)*" " + "|")
    return pos, velocity             # returns new position and new velocity 

def bouncing_ball():                
    global Width                    # access global variable
    YN = "Y"
    while YN == "Y":
        Width = input_range("Input width (10-40): ", 10, 40)
        speed = input_range("Input speed   (1-7): ", 1, 7)
        pos = random.randint(3, Width-3)
        for i in range(1,10):
            pos, speed = move_ball(pos, speed)     # move ball
            time.sleep(0.10)                       # sleep to mimic delay

        YN = input("Try again? ").upper()

bouncing_ball()       # call bouncing_ball function












