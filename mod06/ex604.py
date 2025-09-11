def num(list):
    total = 0
    for sum in list:
        total += sum
    return total

my_list = [1, 2, 3, 4, 5, 6 ,7, 9 ,10]
result = num(my_list)

print(f'the sum of the number is {my_list} and result is {result}')
