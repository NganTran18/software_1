import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flightgame',
         user='flgame',
         password='1111',
         autocommit=True
         )

def a(x):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{x}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

code1 = input("Enter code 1: ")
code2 = input("Enter code 2: ")
a(code1)
a(code2)
list1 = list()
list2 = list()
list1.append(a(code1))
list2.append(a(code2))
list1 = tuple(list1)
list2 = tuple(list2)
distance = geodesic(list1, list2)
print(distance)


