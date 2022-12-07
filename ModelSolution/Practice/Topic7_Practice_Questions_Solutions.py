############################
# EECS1015, York University
# Practice questions #7
# Nested collections
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission from the author.
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################
from random import randint

def keyFunc1(item):
    return item[0]

def keyFunc2(item):
    return item[1]

print("\n---Q1---")
alist = [['C', 16], ['J', 25], ['A', 26], ['L', 6], ['X', 10], ['Z', 2], ['U', 20], ['B', 3], ['F', 8], ['O', 15], ['E', 9], ['I', 23], ['S', 4], ['N', 0], ['W', 11], ['D', 14], ['M', 21], ['T', 19], ['R', 22], ['K', 24], ['H', 18], ['Q', 12], ['V', 13], ['G', 17], ['Y', 7], ['[', 1], ['P', 5]]
print(alist)
print("Sort by first number")
alist.sort(key=keyFunc1)
print(alist)
print("Sory by 2nd number")
alist.sort(key=keyFunc2)
print(alist)

def combine_lists(a_list, b_list):
    new_list = []
    assert len(a_list) == len(b_list), "Lists must be the same length!"
    for i in range(len(a_list)):
        new_list.append( [a_list[i], b_list[i]] )

    return new_list

print("\n---Q2---")
x = ["A", "B", "C", "D", "E", "F"]
y = [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ]
x_y = combine_lists(x,y)
print(x)
print(y)
print(x_y)

def print_min_max_score(student_dict):
    overall_min = 100
    student_min = ""
    overall_max = 0
    student_max = ""
    for name, grades in student_dict.items():
        max_mark = max(grades)
        if max_mark > overall_max:
            overall_max = max_mark
            student_max = name
        min_mark = min(grades)
        if min_mark < overall_min:
            overall_min = min_mark
            student_min = name
    print(f"Overall highest by {student_max:8s} ({overall_max:3d})")
    print(f"Overall lowest  by {student_min:8s} ({overall_min:3d})")


print("\n---Q3---")
students = {'Jawahar': [68, 90, 84, 30, 81], 'Mahmoud': [66, 14, 95, 84, 89], 'Anna': [100, 90, 72, 80, 65], 'Nick': [45, 83, 89, 72, 87], 'Jia': [77, 55, 84, 96, 98]}
print_min_max_score(students)


def get_min_max_score(student_dict):
    overall_min = 100
    student_min = ""
    overall_max = 0
    student_max = ""
    for name, grades in student_dict.items():
        max_mark = max(grades)
        if max_mark > overall_max:
            overall_max = max_mark
            student_max = name
        min_mark = min(grades)
        if min_mark < overall_min:
            overall_min = min_mark
            student_min = name
    result_dict = {}
    result_dict["min"] = [student_min, overall_min]
    result_dict["max"] = [student_max, overall_max]
    return result_dict

print("\n---Q4---")
min_max = get_min_max_score(students)
print(min_max)

def make_3d_list():
    list3d = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    counter = 1
    for depth in range(3):
        for row in range(3):
            for col in range(3):
                list3d[row][col][depth]=counter
                counter += 1
    return list3d

def print_3d_list(list3d):
    for depth in range(3):
        print(f"Plane Z={depth}")
        print("  Y")
        print("X|--------")
        for row in range(3):
            x1 = list3d[row][0][depth]
            x2 = list3d[row][1][depth]
            x3 = list3d[row][2][depth]
            print(f" |{x1:2d} {x2:2d} {x3:2d}")

print("\n---Q5---")
list3d = make_3d_list()
print(list3d)
print_3d_list(list3d)