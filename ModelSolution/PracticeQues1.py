############################
# EECS1015, York University
# Practice questions #1
# -> Variables, expressions, print, input/output
# Author: Michael S. Brown
#
# This code cannot be distributed without written permission 
# (e.g., please do not uploaded this to coursehero)
#
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################



# Question 1
num_str = input("Input number? ")
num1 = int(num_str)
num1 += 5
print(num1)
num_str = input("Input another number? ")
num2 = int(num_str)
print(num1+num2)

# Question 2
print("\nQ2.")
print("Retry Q1 with leading spaces.  It will still work.")

# Question 3
print("\nQ3.")
x = int(input("x: "))
y = (x-2)**2 + 1/(4*x+2)
print(y)

# Question 4
print("\nQ4.")
a_string = input("Input string: ")
print(a_string*10)


# Question 5
print("\nQ5.3")
a=input("input a: ")
b=input("input b: ")
temp=a                  # remember, to swap variables you need a temp value to hold data bound to 'a'
a=b
b=temp
print(a)
print(b)


# Question 6
print("\nQ6.")
print(int(input("a="))*5)
#         ^^^^^^^^^^       <- (1) input()
#     ^^^                  <- (2) int()
#                     ^^   <- (3) * 5
#^^^                       <- (4) print()

# Question 7
print("\nQ7.")
x = input("x= ")
print("your number is ", end="")
print(x)

# Question 8
print("\nQ8.")
h  = float(input("height (in cm): "))
kg = float(input("weight (in kg): "))
print('BMI = ', end="")
print( kg / ((h/100)**2) ) # why the /100?  Input is in cm, but formula is in meters.  100cm = 1m

# Question 9
print("\nQ9.")
var1 = "None"
var2 = None
print(var1*5)
# print(var2*5)  <- commented out

# Question 10
print("\nQ10.")
kg = float(input("weight (in kg): "))
print('Stones = ', end="")
print( kg / 6.35029318  ) # 1 stone = 6.35029318 kg


input("\nPress enter to end.")
