def remove_uneven(list):
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
evenn_list = remove_uneven(my_list)
print(my_list)