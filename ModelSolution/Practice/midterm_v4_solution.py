###########################################
# EECS1015 - York University
# Midterm Exam #4 - Example solution
# (c) Michael S. Brown
# This code cannot be distributed without
# permission from the author.
###########################################

import time               # <- needed for task4
direction = 1            # <- global variable needed for task 4
#
# Define functions for task 4 here
#


def compute_next_position(pos, speed):
    global direction
    pos = pos + (speed * direction)
    if pos > 30:
        pos = 30
        direction = -1
    elif pos < 0:
        pos = 0
        direction = 1
    return pos

def print_arrow(pos):
    global direction
    if direction==-1:
        print(pos*" " + "<")
    else:
        print(pos*" " + ">")
    time.sleep(0.2)

def task4():
    print("\n--- Task 4 ---")
    # write your code below
    yn=input("Draw arrow [Y/N]? ").upper()
    while yn=="Y":
        speed = int(input("Speed between [3-5]: "))
        pos = 5
        for i in range(1,21):
            pos = compute_next_position(pos, speed)
            print_arrow(pos)
        yn=input("Draw arrow [Y/N]? ").upper()

def task3():
    print("\n--- Task 3 ---")
    # write your code below
    total = 100
    while total > 0:
        num = 101
        print(f"Current total [{total:3d}]")
        while num > total or num < 0:
            num = int(input(f"Enter amount to remove: "))
        total = total - num
    print(f"Total is 0")


def task2():
    print("\n--- Task 2 ---")
    # write your code below
    my_string = input("Input a string: ")
    length = len(my_string)
    print(f"String length is {length}.")
    index = int(input("Input index: "))
    x = input("Front or Back (F/B)? ").upper().strip()
    new_string = ""
    if x == "F":
        new_string = my_string[:index]
    else:
        new_string = index * "-" + my_string[index:]
    print(f"Original: |{my_string}|")
    print(f"Modified: |{new_string}|")

def task1():
    print("\n--- Task 1 ---")
    # write your code below
    m = int(input("Enter number of minutes : "))
    days = m // (60 * 24)
    minutes_left = m % (60 * 24)
    hours = minutes_left // 60
    minutes = minutes_left % 60
    print(f"{m:6} minutes is:")
    print(f"|{days:2}| days |{hours:2}| hours |{minutes:2}| minutes")

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