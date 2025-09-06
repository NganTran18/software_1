import random
number = random.randint(1, 10)
print("guess the number between 1 and 10? ")

while True:
    guess = int(input("guess the number:"))
    
    if guess == number:
        print("correct")
        break
   
    elif guess < number:
        print("too low, try again")

    elif guess > number:
        print("too high, try again")  