######################################
# EECS1015 - Fall 2022
# Author: Michael S. Brown
# (c) This code cannot be distributed without permssion of the author.
# Lab 6 - Collections and nested collections - Sample solutions
#####################################

import random

def print_student_info():
    print("Name: Guido van Rossum")
    print("ID: 47394849")
    print("Section A")
    print("email: lookhimup@python.org")

def task0():
    print_student_info()

# Functions for task 1
# Write the function average_num() outside your task1() function.
def average_nums(*nums):     # *nums will be a tuple
    sum = 0
    N = len(nums)           # get length
    if N==0:                # if length is 0, return 0
        return 0
    for i in nums:          # sum items in tuple
        sum = sum + i
    return sum / N          # return divided by length for average

# task 1 code
def task1():
    yn = "Y"
    while yn == "Y":
        choice = int(input("Input 4 or 5 numbers? "))                   # input 4 or 5
        if choice==4:
            nums = input("Input 4 numbers [x1, x2, x3, x4]    : ")      # get string
            x1, x2, x3, x4 = nums.split(",")                            # split into 4 (unpack the list in statement)
            average =  average_nums( int(x1), int(x2), int(x3), int(x4) )   # pass to our function
            print(f'Average is {average:4.2f}')                         # print result
        elif choice==5:
            nums = input("Input 5 numbers [x1, x2, x3, x4, x5] : ")     # get string
            x1, x2, x3, x4, x5 = nums.split(",")                        # split into 5 (pack the list in statement)
            average =  average_nums( int(x1), int(x2), int(x3), int(x4), int(x5) )  # pass to our function
            print(f'Average is {average:4.2f}')                         # print result
        yn = input("Try again? ").upper()

# Task 2
# Write functions for task2 here -- outside your task2() function.

# This function is provided for you.
def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-"*31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}")
    print() # <- an extra empty print to make it look nice

# the function we need to write
def build_stock_dict(long_string):              # define function
    tokens = long_string.split()                # split the string into "tokens"
    new_dict = {}                               # create empty dict
    for token in tokens:                        # for each token
        name, price, symbol = token.split(":")  # split it into name, price, symbol. Split char is ":"
        new_dict[symbol] = [name, float(price)] # create dict item key=symbol, value=[name,float(price)]
    return new_dict                             # return dict

def task2():
    # this code provided
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)
    # Your task -- write build_sock_dict
    stock_dict2 = build_stock_dict(stock_list_string)
    print_stock_dict(stock_dict2)

# Task 3 functions.
# Write your task 3 functions here outside task3()
def create_rand_list():
    list_size = random.randint(5,15)        # random list size
    min_value = random.randint(5,10)        # random min value
    max_value = random.randint(20,50)       # random max value
    new_list = []                           # create empty list
    for i in range(list_size):              # loop through the list
        new_list.append( random.randint(min_value, max_value) )

    return new_list

def delete_list_item(the_list, item):           
    if item in the_list:                   # first check if it is in the list
        index = the_list.index(item)       # if so, find using .index()
        del the_list[index]                # delete it
        return index                       # return pos
    else:
        return -1                          # otherwise return -1

def print_list(the_list):                  
    print("--list--")
    if len(the_list)==0:                   # if empty
        print("(empty)")
    else:
        for i in the_list:                # otherwise loop through items
            print(f"({i})->", end="")     # print formatted as requested
        print("(end)")                    # add the (end)

def task3():
    my_list = create_rand_list()          # create list
    yn="Y"
    while yn=="Y":                        # loop until N
        print_list(my_list)                        # print
        item = int(input("Item to delete: "))      # get item
        result = delete_list_item(my_list, item)   # delete item, get index
        if result>=0:                              # if index is positive
            print(f"Item {item} successfully deleted at position {result}.")
        else:
            print(f"Item {item} could not be deleted.")
        yn=input("Delete item [Y/N]? ").upper()

# Task 4
# Write functions for task4 here.  Write them outside your task4() function.
def print_image(image):                # print image
    for line in image:                 # loop through list
        print(line)                    # print the string

def uncompress_rle_image(rle_image):   # decompress
    image = []                         # create empty imgae
    for line in rle_image:             # for each list in list
        new_line = ""                  # create empty string
        for tokens in line:            # for each tuple
            new_line = new_line + tokens[0] * tokens[1]  # add repeated items to string
        image.append(new_line)         # after adding all items, append this string to image
    return image

def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')], [(9, ' '), (3, '8'), (1, 'l')],
     [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
     [(6, ' '), (1, '.'), (8, '8'), (1, '.')], [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
     [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')], [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
     [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
     [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'), (1, "'")],
     [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'), (1, '-'),
      (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')], [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')], [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'), (3, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'), (7, '.'), (7, ' '), (3, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'), (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'), (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'), (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')], [(52, '.')]]
    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    print_image(image1)
    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)
    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)

def main():
    task0()
    print("\n--- Task 1: Average numbers ---")
    task1()
    print("\n--- Task 2: Text to dictionary---")
    task2()
    print("\n--- Task 3: Deleting from list---")
    task3()
    print("\n--- Task 4: RLE decoding  ---")
    task4()

    input("Press enter to end lab 6.")

if __name__ == '__main__':
    main()