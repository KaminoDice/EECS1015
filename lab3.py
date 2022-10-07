import random

print(""""
---- Task 1: Simple order ----
**Select menu itme**
 (1) Coke   [$1.00]
 (2) Dose   [$2.50]
 (3) Pizza  [$2.25]
 (4) Taco   [$1.50]
 (5) Tea    [$1.00]
""")
amount_list = [1.00, 2.50, 2.25, 1.50, 1.00]

sel_item = int(input("Selection: "))
if sel_item in range(1, 6):
    amount = float(amount_list[sel_item])
else:
    print("Invalid selection - setting amount to $0")
    amount = 0.00

print("""
**Discount**
(C) Child   [under 18] (50% discount)
(A) Adult   [18-64]
(S) Senior  [65+] (25% discount)
""")
sel_dis = input("Selection age: ").upper()
if sel_dis == "C":
    disc_rate = 0.5
elif sel_dis == "A":
    disc_rate = 0
elif sel_dis == "S":
    disc_rate = 0.25
else:
    print("%s is an invalid selection! Extra charge for you!" % sel_dis)
    disc_rate = -0.25

discount = amount * disc_rate
total = amount - discount

print(f"""
Amount   ${amount:6.2f}
Discount ${discount:6.2f}
------------------
Total    ${total:6.2f}
""")

radius = int(input("Input size between 1-10:"))

while (radius > 10) or (radius < 1):
    radius = int(input("Input size between 1-10:"))

for y in range(-10, 11):
    for x in range(-10, 11):
        if x ** 2 + y ** 2 > radius ** 2:
            print(".", end="")
        else:
            print("*", end="")
    print("")

dice_sum = 0
times_roll = int(input("Roll dice how many times? "))
for x in range(times_roll):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll = dice1 + dice2
    dice_sum = dice_sum + roll
    print("[%d] [%d] -- %2d Roll %d" % (dice1, dice2, roll, x + 1))
avg = dice_sum / times_roll
print("Average dice pair value: %4.2f" % avg)
try_again = input("Try again [Y/N] ").upper()

while try_again == "Y":
    dice_sum = 0
    times_roll = int(input("Roll dice how many times? "))
    for x in range(times_roll):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2
        dice_sum = dice_sum + roll
        print("[%d] [%d] -- %2d Roll %d" % (dice1, dice2, roll, x + 1))
    avg = dice_sum / times_roll
    print("Average dice pair value: %4.2f" % avg)
    try_again = input("Try again [Y/N] ").upper()

pi_r = 3.14159265359
M = int(input("Input number of terms, M: "))
sigma = 0

for n in range(M + 1):
    term_A = (-1) ** n
    term_B = 2 * n + 1
    term = term_A / term_B
    sigma = sigma + term
    pi_o = 4 * sigma
    print("n=%d . . . adding fraction: %d/%d" % (n, term_A, term_B))
    print("our  pi = %.11f" % pi_o)
    print("real pi = %s" % pi_r)
