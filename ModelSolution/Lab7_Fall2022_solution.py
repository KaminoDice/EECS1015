#############################
# EECS1015, York University
# Lab 7 Model Solution
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be shared without written
# permission from the author.
#
#############################

def merge_lists(list1, list2):
    new_list = []               # create new empty list
    len1 = len(list1)               # get size of list 1
    len2 = len(list2)               # get size of list 2
    index1 = 0                  # set index1 and index2
    index2 = 0
    assert is_sorted(list1), "List 1 is not sorted!"   # assert if not sorted
    assert is_sorted(list2), "List 2 is not sorted!"   # assert if not sorted
    while index1 < len1 and index2 < len2:  # while condition
        if list1[index1] <= list2[index2]:  # is list1 item <= list2 item
            new_list.append(list1[index1])  # add list1 item to new list
            index1+=1               # update list1 index
        else:                   # otherwise
            new_list.append(list2[index2])  # add list2 item to new list
            index2+=1               # update list2 index

    if index1 < len1:               # what if items left in list1
        new_list.extend(list1[index1:]) # add them to new list
    if index2 < len2:               # what if items left in list2
        new_list.extend(list2[index2:]) # add them to new list

    return new_list             # return new list


# return true if a list is sorted or not
def is_sorted(alist):
    sorted=True
    for i in range(1,len(alist)): # loop from 1 to end
        if alist[i-1] > alist[i]: # if previous element is larger than current, not sorted
            sorted=False
    return sorted

# Merge dictionary 2 into dictionary 1
# If key from dict2 already exists in dict1 leave it unchanged
# dict1 will be updated
def merge_dict(dict1, dict2):
    for key in dict2:
        if key in dict1:
            continue
        else:
            dict1[key] = dict2[key]

def invert_dict(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[value] = key
    return new_dict

def list_to_dict(a_list):
    new_dict = {}
    for i in range(len(a_list)):
        new_dict[i] = a_list[i]
    return new_dict


def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    print(is_sorted(x1))
    print(is_sorted(x2))
    print(is_sorted(x3))

def task2():
    dict1 = {8:"Exercise", 9:"Breakfast", 12:"Lunch", 3:"Study", 6:"Netflix"}
    dict2 = {8:"Sleep", 10:"Lab", 12:"Class", 4:"Call Mom"}
    print(dict1)
    print(dict2)
    merge_dict(dict1,dict2)
    print(dict1)

def task3():
    dict1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
    print(dict1)
    dict2=invert_dict(dict1)
    print(dict2)

def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1:"1", 2:"2"}]
    print(my_list)
    my_dict = list_to_dict(my_list)
    print(my_dict)

def strlist_to_numlist(str_list):
    for i in range(len(str_list)):
        str_list[i] = int(str_list[i])

def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(x)
    strlist_to_numlist(x)
    print(x)

def task6():
    YN = "Y"
    while YN=="Y":
        astr = input("Input 1st sorted list of numbers [x1 x2 ...]: ")
        list1 = astr.split()
        strlist_to_numlist(list1)
        astr = input("Input 2nd sorted list of numbers [y1 y2 ...]: ")
        list2 = astr.split()
        strlist_to_numlist(list2)
        list3 = merge_lists(list1, list2)
        print("Merged lists")
        print(list3)

        YN = input("Try again [Y/N]? ").upper().strip()

def print_student_info():
    print("Name: Elongated Muskrat")
    print("Student ID: 207000000")
    print("Section A or B")
    print("Email: elonmusk@studiedcanada.net")


def task0():
    print_student_info()

def main():
    task0()
    print("\n---- Task 1: Check if list is sorted ----")
    task1()
    print("\n---- Task 2: Merge dictionaries ----")
    task2()
    print("\n---- Task 3: Invert dictionaries ----")
    task3()
    print("\n---- Task 4: List to dictionary ----")
    task4()
    print("\n---- Task 5: String list to num list ----")
    task5()
    print("\n---- Task 6: Merge list with assert ----")
    task6()
    input("\n Press enter to end lab 7.")

if __name__ == "__main__":
    main()