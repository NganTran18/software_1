# ap = dict()

# while True:
#     a = input("Enter a new airport, fetch info or Quit (e/f/q)!")

#     if a == "e":
#         icao = input("enter the ICAO code: ")
#         name = input("enter the name of the airport: ")
#         ap.update({icao: name})
#     elif a == "f":
#         icao = input("enter the ICAO code: ")
#         print(f"Airport name: {ap[icao]}")
#     elif a == "q":
#         print("goodbye!")
#         break

#     else: 
#         print("not valid")




ap = dict()

while True:
    user = input("Enter a new airport, fetch info or quit?: ")
    if user == "new":
        code = input("what is code? ")
        name = input("what is name? ")
        ap.update({code: name})
    elif user == "fetch":
        code = input("what is code? ")
        print(f"here is name: ({ap[code]})")
    elif user == "q":
        break 

