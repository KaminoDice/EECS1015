############################
# EECS1015, York University
# Practice questions #5
# Lists, dictionaries, tuples, and sets
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission from the author.
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################
import random

def stringToCharList(astring):
    char_list = []
    for i in astring:
        char_list.append(i)

    # note a faster way?  char_list = list(astring)
    return char_list

def charstoWords(char_list):
    chartowords = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "-":"dash"}
    word_list = []
    for char in char_list:
        word_list.append( chartowords[char] ) # <- look up associated word

    return word_list

def q8():
    print("\n--- Q8 ----")
    phone_number = input("Input phone number XXX-XXX-XXXX: ")
    char_list = stringToCharList(phone_number)
    word_list = charstoWords(char_list)
    print(char_list)
    print(word_list)
    print("->".join(word_list))

def reverse_collection(a_collection, return_type="L"):
    new_list = []
    for i in a_collection:
        new_list.insert(0,i) # <- always insert at the beginning -- this will reverse the list
    if return_type=='T' or return_type=='t':
        new_list = tuple(new_list)

    return new_list

def q7():
    print("\n--- Q7 ----")
    x = (1,2,3,4,5,6,7,8,9,10)
    y = reverse_collection(x, "L")
    print("Input   ", x)
    print("Reserved", y)
    x = ['A', 'B', 'C', 'D', 'E']
    y = reverse_collection(x, "T")
    print("Input   ", x)
    print("Reserved", y)


def invert_dictionary(a_dict):
    new_dict = {}
    for key, value in a_dict.items():
        new_dict[value] = key
    return new_dict

def q6():
    print("\n--- Q6 ----")
    my_dict = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
    new_dict = invert_dictionary(my_dict)
    print("Input dict", my_dict)
    print("New   dict", new_dict)
    my_dict = {'1': 'Mon', ' 2': 'Tue', ' 3': 'Wed', ' 4': 'Thu', ' 5': 'Fri', ' 6': 'Sat', ' 7': 'Sun'}
    new_dict = invert_dictionary(my_dict)
    print("Input dict", my_dict)
    print("New   dict", new_dict)


def get_unique_items(my_list):
    my_set = set(my_list)
    unique_items = list(my_set)
    return unique_items

def q5():
    print("\n--- Q5 ----")
    x = random_list(20, 0, 4)
    y = get_unique_items(x)
    print('List items  :', x)
    print('Unique items:', y)
    x = list(input("Input a string: "))
    y = get_unique_items(x)
    print('List items  :', x)
    print('Unique items:', y)

    pass

# function for q4
def random_list(N, min, max):
    my_list = []
    for i in range(0, N):
        num = random.randint(min, max)
        my_list.append(num)
    return my_list

def q4():
    print("\n--- Q4 ----")
    x = random_list(10, 0, 100)
    y = random_list(20, 0, 1)
    print(x)
    print(y)

def q3():
    print("\n--- Q3 ----")
    my_dict = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
    for values in my_dict.values():
        print(f"Value {values}")
    for key in my_dict.keys():
        print(f"Key   {key}")
    for key, value in my_dict.items():
        print(f"my_dict[{key}]='{value}'")

def q2():
    print("\n--- Q2 ----")
    print("Input key/value pairs, separated commas.")
    input_string = input("Key/values : ")
    tokens = input_string.split(",")
    my_dict = {}
    for i in tokens:
        key, value = i.split("/")
        my_dict[key.strip()] = value.strip()
    print(my_dict)


    pass

def q1():
    print("\n--- Q1 ----")
    num_input = input("Input a list of numbers [N1,N2,N3]: ")
    tokens = num_input.split(",")
    sum = 0
    for i in tokens:
        n = int(i) # <- recall split items are strings
        sum = sum + n
        print(f"{n:5d}")
    print("--------")
    print(f"{sum:5d}")

def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()

if __name__ == '__main__':
    main()