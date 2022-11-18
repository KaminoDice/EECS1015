#####################################################################################
# EECS1015 - Lab 3 - Sample Solution
# York University
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission of the author.
# (e.g., you can't upload this to illegal dissemination sites such as course hero)
#
#####################################################################################

import random                       # we need to input the random module

print("---- Lab 3 ----")
print("Name: Michael S. Brown")
print("Section A")
print("Student id: 39483333")
print("Email: JustinT@canada.gov")

# Task 1
print("\n---- Task 1: Simple order ----")   # Print the menu
print("**Select menu item**\n"+
      " (1) Coke  [$1.00]\n"+
      " (2) Dosa  [$2.50]\n"+
      " (3) Pizza [$2.25]\n"+
      " (4) Taco  [$1.50]\n"+
      " (5) Tea   [$1.00]")
item = int(input("Selection: "))            # get input, convert to int
amount = None                               # define variable amount (set to None)
if item==1:
    amount=1.00
elif item==2:
    amount=2.50
elif item==3:
    amount=2.25
elif item==4:
    amount=1.50
elif item==5:
    amount=1.00
else:
    print("Invalid selection - setting amount to $0")
    amount=0

# print second choice (age group)
print("**Discount**\n"  
      "(C) Child [under 18] (50% discount)\n"+
      "(A) Adult [18-64]\n"+
      "(S) Senior [65+] (25% discount)")
choice = input("Selection age: ").upper()
discount = None                                     # define discount (set to None)
if choice=="C":
    discount=0.50
elif choice=="A":
    discount=0
elif choice=="S":
    discount=0.25
else:
    print(f"'{choice}' is an invalid selection! Extra charge for you!")
    discount=-0.25

adjustment = amount * discount                  # compute amount of discount  
final = amount - adjusted                       # compute final amount 
print(f"Amount   ${amount:6.2f}  ")
print(f"Discount ${adjustment:6.2f}")
print(18*"-")
print(f"Total    ${final:6.2f}")

# Task 2
print("\n---- Task 2: Draw circle ----")
r = 0                                           # set radius to r=0 (which is invalid)
while r <= 0 or r > 10:                         # while range is invalid
    r = int(input("Input size between 1-10: ")) # ask for input

# draw circle    
for y in range(-10,11):                         # outer loop -> loop y from -10 to 10 
    for x in range(-10,11):                     #   inner loop -> loop x from -10 to 10
        if x**2 + y**2 <= r**2:                 # if inside (or on) circle 
            print("*", end="")                  # print * with no newline
        else:
            print(".", end="")                  # else, print . with no newline
    print("")                                   # print a newline


# task 3
print("\n---- Task 3: Dice pair expected value ----")
tryagain = "Y"                                  # set tryagain to "Y"
while tryagain=="Y":                            # while condition
    sum = 0                                     # set sum to 0
    times = int(input("Roll dice how many times? "))      # get N of times to roll
    for i in range(1,times+1):                            # loop i from 1 to N
        dice1 = random.randint(1,6)                       # get first dice
        dice2 = random.randint(1,6)                       # get second dice
        amount=dice1+dice2                                # compute dice amount
        print(f"[{dice1}]  [{dice2}] -- {amount:2}   Roll {i}")   # output
        sum += amount                                     # add to sum
    result = sum / times
    print(f"Average dice pair value: {result:.2f}")       # print average
    tryagain = input("Try again [Y/N]? ").upper()         # try again


# task 4
print("\n---- Task 4: Compute PI ----")
nmax = int(input("Input number of terms, M: "))           # input M
sum = 0                                                   # sum = 0
for n in range(0,nmax+1):                                 # loop from 0 to M+1
    numerator = (-1)**n                                   # compute top of fraction
    denominator = 2*n+1                                   # compute bot of fraction
    print(f"n={n}  . . . adding fraction: {numerator}/{denominator}")   # print as required
    sum = sum + (numerator/denominator)                   # add term to sum
    pi = 4*sum                                            # compute pi
    print(f" our  pi = {pi:.11f}")                        # print our pi (precision 11 -- yes, lab had a mistake)
    print(f" real pi = 3.14159265359")                    # print real pi



# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")