import random
def dice(sides):
    dice = random.randint(1, sides)
    return dice

def a():
    sides = int(input("Enter sides of the dice: "))

    while True:

        result = dice(sides)
        print("the result is: ", result)

        if result == sides:
            print("You gets the maximum number on the dice!")
            break
a()