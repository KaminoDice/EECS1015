############################
# EECS1015, York University
# Practice questions #6
# Nested collections
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission from the author.
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################

import random

list_3d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("--Q1--")
for i in range(0,3):
    row = list_3d[i]
    a, b, c = row
    print(f"[{i}][0]='{a}' [{i}][1]='{b}'  [{i}][2]='{c}'")

## Q1
print("--Q2--")
print(list_3d)
print("Printing row by row")
for rows in list_3d:
    for col in rows:
        print(col)



print("--Q3--")
print("printing column by column")
for col in range(0,3):
    for row in range(0,3):
        print(list_3d[row][col])


print("---Q4---")
def int_list(str_list):
    new_list = []
    for i in str_list:
        new_list.append( int(i) )
    return new_list

def input_ragged_list():
    new_list = []
    for i in range(1,5):
        in_str = input(f"[{i}/4] Input numbers [ex. 1, 5, 4, ..]: ")
        str_list = in_str.split(",")
        num_list = int_list(str_list)
        new_list.append(num_list)
    return new_list

def print_ragged_list(a_list):
    i = 0
    for lists in a_list:
        print(f"List[{i}] -> [", end="")
        for items in lists:
            print(f"({items}) ", end="")
        print("]")
        i = i + 1

yn="Y"
while yn=="Y":
    print("Input 4 lists")
    ragged_list = input_ragged_list()
    print("Printing the ragged list")
    print_ragged_list(ragged_list) 
    yn=input("Input a new ragged list (Y/N)? ").upper()


print("---Q5---")
card_dict = {}
for card in range(2,11):
    card_dict[str(card)] = card
card_dict.update({"J":11, "Q":12, "K":13, "A":14})
print(card_dict)

print("---Q6---")
for card, value in card_dict.items():
    print(f"[{card:2s}] value={value}")

print("---Q7---")
def print_image(image):
    print("  0 1 2 3 4 5 6 7 8 9")
    for row in range(10):
        print(f"{row} ", end="")
        for col in range(10):
            print(image[row][col],end=" ")
        print()

def create_empty_image():
    image = []
    for x in range(10):
        image.append(list())   # This adds a new empty list to the end of the image list
        for y in range(10):
            image[x].append(".")
    return image

def add_noise(image):
    s = set()
    while len(s) < 15:
        x = random.randint(0,9)
        y = random.randint(0,9)
        image[x][y] = "*"
        s.add((x,y))

    return


i = create_empty_image()
print(i)
add_noise(i)
print(i)
print_image(i)



print("---Q8---")
dict_drinks = {"W":"Water", "T":"Tea", "R":"Red Bull", "C":"Coffee", "Name":"Drink items"}
dict_food   = {"F":"Falafel", "D":"Dosa", "P":"Pizza", "R":"Rice", "Name":"Food items"}
menu_dict = {"D":dict_drinks, "F":dict_food}
print(menu_dict)

yn = "Y"
while yn=="Y":
    print("Selection")
    selection = menu_dict.keys()
    while True:
        for symbol, dict_value in menu_dict.items():
                print(f"'{symbol}' {dict_value['Name']}")
        s = input("Selection: ").upper()
        if s in selection:
            break
        else:
            continue
    print(menu_dict[s]["Name"])  # <- get the dictionary for "s", the get value for key "Name"
    selection = menu_dict[s].keys()
    while True:
        for key, value in menu_dict[s].items():
            if key!="Name":
                print(f"'{key}' {value}")
        new_s = input("Selection: ").upper()
        if new_s in selection:
            break
        else:
            continue
    print(f"Your selection: {menu_dict[s][new_s]}")
    yn=input("Browse Menu (Y/N)? ").upper()

