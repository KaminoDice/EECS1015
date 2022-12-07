############################
# EECS1015, York University
# Practice questions #8
# Nested collections
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be copied or distributed without permission from the author.
# These examples provide at least *one way* of answering the questions.
# Variations that give the same results are fine.
#
############################
import time
import random

class random_sequence:
    def __init__(self, characters=('0','1','2','3','4','5','6','7','8','9')):
        self.characterSet = characters
        self.length = len(characters)

    def get_sequence(self, N=5):
        sequence = []
        assert N > 0, "N must be 1 or larger!"
        for i in range(N):
            pos = random.randint(0, self.length-1)
            sequence.append( self.characterSet[pos] )
        return sequence

print("---Q1. Random sequence object---")
print("Default generator")
default_generator = random_sequence()
print("N=5" , default_generator.get_sequence(5) )
print("N=10", default_generator.get_sequence(10))
print("Object for '0', '1' only")
binary_generator = random_sequence(('0', '1'))
print("N=10", binary_generator.get_sequence(10))
print("N=20", binary_generator.get_sequence(20))
abc_generator = random_sequence(('A', 'B', 'C'))
print("N=10", abc_generator.get_sequence(10))
print("N=20", abc_generator.get_sequence(20))


class stat_analyzer:
    def __init__(self, numbers):
        assert len(numbers) >=3, "Must be a list of at least 3 or more numbers."
        self.num_list = numbers
        self.num_list.sort()
        self.N = len(self.num_list)

    def average(self):
        sum = 0
        for i in self.num_list:
            sum += i
        return sum / self.N

    def median(self):
        return self.num_list[ self.N // 2 ]

    def min(self):
        return self.num_list[0]

    def max(self):
        return self.num_list[-1]

    def print_list(self):
        print(self.num_list)

print("--- Q2. Statistical analyzer ---")
x = stat_analyzer([8, 8, 9, 10, 10, 11, 0, 0, 2, 2, 2, 2, 2, 2, 1])
x.print_list()
print("Average {} Median {}  Min {}  Max {} ".format(x.average(), x.median(), x.min(), x.max()))
x = stat_analyzer([2.3, 2.8, 2.8, 2.3, 2.1, 2.0, 2.2, 2.2, 2.1, 2.3, 2.9, 2.9, -8.7])
x.print_list()
print("Average {:.2f} Median {}  Min {}  Max {} ".format(x.average(), x.median(), x.min(), x.max()))

class greeting:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def greet(self):
        name = self.name
        if self.language == "A":
            print(f"Marhaba, {name}!")
        if self.language == "C":
            print(f"Ni hao, {name}!")
        if self.language == "S":
            print(f"Hola, {name}!")
        if self.language == "P":
            print(f"Witam, {name}!")
        if self.language == "F":
            print(f"Salam, {name}!")
        if self.language == "E":
            print(f"Hi, {name}!")

print("---Q3. Kulti-lanauge Greetings ---")
mahsa   = greeting("Mahsa", "F")
chad    = greeting("Chad", "E")
javier  = greeting("Javier", "S")
abdo    = greeting("Abdel", "A")
oskar   = greeting("Oskar", "P")
luxi    = greeting("Luxi", "C")
mahsa.greet()
chad.greet()
javier.greet()
oskar.greet()
luxi.greet()
abdo.greet()

class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_equation(self):
        print(f" y = {self.a}x^2 + {self.b}x + {self.c}")

    def compute_y(self,x):
        y = self.a*(x**2) + self.b*x + self.c
        return y

    def compute_range(self, start_x, end_x):
        self.print_equation()
        print("    X     |    Y     ")
        for x in range(start_x, end_x+1):
            y = self.compute_y(x)
            print(f"{x:10d}|{y:10d}")

print("--- Q4. Quadratic object ---")
eq1 = quadratic(2,-2, 5)
eq2 = quadratic(1, 2, -2)
eq1.compute_range(-10, 10)
eq2.compute_range(-10, 10)

class snail:
    forward_animation = ["__~@", "_~_@", "~__@"]
    backward_animation  = ["@~__", "@_~_", "@__~"]

    def __init__(self, speed=1):
        self.pos = 0
        self.speed = speed
        self.direction = 1
        self.anim_index = 0

    def update_animation(self):
        if self.anim_index >= 2:
            self.anim_index = 0
        else:
            self.anim_index+= 1

    def move_forward(self):
        self.pos += self.speed
        if self.pos >= 50:
            self.pos = 50
        self.direction = 1
        self.update_animation()

    def move_backward(self):
        self.pos -= self.speed
        if self.pos < 0:
            self.pos = 0
        self.direction = -1
        self.update_animation()

    def print_snail(self):
        print(self.pos * " ", end="")
        if self.direction == 1:
            print(snail.forward_animation[self.anim_index])
        else:
            print(snail.backward_animation[self.anim_index])

print("---Q5. The snail ---")
snail1 = snail(5)
snail2 = snail(2)
for i in range(5):
    snail1.print_snail()
    snail1.move_forward()
    snail2.print_snail()
    snail2.move_forward()
    time.sleep(0.3)
for i in range(5):
    snail1.print_snail()
    snail1.move_backward()
    snail2.print_snail()
    snail2.move_backward()
    time.sleep(0.3)