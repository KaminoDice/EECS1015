#########
# EECS1015 Fall 2022
# Lab 2
# Name: 
# Sudent id: 
#########

print("---- Lab 2 ----")
print("Name: ")
print("Section A")
print("Student id: ")
print("Email: ")

# Task 1
print("\n---- Task 1: Three year investment return ----")
name = input("Name: ").strip().title()
iA = float(input("Initial amount: $ "))
rate = float(input("Rate of return: % "))
Rrate = rate/100
print("Client: {}, yearly rate of return multiplier: {:.2f}".format(name,Rrate))
y1A = iA+iA*Rrate
y2A = y1A+y1A*Rrate
y3A = y2A+y2A*Rrate
print("Year 1\tStarting Amount: ${:8.2f}\t\tEnding Amount: ${:8.2f}".format(iA,y1A))
print("Year 2\tStarting Amount: ${:8.2f}\t\tEnding Amount: ${:8.2f}".format(y1A,y2A))
print("Year 3\tStarting Amount: ${:8.2f}\t\tEnding Amount: ${:8.2f}".format(y2A,y3A))

# Task 2
print("\n----Task 2 Leetspeak converter ----")
string0 = input("Type a long string: ")
string1 = string0.upper().replace("T", "7").replace("A","^").replace("E", "3").replace("I", "!").replace("B", "8").replace("O", ".").replace("C","<").replace("S","$")
print(string1)


# task 3
print("\n---- Task 3: Substring highlighter ----")
string2 = input("Type a sentence at the prompt blow:\n> ")
string3 = input("Enter substring below to highlight:\n> ")

len1 = len(string2)
len2 = string2.find(string3)
len3 = len(string3)

print("Sentence has {} characters, substring has {} characters.".format(len1, len3))
stringA = string2[:len2]
stringB = string3.upper()
stringC = string2[(len2+len3):]
print("Substring highlighted:\n> "+stringA+"*"+stringB+"*"+stringC)

# task 4
print("\n---- Task 4: Exponent ----")
expo = input("Input exponent in the form x^y: ")
index = expo.find("^")
n1 = int(expo[:index])
n2 = int(expo[index+1:])
print("Extracted numbers %d %d" % (n1 ,n2) )
n3 = n1**n2
print("%d" % n3)

# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")