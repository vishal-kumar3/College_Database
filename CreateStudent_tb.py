import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'Students_db'
)

create_table = ("CREATE TABLE Student_tb (UnqID int PRIMARY KEY AUTO_INCREMENT, StID VARCHAR(7), FullName VARCHAR(50), RollNo smallint, Department VARCHAR(3), Batch VARCHAR(5), Course VARCHAR(6), Mark smallint)")

mycursor = db.cursor()

print('Creating Table...')
mycursor.execute(create_table)
print('Table Created.')

# Default Students Data
StID, FullName, department, Batch, course, RollNo, Mark = ['CSE2022', 'Vishal_Kumar', 'CSE', 'CSE22', 'JAVA', 24, 90]
mycursor.execute("INSERT INTO Student_tb (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))

StID, FullName, department, Batch, course, RollNo, Mark = 'CSE2021', 'Test_Student1', 'CSE', 'CSE21', 'JAVA', 29, 85
mycursor.execute("INSERT INTO Student_tb (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))

StID, FullName, department, Batch, course, RollNo, Mark = 'IT2022', 'Test_Student2', 'IT', 'IT22', 'PYTHON', 15, 95
mycursor.execute("INSERT INTO Student_tb (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))

StID, FullName, department, Batch, course, RollNo, Mark = 'IT2021', 'Test_Student3', 'IT', 'IT21', 'PYTHON', 3, 70
mycursor.execute("INSERT INTO Student_tb (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))

print('Added Some Default Data Into Table.')

db.commit()
