####################
# Lab 4 model solution
# (c) Michael S. Brown, York University
# This code cannot be distrubted without permission from the author.
#
####################

# Put your imports and global variables at the top of your code
import random
import time
num_of_jumps = None          # used for task 3 and 4. Initialize to None 

def print_student_info():
    print("Name: Mr. White")
    print("Section A")
    print("Student id: 10000001")
    print("Email: heisenberg@bb.ca")

# simple function to get Yes/No input (returns a boolean)
def get_yes(prompt):
    yn = "q"                        # keep looping until we get an Y or N
    while yn!="Y" and yn!="N":      # you need an "and" condition, not an "or" here
        yn = input(prompt).upper()
    if yn != 'Y':                  # if not "Y", then False
        return False
    else:
        return True                # else True

# gets a float within range
def get_float_input(prompt, min_value, max_value):
    x = min_value - 1    # set initial input to be out of range (you could also do max_value+1)
    while x < min_value or x > max_value: # keep getting input until in range. Here you need an or
        x = float(input(prompt)) # get input
    return x                     # return input

# same as above, but we convert the input to an int() not float()
def get_int_input(prompt, min_value, max_value):
    x = min_value - 1
    while x < min_value or x > max_value:
        x = int(input(prompt))
    return x

# draw an owl
# read lab carefully, this should draw a single owl that is offset
# position. If randomize is True, we randomly select which eye variable to draw.
def draw_owl(offset, randomize=False):
    eye1 = '{o,o}'
    eye2 = '{-,o}'
    eye3 = '{o,-}'
    body = '/)_) '
    feet = ' " " '

    pad = offset * " "   # compute padding (i.e., empty white spaces before the owl)
    if randomize:        # if randomize is True --since this is a boolean, we can just use the variable itself as the condition
        s = random.randint(1,3)   # get a number between 1-3
        if s==1:
            print(pad + eye1)     # draw eye1
        elif s==2:
            print(pad + eye2)     # draw eye2
        else:
            print(pad + eye3)     # draw eye3
    else:
        print(pad + eye1)         # otherwise, draw eye1

    # Print body and then feet
    print(pad + body)
    print(pad + feet)

# computs the return based on formula
def compute_return(amount, rate, years): 
    for i in range(0,years):             # loop years times
        amount = amount + amount*rate    # compute formula 
                                         # I put line breaks between condition statements, but it isn't required.
    return amount                        # return amount. 

def task1():
    N = get_int_input("How many times to move [2-20]? ", 2, 20)   # get N
    T = get_int_input("How long to delay [1-1000ms]? ", 1, 1000)  # get T(ime) of delay
    rand = get_yes("Randomize [Y/N]? ")                           # random?
    for i in range(0, N):                                         # loop N times
        draw_owl(i,rand)                                          # call draw_owl with i, rand
        time.sleep(T/1000)                                        # sleep based on delay
 
def task2():                                        
    keep_going = True                                             # repeat tasks?
    while keep_going:
        amount = get_float_input("Input initial investment amount [1, 10000]? ", 1, 10000)  # get amount
        rate = get_float_input("Annual return rate [0-1]? ", 0, 1) # get rate
        years = get_int_input("How many years [1-10]? ", 1, 10)    # get years -- see how useful the "get" functions are!
        final = compute_return(amount, rate, years)                 # compute return
        if years>1:                                                 # check # of yeras
            print(f"Return in {years} years is: ${final:10.2f}")
        else:
            print(f"Return in {years} year is: ${final:10.2f}")

        keep_going = get_yes("Compute new investment [Y/N]? ")      # see how useful get function is! 

def task3():
    global num_of_jumps                                          # get global variable
    max = 1                                                     # set initial max
    for i in range(1,5):                                        # <- my mistake, should be 1,6
        prompt = f"{i:2}/5   Enter a number [1-100]: "
        num = get_int_input(prompt, 1, 100)                     # get input
        if num % 2 == 1 and num > max:                          # if odd and > than max
            max = num
    print(f"Final max odd number: {max}.")                      # print max
    num_of_jumps = max                                          # set global to max

def task4():                                                    # access global
    global num_of_jumps
    f1 = "  o   [%3d]\n /|\  \n | |  "       # modify string with % format approach
    f2 = " \o/  [%3d]\n  |   \n / \  "       # modify string with % format approach

    input(f"Press enter to perform {num_of_jumps} jumping jacks.")
    step = 1
    for i in range(1, num_of_jumps+1):
        if i % 2 == 0:                      # alternate even odd
            print(f1 % i)                   # print with i for formating
        else:
            print(f2 % i)                   # print with i for formatting
        time.sleep(0.3)

# notice I didn't modify anything in main.
def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")

if __name__ == "__main__":
    main()