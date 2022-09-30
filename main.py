########################################
# EECS1015- Fall 2022
# Lab 1
#
# Your name: Huanrui Cao
# Your section: A
# Your student ID: 219256809
# Your email contact: saikoro@my.yorku.ca
#######################################

# Please fill out your info for each lab 
print("---- Lab 1 ----")
print("Name: Huanrui Cao")
print("Section A")
print("Student id: 219256809 ")
print("Email: saikoro@my.yorku.ca")

# Task 1
print('\n---- Task 1: Currency converter ----')
cdollar = float(input("Amount in Canadian dollars:"))
print("Amount in other currencies:")
print("USD: "+ str(cdollar*0.76))
print("EUR: "+ str(cdollar*0.75))
print("NGN: "+ str(cdollar*322.24))
print("CNY: "+ str(cdollar*5.25))
print("INR: "+ str(cdollar*97.14))

# Task 2
print('\n---- Task 2: String math ----')
print("Enter three strings: ")
str1 = input("str1: ")
str2 = input("str2: ")
str3 = input("str3: ")
print("String concatenation: ")
print("str1 + str2 + str3 = "+ str1 + str2 + str3)
print("str3 + str2 + str1 = "+ str3 + str2 + str1)
print("str2 + str1 + str3 = "+ str2 + str1 + str3)
num = int(input("Input an integer: "))
print("String multiply: ")
print("num x str1 = "+ num * str1)
print("num x str2+str3 = " + num * (str2 + str3))

# Task 3
print("\n---- Task 3: Math operators ----")
x = int(input("Input integer x: "))
y = int(input("Input integer y: "))
print("Integer math:")
print("x / y = "+ str(x/y))
print("x// y = "+ str(x//y))
print("x % y = "+ str(x%y))
print("x**y = " + str(x**y))
x = float(input("Input float x: "))
y = float(input("Input float y: "))
print("Integer math:")
print("x / y = "+ str(x/y))
print("x// y = "+ str(x//y))
print("x % y = "+ str(x%y))
print("x**y = " + str(x**y))

# Task 4
print('\n---- Task 4: Simple cylinder computation ----')
pi=355/113
r=float(input("Radius: "))
h=float(input("Height: "))
print("Cylinder surface area: "+ str(2*pi*r*h+2*pi*r**2))
print("Cylinder volume: " + str(pi*r**2*h))

## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\n---- FINISHED ----")
input("Press enter to end.")