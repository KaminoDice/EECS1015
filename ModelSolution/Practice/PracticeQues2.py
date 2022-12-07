############################################################################
# EECS1015, York University
# Practice questions #2
# -> Strings, formatted output
# Author: Michael S. Brown (c) 
# This code cannot be distributed without written permission 
# (e.g., please do not uploaded this to coursehero)
#
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################################################################



# Question 1
print("Q1.")
print("\\\\ \"_\" //")  ## escape character for a \ is '\\'.  Escape character of " is \"
print("The new line characters is '\\n'")

# Question 2
print("\nQ2.")
num = int(input("Enter a number: "))
result = num * 17
digits = len( str(result) )  # convert the number to a string, call len() to get the # of chars
print(f"{num}*17={result} . . it has {digits} digits.")

# Question 3
print("\nQ3.")
num = int(input("Enter a number: "))
result = num * 17
digits = len( str(result) )  # convert the number to a string, call len() to get the # of chars
print("{}*17={} . . it has {} digits.".format(num, result, digits))

# Question 4
print("\nQ4.")
a_string = input("Input a long string: ")
str_length = len(a_string)
print(f"'{a_string}' is {str_length} characters.")
start = int(input("start: "))
N = int(input("# of chars: "))
extracted = a_string[start:start+N]  # <- slice starting at start and end at start+N
print(f"extracted '{extracted}'")

# Question 5
print("\nQ5.")
a_string = input("Input a long string: ")
str_length = len(a_string)
print(f"'{a_string}' is {str_length} characters.")
start = int(input("start: "))-1   # adjust by -1, since the user is counting from 1 instead of 0.
N = int(input("# of chars: "))
extracted = a_string[start:start+N]  # <- slice starting at start and end at start+N
print(f"extracted '{extracted}'")

# Question 6
print("\nQ6.")
a_string = input("Type a sentence: ")
a_string = a_string.strip()               # remove leading/after spaces
a_string = a_string.replace(",", "")      # replace commmas with empty string
a_string = a_string.replace(".", "")      # replace period with comma
a_string = a_string.replace(" ", "*")     # replace spaces with "*"
a_string = a_string.lower()
print(f'Modified sentence: {a_string}')

# Question 7
print("\nQ7.")
a_string = input("Input a long string: ")
str_length = len(a_string)
mid = str_length // 2
mid_char = a_string[mid]
print(f"The string is {str_length} characters long. The middle character is '{mid_char}'")
front = a_string[:mid]
back = a_string[mid:]
flipped = back + "|" + front
print(f"Flipped String")
print(flipped.upper())

# Question 8
print("\nQ8.")
a_string = input("Give a string with a least two '*': ")
first_pos = a_string.find('*')
second_pos = a_string[first_pos+1:].find('*') + first_pos + 1
#           ^^^^^^^^^^^^^^^
#           splice string starting at first_pos + 1 (the +1 is so it doens't include the '*'
#                                ^^^^^^^^  find() wil be applied to the sliced string
#                                             ^^^^^^^^^^ since the sliced string
#                                                        starts at firstPos+1, add this to our
#                                                        found position for the 2nd '*'
#
print(f"1st '*' at {first_pos}, 2nd '*' at {second_pos}")