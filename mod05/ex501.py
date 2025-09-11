import random

dice = int(input("how many dice to roll? "))

total = 0

for item in range(dice):
    roll = random.randint(1, 6)
    total += roll

print("The sum of the dice rolls is:", total)