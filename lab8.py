##################################
# EECS1015 - York University
# Author: Michael S. Brown 
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 8 starter code
#
##################################
import random


def print_student_info():
    print("Name: Cao Huanrui")
    print("Student ID: 219256809")
    print("Section A")
    print("Email: saikoro@my.yorku.ca")

def is_vaild_sequence(dna):
    if dna[0] not in ['A','T','G','C']:
        return False
    if len(dna) == 1:
        return True
    return is_vaild_sequence(dna[1:])

# class for task 2
class virus:

    def __init__(self, DNAinput=""):
        if len(DNAinput) ==50 and is_vaild_sequence(DNAinput), 
        self.DNA = DNAinput
        "Invalid DNA input! "
        

# class for task 1
class lotto_ticket:
    ticket_counter = 1
    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_counter
        self.numbers = set()
        while len(self.numbers) <5 :
            ranint = random.randint(1, 20)
            self.numbers.add(ranint)
        lotto_ticket.ticket_counter = lotto_ticket.ticket_counter + 1
        
    def print_ticket(self):
        print("Ticket #[%3d]" % (self.ticket_id),end='')
        for i in self.numbers:
            print(f"  {i:2d}  ",end='')
        print()
        
    def print_and_return_win(self, lotto_numbers) -> int:
        com_set = self.numbers & lotto_numbers
        print("Ticket #[%3d]" %(self.ticket_id),end='')
        for i in self.numbers:
            if i in lotto_numbers:
                print(f" *{i:02d}* ",end="")
            else:
                print(f"  {i:02d}  ",end="")
        match = len(com_set)
        if match == 3:
            win_amount = 2
        elif match == 4:
            win_amount = 20
        elif match ==5:
            win_amount = 100
        else:
            win_amount = 0
        print(f"    [{match:d} matches, ${win_amount:d}]")
        return win_amount

def lotto_draw():
        lotto_set = set()
        while len(lotto_set) <5 :
            ranint = random.randint(1, 20)
            lotto_set.add(ranint)
        print("--LOTTO DRAW--")
        for item in lotto_set:
            print(f" {item:d} ", end = "")
        print()
        return lotto_set

  
def task0():
    print_student_info()

def task1():
    amount = 100
    print(f"You have ${amount:d}")
    ticket_amount = int(input("How many lotto tickets do you want [$2 each]? "))
    while (ticket_amount != 0 and amount >=2):
        while (ticket_amount*2> amount) or (ticket_amount < 0):
            ticket_amount = int(input("How many lotto tickets do you want [$2 each]? "))
        ticket_list = []
        amount = amount - ticket_amount*2
        for i in range(ticket_amount):
            ticket_list.append(lotto_ticket())
        for item in ticket_list:
            item.print_ticket()
        lotto_numbers = lotto_draw()
        input("---Press enter to check your winnings---")
        for item in ticket_list:
            amount = amount + item.print_and_return_win(lotto_numbers)
        print(f"You have ${amount:d}.")
        if (amount >=2):
            ticket_amount = int(input("How many lotto tickets do you want [$2 each]? "))
        else:
            break
    print(f"\nYou have ${amount:d}")




def task2():
    pass

def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
      main()