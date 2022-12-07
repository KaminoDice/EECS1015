###########################################
# EECS1015 - Practice Final Exam
#
# (c) Michael S. Brown -- This file cannot be
# shared or reused without permission.
#
###########################################
import random

def student_info():
    print("Name: ")
    print("Student ID: ")
    print("Email: ")
    print("Section: ")
    print("Lab: ")

def task0():
    student_info()

def task1():
    YN = "Y"
    while YN=="Y":
        word_input = input("Type in a long sentence: ")
        words = word_input.split()                          # split input
        substring = input("Remove words containing: ")
        with_words = []                                     # create two empty lists
        wo_words = []
        for word in words:
            if substring in word:                          # if with words
                with_words.append(word)
            else:                                          # if not with words
                wo_words.append(word)

        with_string = " ".join(with_words)                 # join and print
        wo_string   = " ".join(wo_words)
        print(f"With substring: '{with_string}'")
        print(f"W/O  substring: '{wo_string}'")
        YN = input("Try again? [Y/N] ").upper()

# Task 2 - reshape code
def reshape(my_list, row, col):                             
    rList = []                   # create empty main rList
    index = 0                    # create an index to walk thorugh the list
    for i in range(row):         # for each row
        row_list = []            # create an empty list
        for j in range(col):     # for each col
            row_list.append(my_list[index])     # add item at [index] into row list
            index+=1                            # increment index
        rList.append(row_list)                  # add row list to out main rList
    return rList                                # return our list

# code provided for you
def randomlist(N):
    rlist = []
    for i in range(N):
        rlist.append(random.randint(0,9))
    return rlist

def task2():
    YN = "Y"
    while YN=="Y":
        N = int(input("List length: "))
        rlist = randomlist(N)               # create random list
        print(rlist)                        # print the list
        rows=0                              # set up rows/cols variables
        cols=0
        while rows*cols!=N:                 # loop while row*col not N
            rows = int(input("Rows: "))     # get input
            cols = int(input("Cols: "))
            if rows*cols != N:              # if not correct print error
                print(f"Error: {rows}*{cols} != {N}")

        new_2D = reshape(rlist, rows, cols)  # call reshape (it returns a list)
        print("Reshaped List")
        print(new_2D)                        # print the list
        YN = input("Try again? [Y/N] ").upper()

# Task 3 

def find_duplicates(my_dict):
    new_dict = {}                       # create empty dictionary
    for values in my_dict.values():     # get values from my_dict (values=words)
        new_dict[values] = []           # create empty list for each word
    for key, value in my_dict.items():  # loop through line # (key) and words)
        new_dict[value].append(key)     # append line number to word dictionary
    for key in list(new_dict.keys()):   # loop through keys (keys has been turned into a list)
        if len(new_dict[key]) == 1:     # len of the list for the word is 1 
            del new_dict[key]           # delete it
    # alternative strategy -- make a new list that skips any list with only 1 item 
    # final_dict = {}
    # for key, value in new_dict.items():
    #     if len(new_dict[key]) > 1:
    #          final_dict[key] = value
    # return final_dict
    return new_dict                     # return new dictionary

def task3():
    my_dict = {}
    word= " "
    count = 0
    YN = "Y"
    while YN=="Y":
        my_dict = {}      # create empy dictionary
        word = " "        # starting variable for loop
        count = 1         # set cound to 1
        print("Input words, press enter to end.")
        while word != "":    # while word not empty
            word = input(f"[Input {count:2d}] Word: ") # get word      
            if word != "":                             # if not empty
                my_dict[count] = word                  # add to dictionary
                count = count + 1                      # increment counter
        print("Dictionary")                            
        print(my_dict)                   # print dictionary
        duplicates = find_duplicates(my_dict)       # find duplicates
        print("Duplicates")              
        print(duplicates)                # print duplicates
        YN = input("Try again? ").upper()

# class definition
class rangeChecker:
    range_counter = 1                            # class variable

    def __init__(self, name="", min=0, max=10):  # initializer
        self.id = rangeChecker.range_counter     # set id to range_counter
        rangeChecker.range_counter += 1          # increment range_counter
        self.name = name
        assert max>min, f"Max ({max}) must be greater than min ({min})" # assert
        self.min = float(min)                    # set min/max (convert to float)
        self.max = float(max)

    def within_range(self, number):             # check within range
        if self.min <= number <= self.max:      # yes, you can do this in python
            return True                         # if in range return True
        else:
            return False                        # else False

    def outside_range(self, number):            # check outside range
        if number > self.max or number < self.min:    # use or
            return True                               # outside range
        else:
            return False                              # inside

    def print(self):                                # print range checker
        print(f"rangeChecker [{self.id:2d}]  '{self.name:10s}'  - {self.min:8.2f} <= num <= {self.max:8.2f}")


def task4():
    YN = "Y"
    while YN=="Y":
        object_list = []            # create empty object list 
        for i in range(3):          # loop 3 times
            name, min, max = input(f'Range {i} Name, Min, Max: ').split(",")
            range_obj = rangeChecker(name, float(min), float(max) )
            object_list.append( range_obj ) # add object to the list
        num_list = input(f'Input list of numbers x1,x2,..,xn: ').split(",")
        # now, loop through the objects
        for checker in object_list:
            checker.print()   # print the object
            for num in num_list:   # loop through the numbers
                # check inside
                print(f"Inside range [{float(num):8.2f}]: " + str( checker.within_range(float(num))))
        for checker in object_list:  # loop thru objects agian
            checker.print()          # print the object info
            for num in num_list:      # loop through numbers
                # check outisde
                print(f"Outside range [{float(num):8.2f}]: " + str(checker.outside_range(float(num))))
        YN = input("Try again? ").upper()

def main():
    task0()
    print("--- Task 1 ---")
    task1()
    print("\n--- Task 2 ---")
    task2()
    print("\n--- Task 3 ---")
    task3()
    print("\n--- Task 4 ---")
    task4()

if __name__ == "__main__":
    main()