#####################################################################################
# EECS1015 - Lab 2 - Sample Solution
# York University
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission of the author.
# (e.g., you can't upload this to illegal dissemination sites such as course hero)
#
# This task provides an example solution.
#####################################################################################

print("\---- Lab 2 ----")
print("Name: Michael S. Brown")
print("Section A")
print("Student id: 9999999")
print("Email: elonmusk@aol.com")

# Task 1
print("\n---- Task 1: Three year investment return ----")
name = input("Name: ")                              # get input from user
name = name.strip()                                 # strip white spaces
name = name.title()                                 # convert to title (first letter of each work capital)
amount = float(input("Initial amount: $ "))         # Input initial amount
rate   = float(input("Rate of return: % "))/100     # Input rate of return
print(f"Client: {name}  Yearly rate of return multiplier: {rate:.2f}")
new_amount = amount + rate*amount
print("Year 1\tStarting Amount: ${:8.2f}\t\tEnding Amount: ${:8.2f}".format(amount, new_amount))
amount = new_amount
new_amount = amount + rate*amount
print("Year 2\tStarting Amount: ${:8.2f}\t\tEnding Amount: ${:8.2f}".format(amount, new_amount))
amount = new_amount
new_amount = amount + rate*amount
print("Year 3\tStarting Amount: ${:8.2f}\t\tEnding Amount: ${:8.2f}".format(amount, new_amount))



# Task 2
print("\n----Task 2 Leetspeak converter ----")
string = input("Type a long string: ").upper().strip()  # input from user -- first convert to upper, then strip whitespaces
string = string.replace("T", "7")                       # apply replace for T to 7
string = string.replace("A", "^")                       # apply replace for A to ^
string = string.replace("E", "3")                       # apply replace for E to 3
string = string.replace("I", "!")                       # apply replace for I to !
string = string.replace("B", "8")                       # apply replace for B to 8
string = string.replace("O", ".")                       # apply replace for O to .
string = string.replace("C", "<")                       # apply replace for C to <
string = string.replace("S", "$")                       # apply replace for S to $
print(string)                                           # print the final string


# task 3
print("\n---- Task 3: Substring highlighter ----")
print("Type a sentence at the prompt below: ")
mystr = input("> ")
mystr_len = len(mystr)
print("Enter substring below to highlight: ")
substr = input("> ")
substr_len = len(substr)
pos = mystr.find(substr)
print("Sentence has {} characters, substring has {} characters".format(mystr_len,substr_len))
new_string = mystr[:pos] + "*" + substr.upper() + "*" + mystr[pos+substr_len:]
print("Substring highlighted:")
print("> %s" % new_string)


# task 4
print("\n---- Task 4: Exponent ----")
str = input("Input exponent in the form x^y: ")   # input string
number1 = int(str[0])                  # get first character
number2 = int(str[-1])                 # get last character
print("Extracted numbers {} {}".format(number1,number2))  # print extract numbers
result = number1 ** number2                   # multiple numbers
print("{}^{} = {}".format(number1, number2, result))   # print as formatted text


# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")