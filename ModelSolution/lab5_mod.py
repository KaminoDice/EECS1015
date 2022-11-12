#####################
# EECS1015 - Fall 2022
# Lab 5 - Model solution
# Michael S. Brown
#
######################

import random

# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Douglas F")
    print("Section A")
    print("Student id: 9999999")
    print("Email: df@ontario.ca")

# input list
def input_list():
    num = 0
    myList = []                                     # create empty list
    while num >= 0:                                 # while num is positive
        num = int(input("Input positive int: "))    # get input
        if num >= 0:                                # if it is positive
            myList.append(num)                      # add to list

    return(myList)

# easy compute average function
def compute_average(alist):
    sum = 0
    if len(alist) == 0:
        return 0
    for num in alist:
        sum = sum + num
    average = sum / len(alist)
    return average

# Task 1
def task1():
    YN = "Y"
    while YN == "Y":                    # loop while Y
        l = input_list()
        a = compute_average(l)
        print(f"List average {a:.2f}")
        YN = input("Do again [Y/N]? ").strip().upper()  # get input from user


# Task 2
def task2():
    s = input("Input a long string: ").upper()          # get a long string
    sList = list(s)                                     # convert to list
    keys = set(sList)                                   # convert to set
    sDict = {}                                          # make empty dict
    for k in keys:                                      # items in key
        sDict[k] = 0                                    # make dict item set to 0
    for c in sList:                                     # for characters in list
        sDict[c] = sDict[c] + 1                         # increase the value in the dict
    keyList = list(keys)                                # make keys into list
    keyList.sort()                                      # sort (not required)
    for c in keyList:                                   # loop through each key
        v = sDict[c]
        print("'{}' |{}".format(c,'*'*v))               # print out result

# task 3
def task3():

    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']', 'K': '1',
     'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5', 'V': '!',
     'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D', '7': 'E',
     '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ':'_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J', '1': 'K',
     '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U', '!': 'V',
     '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6', 'E': '7',
     '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}

    YN = "Y"
    while YN=="Y":                                                          # YN loop
        msg = input("Input message : ").strip().upper()                     # get messsage
        ED = input("Encode (E) or Decode (D)? ").strip().upper()            # get E/D

        if ED == "E":                           # if encode
            print("Encoded message: ")
            for i in msg:                       # loop through the string
                print(encoder[i], end="")       # printout encoded char
            print()                             # print new line
        else:
            print("Decoded message: ")          # if decode (I only check "E")
            for i in msg:                       # loop through the string
                print(decoder[i], end="")       # printout decoded char
            print()                             # print new line

        YN = input("Encode/decode again [Y/N]? ").strip().upper()

# function for task 4
# generate random set of 5 numbers
def random_set():
    numbers = set()                                 # create a step
    while len(numbers) < 5:                         # need a while loop
        new_number = str(random.randint(1, 20))     # make rand # a string
        numbers.add(new_number)                     # add -- if it is a duplicate the set will not repeat it
    return numbers

# funciton for task 4
# Just prints out the set
def print_set(aSet, prompt="set: "):
    print(prompt, end="")
    for i in aSet:
        print(f"{i} ", end="")
    print()

# task 4
def task4():
    YN = "Y"
    while YN == "Y":                                                   # Y/N loop
        x = set(input("Enter 5 numbers between 1-20: ").split())       # get input, split into set
        if len(x) != 5:                                                # if not 5, continue loop
            continue
        y = random_set()                                               # get random set
        print_set(y, prompt="Computer's numbers: ")                    # print
        common = x.intersection(y)                                     # find intersection
        common_len = len(common)                                       # how many in intersection set
        if common_len == 0:                                             # if 0
            print("NO MATCHES!!")
        elif common_len == 5:                                           # else print matches
            print_set(common, f"{common_len} matches found: ")          # you win
            print("YOU WIN!!")
        else:
            print_set(common, f"{common_len} matches found: ")          # else just print

        YN = input("Try again [Y/N]? ").strip().upper()                 # repeat


def main():
    print_lab_info()

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