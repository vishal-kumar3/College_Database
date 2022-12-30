
import mysql.connector

print('No Error in Import')


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin'
) 

create_db = "CREATE DATABASE students_db"

mycursor = db.cursor()

print('No Error in connection')

mycursor.execute("DROP database IF EXISTS Students")

mycursor.execute(create_db)
print('Created Database Students')

