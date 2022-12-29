
# Import sql-connector
import mysql.connector

# Import libraries
from matplotlib import pyplot as plt
import numpy as np

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'Students'
)


mycursor = db.cursor()


create_db = "CREATE DATABASE students"
delete_db = "DROP TABLE IF EXISTS Student"
create_table = "CREATE TABLE Student (ID int PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(20), Roll smallint UNSIGNED, Batch VARCHAR(5))"
fetch_tabledetails = "DESCRIBE Student"
insert_data = "INSERT INTO Student (Name, Roll, Batch) VALUES (%s, %s, %s, %s)", (1, "Vishal", 24, "CSE22")
students_details = "SELECT * FROM Student"

add_column = "ALTER TABLE Student ADD COLUMN food VARCHAR(20)"
change_column_name = "ALTER TABLE Student CHANGE name first_name VARCHAR(20)"


def sql_print():
    result = mycursor.fetchall()
    for x in result:
        print(x)


def new_table():
    mycursor.execute(delete_db)

    print('Creating Table')
    mycursor.execute("CREATE TABLE Student (UnqID int PRIMARY KEY AUTO_INCREMENT, StID VARCHAR(7), FullName VARCHAR(50), RollNo smallint, Department VARCHAR(3), Batch VARCHAR(5), Course VARCHAR(4), Mark smallint)")
    print('Table created')


# new_table()


def batch_CSE():
    print('\nSet Batch Info...')
    bat = input('''1.CSE22\n2.CSE21\n>''')
    if bat == '1':
        Batch = 'CSE22'
    elif bat == '2':
        Batch = 'CSE21'
    
    return Batch


def batch_ECE():
    print('\nBatch Set to "ECE22"')
    Batch = 'ECE22'
    return Batch


def student_id_number():

    print('\nSet Student ID...')
    StIDNo = input('1.CSE2201\n2.CSE2101\n3.ECE2201\n4.ECE2202\n>')
    if StIDNo == '1':
        StID = 'CSE2201'
        department = 'CSE'
        batch = batch_CSE()

    elif StIDNo == '2':
        StID = 'CSE2101'
        department = 'CSE'
        batch = batch_CSE()

    elif StIDNo == '3':
        StID = 'ECE2201'
        department = 'ECE' 
        batch = batch_ECE()
               
    else:
        StID = 'ECE2202'
        department = 'ECE'
        batch = batch_ECE()
    
    return StID, department, batch


def course_name():
    print('\nSet course...')
    cour = input('''1.C001\n2.C002\n>''')
    if cour == '1':
        course = 'C001'
    else:
        course = 'C002'
    
    return course


def insert_data():
    FullName = input("\nEnter Full Name of Student(use '_' instead of 'space'): ")
    Mark = 0

    StID, department, Batch = student_id_number()
    course = course_name()

    RollNo = int(input('Enter Roll Number: '))

    
    mycursor.execute("INSERT INTO Student (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))
    print('\nStudent Added\n')
    db.commit()


def examination():

    print('Student\'s List:-\n')
    print('\n(UID | SttID | FullName | Roll | Department | Batch | Course | Mark)')

    mycursor.execute(students_details)
    sql_print()
    print('\nUPDATE STUDENTS MARKS HERE...\n')
    stID = int(input('Enter Student ID: '))
    mark = int(input('Enter Marks of student:'))

    mycursor.execute(f'''
    UPDATE Student
    SET Mark = {mark}
    WHERE UnqID = {stID}
    ''')
    db.commit()
    print('Done')



choice = 6

while choice != 0:

    print('\n--------Student Examination Portal--------\n')
    print('''
    1. Add Student
    2. Update Student Marks
    3. Department
    4. Course
    5. Complete Student Details
    6. Marks of all Students
    0. Exit Program
    ''')

    choice = int(input('StudentDataBase>'))
    
    if choice == 1 :
        print('Write Full Details Here...')
        insert_data()


    elif choice == 2 :
        print('Update Marks Here...')
        # Marks
        examination()


    elif choice == 3 :
        print('Students By Department:-\n')

        Department = int(input('Department of Student :-\n1. CSE\n2. ECE\n>'))
        if Department == 1 :
            Department = 'CSE'
        else:
            Department = 'ECE'

        mycursor.execute(f'SELECT * FROM Student WHERE Department = "{Department}"\n')
        sql_print()


    elif choice == 4 :
        print('Student By Course:-\n')

        Course = int(input('Course of Student :-\n1. C001\n2. C002\n>'))
        if Course == 1 :
            Course = 'C001'
        else:
            Course = 'C002'

        mycursor.execute(f'SELECT * FROM Student WHERE Course = "{Course}"\n')
        sql_print()


    elif choice == 5:
        print('Listing Student\'s Deatails here')
        print('(UID | SttID | FullName | Roll | Department | Batch | Course | Mark)')
        mycursor.execute(students_details)
        sql_print()


    elif choice == 6 :

        yes = input('Have You Updated Students Marks? (y/n) >')
        if yes == 'n':
            print('First Update Marks And Come Back...')
        elif yes == 'y':
            name_list = []
            mark_list = []
            print(f'Pie Chart for Students...\n')

            mycursor.execute('SELECT Mark FROM Student')
            result = mycursor.fetchall()
            for x in result:
                for y in x:
                    mark_list.append(y)

            mycursor.execute('SELECT FullName FROM Student')
            result = mycursor.fetchall()
            for x in result:
                for y in x:
                    name_list.append(y)

            # Creating pie chart
            fig = plt.figure(figsize=(10, 7))
            plt.pie(mark_list, labels = name_list)

            # Show plot
            plt.show()
        else: 
            print('Please Choose options correctly')



print('Exiting Program...')

db.close()

