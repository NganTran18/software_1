num = int(input(" Enter a number: "))

if num < 0:
    print("It is not prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is NOT a prime number")
            break
    else:
        print("It is a prime number")
