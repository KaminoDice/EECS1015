###########################################
# EECS1015 - York University
# Midterm Exam #3 - Example solution
# (c) Michael S. Brown
# This code cannot be distributed without 
# permission from the author.
###########################################


import math               # <- needed for task1
import random             # <- needed for task 4
postive = True            # <- global variable needed for task 4
#
# Define functions for task 4 here
#
def compute_function(x):
    global positive
    if x < 0:
        positive = False
    else:
        positive = True
    x = (x/2)**2 + 3
    return int(x)

def compute_string(N):
    global positive
    x = "." * N
    if positive:
        x = x + "\\"
    else:
        x = x + "/"
    return x

def task4():
    print("\n--- Task 4 ---")
    # write your code below
    for x in range(-10,11):
        y = compute_function(x)
        line = compute_string(y)
        print(line)

def task3():
    print("\n--- Task 3 ---")
    # write your code below
    YN = input("Roll dice [Y/N]? ").upper().strip()
    while YN == "Y":
        count = 0
        for i in range(1, 11):
            dice = random.randint(1, 6)
            print(f"Roll {i:2d}  [ {dice} ]")
            if dice == 6:
                count = count + 1
        print(f"You rolled *{count}* sixes.")
        YN = input("Roll dice [Y/N]? ").upper().strip()

def task2():
    print("\n--- Task 2 ---")
    # write your code below
    my_string = input("Input string: ")
    input_string = my_string
    replace = input("Replace or cut [R/C]: ").upper()
    if replace == "R":
        x = input("Character to replace? ")[0]
        y = input("New character? ")[0]
        my_string = my_string.replace(x, y)
    elif replace == "C":
        x = input("Character to cut? ")[0]
        my_string = my_string.replace(x, "")
    print(f"Input string    : '{input_string}'")
    print(f"Modified string : '{my_string}'")

def task1():
    print("\n--- Task 1 ---")
    # write your code below
    # print(math.pi) <- built in value of pi
    # x = 4.0
    # y = math.sqrt(x) <- example of using square root
    # print(y)
    r = float(input("Input the radius : "))
    h = float(input("Input the height : "))
    volume = math.pi * r ** 2 * (h / 3)
    l = math.sqrt(h**2 + r ** 2)
    surface_area = math.pi * r ** 2 + math.pi * r * l
    print("Cone size:")
    print(f"{volume:10.4f}\t\t \\Volume\\")
    print(f"{surface_area:10.4f}\t\t \\Surface Area\\")

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