#####################################################################################
# EECS1015 - Lab 1 - Sample Solution
# York University
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission of the author.
# (e.g., you can't upload this to illegal dissemination sites such as course hero)
#
# This task provides an example solution.
#####################################################################################

# Your info
print("---- Lab 1 ----")
print("Name: Michael S. Brown")
print("Section A")
print("Student id: 1999999")
print("Email: msb999@aol.com")

# Task 1
print('\n---- Task 1: Currency converter ----')
amount = float(input("Amount in Canadian dollars: "))
print("Amount in other currencies: ")
print("USD: ", end="")
print(amount*0.76)
print("EUR: ", end="")
print(amount*0.75)
print("NGN: ", end="")
print(amount*322.24)
print("CNY: ", end="")
print(amount*5.25)
print("INR: ", end="")
print(amount*97.14)

# Task 2
print('\n---- Task 2: String math ----')
print("Enter three strings: ")
str1 = input('str1: ')
str2 = input('str2: ')
str3 = input('str3: ')
print("String concatenation:")
print("str1 + str2 + str3 = ", end="")
print(str1 + str2 + str3 )
print("str3 + str2 + str1 = ", end="")
print(str3 + str2 + str1 )
print("str2 + str1 + str3 = ", end="")
print(str2 + str1 + str3 )
num = int(input("Input an integer: "))
print("String multiply:")
print("num x str1 = ", end="")
print(num * str1)
print("num x str2+str3 = ", end="")
print(num * (str2+str3))

# Task 3
print("\n---- Task 3: Math operators ----")
x = input("Input integer x: ")
y = input("Input integer y: ")
print("Integer math:")
xint = int(x)
yint = int(y)
print("x / y = ", end="")
print(xint/yint)
print("x// y = ", end="")
print(xint//yint)
print("x % y = ", end="")
print(xint%yint)
print("x** y = ", end="")
print(xint**yint)
x = input("Input float x: ")
y = input("Input float y: ")
print("Float math: ")
xfloat = float(x)
yfloat = float(y)
print("x / y = ", end="")
print(xfloat/yfloat)
print("x// y = ", end="")
print(xfloat//yfloat)
print("x % y = ", end="")
print(xfloat % yfloat)
print("x** y = ", end="")
print(xfloat**yfloat)

# Task 4
print('\n---- Task 4: Simple cylinder computation ----')
pi = 355/113
radius = float(input("Radius: "))
height = float(input("Height: "))
print("Cylinder surface area: ", end="")
surfacearea = 2*pi*radius*height+2*pi*radius**2
print(surfacearea)
print("Cylinder volume: ", end="")
volume = pi*radius**2*height
print(volume)

## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("---- FINISHED ----")
input("Press enter to end.")