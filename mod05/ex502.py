number = []

while True:
    user = input("Enter number: ")

    if user == "":
        break

    elif user != "":
        number.append(user)

number.sort(reverse=True)

descending = number[:5]

print("Five greatest numbers sorted in descending order: ")

for item in number:
    print(item)

