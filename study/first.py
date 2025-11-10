#user = int(input('Enter a number: '))
#while user > 0 :
 #   print(user)
  #  user = user - 1
#print("kaboom")

#num = 20
#if num > 20:
#    print("A")
#elif num >10:
#   print("B")
#else:
#    print("C")
#print("D")

#attempt = 0
#while attempt < 3:
 #  name = input("Enter your name: ")
  # password = input("Enter your password: ")
#
 #  if name == "james" and password == "bond":
  #      print("Access granted")
   #else:
    #    print("Access denied")
   #attempt = attempt + 1
#print("your attempt number is: ", attempt)

# a = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10,11,12,13,14,15,16,17,18,19]
# print(a[-1])
# print(a[len(a)-1])


# def f():
    # print('hello')
# print(f)

# names = ['A', 'B', 'C', 'D', 'E']
# phones = [35, 84, 90, 75, 25,]
#
num = {"Pekka":"050", "Ahmed": "040", "Viivi":"090"}
# print(num["Ahmed"] )       #print số
# for i in num:
    # print(num[i])
# emset = {}                  #xem nó loại gì
# print(type(emset))

# num["Ahmed"] = 7583    #đổi số 
num["Geogre"] = "010"  #thêm thông tin
# print(num)
# for i in num:
    # print(f'The phone number of {i} is {num[i]}.') #list tất cả

# phonenum = input("Enter the phone number: ")            # hỏi số đó là của ai
# for i in num:
#   if phonenum in {num[i]}:
#     print(f"{phonenum} is {i} number")
#     break
#   else:
#     print("not exist")


import mysql.connector
from geopy.distance import geodesic  # cần cài geopy trước

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flightgame',
         user='flgame',
         password='1111',
         autocommit=True
         )

def coordinates(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cur = connection.cursor()
    cur.execute(sql, (icao,))
    row = cur.fetchone()
    cur.close()
    return row

def distance(code1, code2):
    coords1 = coordinates(code1)
    coords2 = coordinates(code2)

    if not coords1 or not coords2:
        return None


    return geodesic(coords1, coords2).kilometers

while True:
    code1 = input("Enter first ICAO code: ").strip().upper() #strip() -> remove the space at the begin and end
    if code1 =="":
        break
    code2 = input("Enter second ICAO code: ").strip().upper()
    if code2 == "":
        break

    dist = distance(code1, code2)
    if dist is None:
        print("One or both ICAO codes not found.")
    else:
        print(f"Distance between {code1} and {code2}: {dist:.2f} km")





