import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flightgame',
         user='flgame',
         password='1111',
         autocommit=True
         )
def a(code):
    sql = f"select name,type from airport where iso_country = '{code}' order by type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return print(result)

airport = input("enter area code: ")
a(airport)
