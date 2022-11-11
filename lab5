################################
# EECS1015, York University
# Lab 5 starting code
# Name: Cao Huanrui
# Section A
# Student id: 219256809
# Email: saikoro@my.yorku.ca
################################

import random


# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Cao Huanrui")
    print("Section A")
    print("Student id: 219256809")
    print("Email: saikoro@my.yorku.ca")


def task0():
    # Example of calling a function from taskX() functions.
    # you should write all functions "outside" your task1()-task4() functions.
    print_lab_info()


def task1():
    num_list = input_list()
    avg = compute_average(num_list)
    print("List average %.2f" % avg)
    again = input("Do again [Y/N]? ")
    while again == 'Y' or again == 'y':
        num_list = input_list()
        avg = compute_average(num_list)
        print("List average %.2f" % avg)
        again = input("Do again [Y/N]? ")


def input_list():
    num_list = []
    num = int(input("Input positive int: "))
    while num >= 0:
        num_list.append(num)
        num = int(input("Input positive int: "))
    return num_list


def compute_average(num_list):
    sum_list = 0
    if len(num_list) == 0:
        return 0
    else:
        for i in range(len(num_list)):
            sum_list = sum_list + num_list[i]
        avg = sum_list / len(num_list)
        return avg


def task2():
    initial_string = input("Input a long string: ")
    initial_list = [*initial_string.upper()]
    set_list = sorted(set(initial_list))
    for char in set_list:
        star = "*"
        print("'" + char + "'" + " |" + star * initial_list.count(char))


def task3():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']',
               'K': '1',
               'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5',
               'V': '!',
               'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D',
               '7': 'E',
               '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ': '_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J',
               '1': 'K',
               '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U',
               '!': 'V',
               '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6',
               'E': '7',
               '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}
    code_string = input("Input message : ")
    code_list = [*code_string.upper()]
    coder = input("Encode (E) or Decode (D)? ")
    if coder == 'E':
        for char in code_list:
            if char in encoder.keys():
                print(encoder[char], end="")
            else:
                print("\nInvalid input")
                break
    elif coder == 'D':
        for char in code_list:
            if char in decoder.keys():
                print(decoder[char], end="")
            else:
                print("\nInvalid input")
                break
    print("")
    again = input("Encode/decode again [Y/N]? ")
    while again == 'Y' or again == 'y':
        code_string = input("Input message : ")
        code_list = [*code_string.upper()]
        coder = input("Encode (E) or Decode (D)? ")
        if coder == 'E':
            for char in code_list:
                if char in encoder.keys():
                    print(encoder[char], end="")
                else:
                    print("\nInvalid input")
                    break
        elif coder == 'D':
            for char in code_list:
                if char in decoder.keys():
                    print(decoder[char], end="")
                else:
                    print("\nInvalid input")
                    break
        print("")
        again = input("Encode/decode again [Y/N]? ")


def task4():
    input_num = input("Enter 5 numbers between 1-20: ")
    input_split = set(input_num.split(" "))
    while len(input_split) != 5:
        input_num = input("Enter 5 numbers between 1-20: ")
        input_split = set(input_num.split(" "))
    ran_set = random_set()
    print_set(ran_set, "Computer's numbers:")
    input_set = set(map(int, input_split))
    com_set = ran_set & input_set
    len_set = len(com_set)
    if len_set == 1:
        print_set(com_set, "1 matche found: ")
    elif len_set == 0:
        print("NO MATCHES")
    elif len_set == 5:
        print("YOU WIN!")
    else:
        com_str = str(len_set) + " matches found: "
        print_set(com_set, com_str)
    again = input("Try again [Y/N]? ")
    while again == 'Y' or again == 'y':
        input_num = input("Enter 5 numbers between 1-20: ")
        input_split = set(input_num.split(" "))
        while len(input_split) != 5:
            input_num = input("Enter 5 numbers between 1-20: ")
            input_split = set(input_num.split(" "))
        ran_set = random_set()
        print_set(ran_set, "Computer's numbers:")
        input_set = set(map(int, input_split))
        com_set = ran_set & input_set
        len_set = len(com_set)
        if len_set == 1:
            print_set(com_set, "1 matche found: ")
        elif len_set == 0:
            print("NO MATCHES")
        elif len_set == 5:
            print("YOU WIN!")
        else:
            com_str = str(len_set)+" matches found: "
            print_set(com_set, com_str)
        again = input("Try again [Y/N]? ")


def random_set():
    ran_set = set()
    for i in range(5):
        ranint = random.randint(1, 20)
        while ranint in ran_set:
            ranint = random.randint(1, 20)
        ran_set.add(ranint)
    return ran_set


def print_set(aSet, prompt):
    print(prompt, end="")
    for i in aSet:
        print(i, end="")
        print(" ", end="")
    print("")


def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()


if __name__ == "__main__":
    main()
