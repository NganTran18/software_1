import math

def a():
    gasolin = float(input("Gasolin(gallon): "))
    if gasolin > 0:
        liter = gasolin * 3.785
    else:
        print("error number")
    return liter

value = a()
print("The gasoline convert to liters: ", value)