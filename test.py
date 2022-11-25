class A:
    y = 0     
    def __init__(self, id):
        self.x = id
        A.y = id
    def printID(self):
        print(self.x)
x1 = A(1)
x2 = A(10) 
x3 = A(-1)

x1.printID()

'''

class Foo:
   def __init__(self, x):
      self.x = 10
   def print(self):
      print(self.x)
a = Foo(10)
b = Foo(20)
a.x = 20
a.print()
b.print()

class Foo:
   def _init_(self, name, age = 18):
      self.name = name
      self.age = age

class A:
    def __init__(self, id):
        self.x = id

class B:
    def __init__(self, id):
        self.x = A(id+1)

class C:
    def __init__(self, id):
         self.x = B(id+1)

x = C(10)
print(x.x.x.x)

class A:
  y = 0     
  def __init__(self, id):
    self.x = id
    A.y = id
  def printID(self):
    print(A.y)

def main():
  x1 = A(1)
  x2 = A(10) 
  x3 = A(-1)
  x1.printID()

if __name__ == "__main__":
  main()

x = set(input("Enter 5 numbers between 1-20: ").split())
print(x)

### Task 2.5
print("\n---- Task 2.5: Draw square ----")

radius = int(input("Input size between 1-10:"))

while (radius > 10) or (radius < 1):
    radius = int(input("Input size between 1-10:"))

for y in range(-10, 11):
    if (y > radius) or (y < -radius):
        for x in range(-10, 11):
            print(".",end="")
        print("")
    else:
            for x in range(-10, 11):
                if (x > radius) or (x < -radius):
                    print(".", end="")
                else:
                    print("*", end="")
            print("")
import math
print('\n---- Task 4: Simple cylinder computation ----')
a="pi"
print(a)
string0 = input("Type a long string: ")
string1 = string0.upper().replace("T", "7").replace("A","^").replace("E", "3").replace("I", "!").replace("B", "8").replace("O", ".").replace("C","<").replace("S","$")
print(string1)
print("\n---- Task 3: Substring highlighter ----")
string2 = input("Type a sentence at the prompt blow:\n>")
string3 = input("Enter substring below to highlight:\n>")
len1 = string2.find(string3)
len2 =len(string2)
len3 =len(string3)
print("Sentence has {} characters, substring has {} characters.".format(len2, len3))
stringA = string2[:len1]
stringB = string3.upper()
stringC = string2[(len1+len3):]
print(stringA+"*"+stringB+"*"+stringC)

print("\n---- Task 4: Exponent ----")
expo = input("Input exponent in the form x^y: ")
index = expo.find("^")
n1 = int(expo[:index])
n2 = int(expo[index+1:])
print("Extracted numbers %d %d" % (n1 ,n2) )
n3 = n1**n2
print("%d" % n3)
'''