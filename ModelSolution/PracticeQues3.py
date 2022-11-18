############################
# EECS1015, York University
# Practice questions #3
# Control structures (if, for, while)
# Author: (c) Michael S. Brown 
# This file cannot be copied or distributed without written permission from the author.
#
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################
import random

# Question 1
print("Q1.")
oddsum=0
evensum=0
for i in range(1,11):
    num = int(input((f"[{i:2}] Enter a number: ")))
    if num % 2 == 0:
        evensum += num
    else:
        oddsum += num
print(f"Sum of odd numbers: {oddsum}")
print(f"Sum of even numbers: {evensum}")


# Question 2
print("\nQ2.")
N = int(input("Enter N: "))
x = 5
while x <= N:
    print(x)
    x+=5

# Question 3
print("\nQ3")
for i in range(2, 82, 2):
    stri = str(i)
    if stri.find('6') != -1:
        print(f"*{i}* ", end="")
    else:
        print(f"{i} ", end="")
print()

# Questions 4
print("\nQ4.")
print("Times table")
# print header
for i in range(1,10):
    if i==1:
        print(" |  1", end="")
    else:
        print(f" {i:2}", end="")
print()
print("-"*30)
# print times table
for i in range(1,10):
    for j in range(1,10):
        if j==1:
            print(f"{i}|", end="")
        product = i*j
        print(f" {product:2}", end="")
    print()

# Question 5
print("\nQ5.")
for i in range(0,21, 1):
    f = i / 10
    if f!=2.0:
        print(f"{f}, ", end="")
    else:
        print(f"{f}")

# Question 6
print("Q6.")
name = input("Your name? ")
age = int(input("Your age? "))
if age < 15:
    print(f"Hello {name},")
elif age < 30:
    print(f"Hi {name},")
elif age < 54:
    print(f"Dear {name},")
else:
    print(f"Honourable {name},")
print("Welcome to York.")

# Question 7
print("\nQ7.")
count = 0
while count < 3:
    x = int(input("input: "))
    if x >= 5 and x <= 8:
        print("within range")
        count = count + 1
print("Stopping - three values within range inputted.")

# Question 8
print("\nQ8.")
YN = "Y"
while YN == "Y":
    previous = None
    first = None
    points = 0
    for i in range(1, 11):
        dice = random.randint(1,6)
        points += dice
        if i==1:
            first = dice                 # remember first dice (i.e. , when i==1)
            print(f"{dice}")
        else:
            if dice != previous:         # if not the first, check if equal to previous
                print(f"{dice}")
            else:
                print(f"{dice} - Lucky Repeat +10!")
                points += 10
        if i==10:                       # if last check with first
           if dice==first:
               print("First and last day the same - Super Lucky +20!")
               points += 20
        previous = dice                 # keep track of previous dice
    print(f"Total points: {points}")
    YN = input("Play again? ").upper()








