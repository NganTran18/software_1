import mysql.connector
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='people',
         user='root',
         password='1118',
         autocommit=True
         )
connection