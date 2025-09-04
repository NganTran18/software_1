cabin = input("what class us the cabin (A,B,C.LUX)? ")

if cabin == "LUX":
    print("an upper-deck cabin with a balcony")
elif cabin == "A":
    print(" above the car deck, equipped with a window")
elif cabin == "B":
    print("windowless cabin above the car deck")
elif cabin == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")
