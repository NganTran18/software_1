import math

def unit_price_pizza(diameter, price):
    radius = (diameter / 2 ) / 100
    area_pizza = math.pi * (radius **2)

    a_pizza = price / area_pizza
    return a_pizza

def a():
    diameter1 = float(input("What is the diameter for the pizza 1(cm): "))
    price1 = float(input("what is the prices pizza 1: "))

    diameter2 = float(input("What is the diameter for the pizza 2(cm): "))
    price2 = float(input("what is the prices pizza 2: "))

    unit_pizza1 = unit_price_pizza(diameter1, price1)
    unit_pizza2 = unit_price_pizza(diameter2, price2)

    print(f"the prices of the pizza 1:", unit_pizza1 , "euro/m^2")
    print(f"the prices of the pizza 2:", unit_pizza2 ,  "euro/m^2")

    if unit_pizza1 < unit_pizza2:
        print("Pizza 2 is better")

    if unit_pizza2 < unit_pizza1:
        print("Pizza 1 is better")

    else:
        print("2 pizza are the same!")

a()