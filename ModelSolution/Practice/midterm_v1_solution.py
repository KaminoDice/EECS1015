###########################################
# EECS1015 - York University
# Midterm Exam #1 - Example solution
# (c) Michael S. Brown
# This code cannot be distributed without 
# permission from the author.
###########################################

import math             # <- needed for task 1
amount = 0.0            # <- needed for task 4

#
# Define functions for task 4 here
#
def get_rate():
    num = 0
    while num <= 0 or num > 100:
        num = int(input("Input percentage [1-100]: "))
    rate = num / 100
    return rate

def compute_return(rate):
    global amount
    new_amount = amount + amount * rate
    return new_amount

def print_result(new_amount, rate):
    global amount
    print(f"[${amount:10.2f}] initial amount.")
    print(f"[x{rate:10.2f}] rate.")
    print(f"[${new_amount:10.2f}] new amount.")

def task4():
    print("\n--- Task 4 ---")
    # write your code below
    YN = input("Compute a return [Y/N]?  ").strip().upper()
    global amount
    while YN == "Y":
        amount = float(input("Input amount: "))
        rate = get_rate()
        new_amount = compute_return(rate)
        print_result(new_amount, rate)
        YN = input("Again [Y/N]? ").strip().upper()

def task3():
    print("\n--- Task 3 ---")
    # write your code below
    num = 0
    total = 0
    while num >= 0:
        print(f"Current total [{total:4d}]")
        num = int(input("Input number between 1-20: "))
        if num >= 1 and num <= 20:
            total = total + num
        elif num >= 0:
            print(f"Invalid number {num}!")
    print(f"Final total [{total:4d}]")

def task2():
    print("\n--- Task 2 ---")
    # write your code below
    my_string = input("Enter a string: ")
    slice = input("Slice [Y/N]? ").upper().strip()
    repeat = input("Repeat [Y/N]? ").upper().strip()
    if slice == "Y":
        cut = len(my_string) // 2
        my_string = my_string[0:cut]
    if repeat == "Y":
        my_string = my_string * 5
    print(my_string)

def task1():
    print("\n--- Task 1 ---")
    # example of using sqrt
    # x = 4
    # x_sr = math.sqrt( x )
    # print(x_sr)
    # write your code below
    print("Input the first point:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    print("Input the second point:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(f"P1 ({x1:6.2f}, {y1:6.2f})")
    print(f"P2 ({x2:6.2f}, {y2:6.2f})")
    print(f"Distance between P1 and P2: '{distance:6.2f}'")

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