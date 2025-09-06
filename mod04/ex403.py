list = []
while True:
    num = input("enter numbers or empty string to quit: ")
    if num == '':
        break
    list.append(float(num))
if list:        
    print(f"Largest: {max(list)}")
    print(f"Smallest: {min(list)}")
