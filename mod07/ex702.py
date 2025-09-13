names = set()

while True:
    user = input("Enter a name: ")

    if user == "":
        break

    if user in names:
        print("Existing name")
    else:
        print("New name")
    names.add(user)
print("\nAll names:")
for i in names: 
    print(i)