##################################
# EECS1015 - York University
# Author: Michael S. Brown 
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 7 starter code
#
##################################


from dataclasses import asdict
from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY
from tkinter import Y

x = list()
def print_student_info():
    print("Name: Cao Huanrui")
    print("Student ID: 219256809")
    print("Section A")
    print("Email: saikoro@my.yorku.ca")


def task0():
    print_student_info()


def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    print(is_sorted(x1))
    print(is_sorted(x2))
    print(is_sorted(x3))
    # Write function is_sorted() outside this function
    # apply the function on each list and print the results


def is_sorted(aList):
    listRange = len(aList)
    flag = 0
    for i in range(1, listRange):
        if aList[i] < aList[i - 1]:
            flag = 1
    if not flag:
        return True
    else:
        return False


def task2():
    dict1 = {8: "Exercise", 9: "Breakfast", 12: "Lunch", 3: "Study", 6: "Netflix"}
    dict2 = {8: "Sleep", 10: "Lab", 12: "Class", 4: "Call Mom"}
    # Write function merge_dict() outside this function
    print(dict1)  # print dict1
    print(dict2)  # print dict2
    merge_dict(dict1, dict2)  # call merge_dict(dict1, dict2)  <- which will modified dict1
    print(dict1)  # print dict1 again (after it is modified)


def merge_dict(dict1, dict2):
    for key in dict2:
        if key not in dict1:
            value = dict2.get(key)
            dict1.update({key: value})
    print("dict2 merged into dict1")


def task3():
    a_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    # write function invert_dict() outside this function
    print(a_dict)  # print a_dict
    new_dict = invert_dict(a_dict)  # call invert_dict(a_dict)
    print(new_dict)  # print new dict


def invert_dict(a_dict):
    new_dict = {}
    for key in a_dict:
        value = a_dict.get(key)
        new_dict.update({value: key})
    return new_dict


def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1: "1", 2: "2"}]
    # write function list_to_dict() outside this function
    print(my_list)  # print list
    listtodict = list_to_dict(my_list)  # call list_to_dict(my_list)
    print(listtodict)  # print new dictionary


def list_to_dict(a_list):
    aDict = {}
    len_list = len(a_list)
    for i in range(len_list):
        aDict.update({i: a_list[i]})
    return aDict


def task5():
    global x
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # write function str_list_to_num_list()
    print(x)  # print list x
    str_list_to_num_list(x)  # call function str_list_to_num_list(x)
    print(x)  # print list x again (it should be updated)


def str_list_to_num_list(str_list):


    for i in range(len(str_list)):
        str_list[i] = int(str_list[i])


def task6():
    # write code as described in the PDF
    again = 'Y'
    while again == 'Y':
        list1 = list(map(int, input("Input 1st sorted list of numbers [x1 x2 ...]: ").strip().split()))
        list2 = list(map(int, input("Input 2nd sorted list of numbers [y1 y2 ...]: ").strip().split()))
        new_list = merge_lists(list1, list2)
        print(new_list)
        again = input("Try again [Y/N]? ").upper()


def merge_lists(list1, list2):
    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    i = 0
    j = 0
    assert is_sorted(list1), "List 1 is not sorted!"
    assert is_sorted(list2), "List 2 is not sorted!"
    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    if i < len1:
        new_list.extend(list1[i:])
    if j < len2:
        new_list.extend(list2[j:])
    print("Merged list")
    return new_list


def main():
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


if __name__ == "__main__":
    main()
