###########################################
# EECS1015 - Practice Final Exam
# Fall 2022, York University
# Starting code
#
###########################################
from multiprocessing.sharedctypes import Value
import random
from re import S
from this import s
from unittest import result

def student_info():
    print("Name: Huanrui Cao")
    print("Student ID: 219256809")
    print("Email: saikoro@my.yorku.ca")
    print("Section: A")
    print("Lab: ")

def task0():
    student_info()

def task1():
    try_again = "Y"
    while try_again == "Y": 
        input_str = input("Type in a long sentence: ")
        remove_str = input("Remove words containing: ")
        input_list = input_str.strip().split()
        with_str = ""
        without_str = ""
        for token in input_list:
            if remove_str in token:
                with_str += token
                with_str += ' '
            else:
                without_str += token
                without_str += ' '
        print(f"With substring: '{with_str.strip()}'")
        print(f"W/O substring: '{without_str.strip()}'")
        try_again = input("Try again? [Y/N] ").upper()

    

# write randomlist and reshape for task2 below
def randomlist(N):
    random_list = []
    for i in range(N):
        random_list.append(random.randint(0,9))
    return random_list

def reshape(a_list, num_rows, num_cols):
    new_list = []
    for i in range(num_rows):
        row_list = a_list[i*num_cols:(i+1)*num_cols]
        new_list.append(row_list)
    return new_list

def task2():
    yn = "Y"
    while yn.upper() == "Y":
        N = int(input("List length: "))
        rand_list = randomlist(N)
        print(rand_list)
        num_rows = int(input("Rows: "))
        num_cols = int(input("Cols: "))
        while num_cols*num_rows != N:
            print(f"Error: {num_rows}*{num_cols} != {N}")
            num_rows = int(input("Rows: "))
            num_cols = int(input("Cols: "))
        print("Reshaped List")
        print(reshape(rand_list, num_rows, num_cols))
        yn = input("Try again? [Y/N] ")


# write function find_duplicates() for task 3 below
def find_duplicates(a_dict):
    d_dict = {}
    for key, value in a_dict.items():
        if  value not in d_dict:
            d_dict[value] = [key]
        else:
            d_dict[value].append(key)
    
    result_d = {}
    for key, values in d_dict.items():
         if len(values)>1:
            result_d[key] = values

    return result_d
            

def task3():
    yn = "Y"
    while yn.upper() == "Y":
        print("Input words, press enter to end.")
        input_count = 0
        input_word = "input_word"
        input_dict = {}
        while input_word != "":
            input_count += 1
            input_word = input(f"[Input {input_count:2d}] Word: ")
            if input_word != "":
                input_dict[input_count] = input_word
        print(f"Dictonary\n {input_dict}\nDupicates")
        print(find_duplicates(input_dict))
        yn = input("Try again? ")




# write class rangeChecker for task4 below
class rangeChecker:
    range_counter = 1

    def __init__(self, name, min ,max):
        assert float(max) > float(min), "max should larger than min!"
        self.id = rangeChecker.range_counter
        rangeChecker.range_counter += 1
        self.name = name
        self.min_value = float(min)
        self.max_value = float(max)

    def within_range(self, number):
        if self.min_value < number < self.max_value:
            return True
        else:
            return False

    def outside_range(self, number):
        if number < self.min_value or number > self.max_value:
            return True
        else:
            return False
    
    def print(self):
        print(f"rangeChecker  [{self.id:2d}] '{self.name:10s}' - {self.min_value:8.2f} <= num <= {self.max_value:8.2f}")



def task4():
    yn = "Y"
    while yn.upper() == "Y":
        rc = []
        for i in range(3):
            input_list = input(f"Range {i} Name, Min, Max: ").split(",")
            rc.append(rangeChecker(input_list[0], input_list[1], input_list[2]))
        num_list = input("Input list of numbers x1,x2,...xn: ").split(",")
        for item in rc:
            item.print()
            for num in num_list:
                numf = float(num)
                print(f"Inside range [{numf:8.2f}]: {item.within_range(numf)}")  
        for item in rc:
            item.print()
            for num in num_list:
                numf = float(num)
                print(f"Outside range [{numf:8.2f}]: {item.outside_range(numf)}")
        yn = input("Try again? ")

    
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