################################
# EECS1015 York Univresity
# Lab 4 - Starter Code
# Name: Cao Huanrui
# Section A
# Student id: 219256809
# Email: saikoro@my.yorku.ca
################################
import random
import time


def print_student_info():
    print("Name: Cao Huanrui")
    print("Section A")
    print("Student id: 219256809")
    print("Email: saikoro@my.yorku.ca")


def task1():
    intN = get_int_input("How many times to move [2-20]?\t", 2, 20)
    sleepT = 0.001 * get_int_input("How long to delay [1-1000ms]?\t", 1, 1000)
    print(sleepT)
    boolR = get_yes("Randomize [Y/N]?\t")
    for i in range(1, intN + 1):
        draw_owl(i, boolR)
        time.sleep(sleepT)


def get_int_input(prompt, min_value, max_value):
    inNum = int(input(prompt))
    int_min_value = int(min_value)
    int_max_value = int(max_value)
    while (inNum < int_min_value) or (inNum > int_max_value):
        inNum = int(input(prompt))
    return inNum


def get_yes(prompt):
    str1 = input(prompt)
    while (str1 != "Y" and str1 != "y" and str1 != "N" and str1 != "n"):
        str1 = (input(prompt))
    if (str1 == "Y" or str1 == "y"):
        return True
    else:
        return False


def draw_owl(position, randomize):
    eye1 = "{o,o}"
    eye2 = "{-,o}"
    eye3 = "{o,-}"
    body = "/)_) "
    feet = ' " " '
    randomeye = random.randint(1, 3)
    for i1 in range(1, position + 1):
        print("", end=" ")
    if randomize:
        if randomeye == 1:
            print(eye1)
        elif randomeye == 2:
            print(eye2)
        elif randomeye == 3:
            print(eye3)
    else:
        print(eye1)
    for i2 in range(1, position + 1):
        print("", end=" ")
    print(body)
    for i3 in range(1, position + 1):
        print("", end=" ")
    print(feet)


def task2():
    amount = get_float_input("Input initial investment amount [1, 10000]?\t", 1, 10000)
    rate = get_float_input("Annual return rate [0-1]?", 0, 1)
    years = get_int_input("How many years [1-10]? ", 1, 10)
    r_amount = compute_return(amount, rate, years)
    if years == 1:
        print("Return in %d year is: $\t%10.2f" % (years, r_amount))
    else:
        print("Return in %d years is: $\t%10.2f" % (years, r_amount))
    global bool_new
    bool_new = get_yes("Compute new investment [Y/N]?")


def get_float_input(prompt, min_value, max_value):
    famount = float(input(prompt))
    while (famount < min_value) or (famount > max_value):
        famount = float(input(prompt))
    return famount


def compute_return(amount, rate, years):
    for i in range(1, years + 1):
        amount = amount + amount * rate
    return amount


def task3():
    global num_of_jumps
    max_odd = 1
    for i in range(1, 6):
        number_input = get_int_input("%d/5 Enter a number [1-100]: " % i, 1, 100)
        if (number_input % 2 != 0):
            max_odd = max(number_input, max_odd)
    print("Final max odd number: %d" % max_odd)
    num_of_jumps = max_odd


def task4():
    global floor
    frame1 = "  o   [%3d]\n /|\  \n / \  "
    frame2 = " \o/  [%3d]\n  |   \n / \  "
    input("Press enter to perform %d jumping jacks." % num_of_jumps)
    for i in range(1, num_of_jumps + 1):
        floor = i
        if (i % 2 != 0):
            print(frame1 % floor)
            time.sleep(0.3)
        else:
            print(frame2 % floor)
            time.sleep(0.3)


def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    while bool_new:
        task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")


if __name__ == "__main__":
    main()
