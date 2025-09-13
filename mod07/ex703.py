ap = dict()

while True:
    a = input("Enter a new airport, fetch info or Quit (e/f/q)!")

    if a == "e":
        icao = input("enter the ICAO code: ")
        name = input("enter the name of the airport: ")
        ap.update({icao: name})
    elif a == "f":
        icao = input("enter the ICAO code: ")
        print(f"Airport name: {ap[icao]}")
    elif a == "q":
        print("goodbye!")
        break

    else: 
        print("not valid")
