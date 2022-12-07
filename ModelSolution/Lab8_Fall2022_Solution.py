#############################
# EECS1015, York University
# Lab 8 Model Solution
# Author: Michael S. Brown
# (c) Michael S. Brown
# This code cannot be shared without written
# permission from the author.
#
#############################

import random

# find mutations
def find_mutations(virus1, virus2):
    virus1_DNA = virus1.getDNA()            # get DNA
    virus2_DNA = virus2.getDNA()            # get DNA
    mutation_map = ""                       # create empty string
    for i in range(len(virus1_DNA)):         # loop through the DNA
        if virus1_DNA[i] != virus2_DNA[i]:  # if they don't match at this position (i)
            mutation_map += "^"             # add a "^"
        else:                               # else
            mutation_map += " "             # add a " "
    return mutation_map

class virus:
    DNA_list = ["A", "G", "T", "C"]
    def __init__(self, DNA=""):
        assert len(DNA)== 50 or len(DNA) ==0, "DNA must be 50 characters!"
        if DNA != "":
            self.DNA = DNA
            for i in DNA:               # check if DNA string is valid (optional)
                assert i in virus.DNA_list, f"DNA must only contain 'A' 'G' 'C' or 'T'"
        else:
            virus_dna = []              # create a new DNA string
            for i in range(50):
                virus_dna.append( virus.DNA_list[ random.randint(0,3)] )
            self.DNA = "".join(virus_dna)

    def getDNA(self):
        return self.DNA

    def replicate(self):
        new_DNA_list = list(self.DNA)                               # convert to list
        chance = random.randint(1, 100)                             # get chance
        if chance>=95:                                              # if 95 or more
            position = random.randint(0,49)                         # get random postion
            while new_DNA_list[position] == self.DNA[position]:     # if updated choice == old value, keep looping
                new_DNA_list[position] = virus.DNA_list[ random.randint(0, 3) ]
        new_DNA = "".join(new_DNA_list)                             # create new DNA <- if no change, will be the same DNA
        replicated_virus = virus(new_DNA)
        return replicated_virus                                     # return replicate


class lotto_ticket:
    ticket_counter = 0                  # class variable

    def __init__(self):
        lotto_ticket.ticket_counter += 1        # add one to class variable
        self.id = lotto_ticket.ticket_counter   # assign id
        self.numbers = set()                    # get new numbers
        while len(self.numbers) < 5:            # loop until we have 5 new numbers
            self.numbers.add(random.randint(1,20))

    def print_ticket(self):
        print(f"Ticket #[{self.id:3d}]", end="")
        for num in self.numbers:
            print(f"  {num:2d}  ", end="")
        print()

    def print_and_return_win(self, lotto_numbers):
        win_amounts = {0:0, 1:0, 2:0, 3:2, 4:20, 5:100}         # you could use an if statement, but this is faster
        matches = self.numbers.intersection(lotto_numbers)
        num_matches = len(matches)
        win_amount = win_amounts[num_matches]
        print(f"Ticket #[{self.id:3d}]", end="")
        for i in self.numbers:
            if i in matches:
                print(f" *{i:02d}* ", end="")
            else:
                print(f"  {i:02d}  ", end="")
        print(f"\t[{num_matches} matches, ${win_amount}]")

        return win_amount

# lotto draw function
def lotto_draw():
    numbers = set()
    while len(numbers) < 5:
        numbers.add(random.randint(1,20))
    return numbers

def print_lotto_draw(numbers):
    print("--LOTTO DRAW--")
    for i in numbers:
        print(f"{i:2d} ", end="")
    print()

def task1():
    amount = 100
    tickets = None
    while amount >= 2:
        print(f"You have ${amount}.")
        x = int(input("How many lotto tickets do you want [$2 each]? "))
        if x < 0 or x*2 > amount:
            continue
        elif x==0:
            break
        elif x*2 <= amount:
            # buy some tickets
            amount -= x*2
            tickets = []            # create ticket list
            for i in range(x):
                new_ticket = lotto_ticket() # get a new ticket object
                new_ticket.print_ticket()   # print it out
                tickets.append(new_ticket)  # add it the ticket list

        lotto_numbers = lotto_draw()        # draw lotto numbers
        print_lotto_draw(lotto_numbers)     # print them

        input("---Press enter to check your winnings---")
        for ticket in tickets:                                          # loop through tickets
            win_amount = ticket.print_and_return_win(lotto_numbers)     # compute win and print
            amount += win_amount                                        # add to amount

    # loop back to while

    print(f"You have ${amount}.")                                       # our final amount

def task2():
    YN = "Y"
    while YN == "Y":
        name = input("Name of virus: ")
        my_virus = virus()                                      # create a virus
        print(f"Original DNA sequence: {my_virus.getDNA()}")
        times = int(input("How many times to replicate? "))
        original_virus = my_virus                               # remember starting virus
        for i in range(times):                                  # loop to repliacte
            my_virus = my_virus.replicate()                     # replicate
            print(f"Replica [{i:4d}] DNA sequence: {my_virus.getDNA()}")    # print it out

        print(f"Comparing latest {name} virus to the original {name}.")
        DNA_difference = find_mutations(original_virus, my_virus)   # get differences
        print(original_virus.getDNA())                              # print original
        print(my_virus.getDNA())                                    # print new one
        num_of_differences = DNA_difference.count("^")              # count # of differneces
        if num_of_differences > 5:                                  # more than 5
            print(DNA_difference)
            print(f"{num_of_differences} mutations -- a *new* virus has been created.")
        elif num_of_differences > 0:                                # more than 0
            print(DNA_difference)
            print(f"{num_of_differences} mutations -- virus is the same.")
        else:                                                       # none
            print("No mutations detected.")

        YN = input("Try again? ").upper()           # try again


def main():
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
    main()