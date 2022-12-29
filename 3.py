import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'Students'
)

create_db = "CREATE DATABASE students"
delete_db = "DROP DATABASE IF EXISTS students"
create_table = ("CREATE TABLE Student (UnqID int PRIMARY KEY AUTO_INCREMENT, StID VARCHAR(7), FullName VARCHAR(50), RollNo smallint, Department VARCHAR(3), Batch VARCHAR(5), Course VARCHAR(4), Mark smallint)")

mycursor = db.cursor()


# mycursor.execute(create_table)

# Default Students Data
StID, FullName, department, Batch, course, RollNo, Mark = ['CSE2201', 'Pratik_Kumar', 'CSE', 'CSE22', 'C001', 24, 50]
mycursor.execute("INSERT INTO Student (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))
StID, FullName, department, Batch, course, RollNo, Mark = 'CSE2202', 'Test_Student1', 'CSE', 'CSE21', 'C002', 29, 85
mycursor.execute("INSERT INTO Student (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))
StID, FullName, department, Batch, course, RollNo, Mark = 'ECE2202', 'Test_Student2', 'ECE', 'ECE22', 'C002', 15, 65
mycursor.execute("INSERT INTO Student (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))
StID, FullName, department, Batch, course, RollNo, Mark = 'ECE2201', 'Test_Student3', 'ECE', 'ECE22', 'C001', 3, 40
mycursor.execute("INSERT INTO Student (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))

db.commit()