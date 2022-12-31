
# Import sql-connector
import mysql.connector

# Import csv to access csv file and edit it
import csv   

# Importing pyplot from matplotlib library to create graphs
from matplotlib import pyplot as plt

# To do system work
import os
import sys
import subprocess


# Connecting to mysql sever and using 'Students' database
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'Students_db'
)

# Creating an object that is used to excecute mysql commands in python
mycursor = db.cursor()

# Making global variables to use them further in this program
create_db = "CREATE DATABASE students"
delete_db = "DROP TABLE IF EXISTS Student"
create_table = "CREATE TABLE Student (ID int PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(20), Roll smallint UNSIGNED, Batch VARCHAR(5))"
students_details = "SELECT * FROM Student_tb"


# variables used to access certain values from Table 'Student'
global_uid = 0
global_studentID = 1
global_name = 2
global_roll = 3
global_department = 4
global_batch = 5
global_course = 6
global_marks = 7


# printing the data retrived from Table 'Student'
def sql_print():
    """
    To Make it to print anything from mysql database
    """    
    # retriving all data of Table
    result = mycursor.fetchall()
    for x in result:
        print(x)

# To identify what machine is used to run this program
def get_platform():
    # Trying to find out which platform is used to run this program
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]


if get_platform() == 'Linux':
    fileName = '/'
else:
    fileName = '\\'

# To open any file from python using subprocess
def open_file(file_name):
    # opening the file using subprocess
    subprocess.run(['start', file_name], shell=True)
    

def continue_function():
    input('Press Enter to continue [This will clear the screen]...)
    # To clear the screen
    os.system('cls')


# To create new table if needed
def new_table():
    """To create New Table using mysql code
    """    
    mycursor.execute(delete_db)

    print('Creating Table')
    mycursor.execute("CREATE TABLE Student (UnqID int PRIMARY KEY AUTO_INCREMENT, StID VARCHAR(7), FullName VARCHAR(50), RollNo smallint, Department VARCHAR(3), Batch VARCHAR(5), Course VARCHAR(6), Mark smallint)")
    print('Table created')


# Options to Choose stream of students
def st_stream():
    """ To get the stream of student while their register process

    Returns:
        stream: Variable containing CSE or IT
    """    
    stream = int(input('\nChoose Stream:-\n1. CSE\n2. IT\n>'))
    if stream == 1:
        stream = 'CSE'
    else:
        stream = 'IT'
    # returning the value stream
    return stream


# Options to choose students year
def st_year():
    """While registration to choose their 4 year session

    Returns:
        year : Student year session
    """    
    year = int(input('\nChoose Year:-\n1. 2021-25\n2. 2022-26\n>'))
    if year == 1:
        year = '2021-25'
    else:
        year = '2022-26'
    # returning the value year
    return year


# Manipulating the Students data here
def student_info():
    """Manages Student data here :-
        It manages studentID, Department, Batch and Course of student
        using their stream and year.

    Returns:
        StID : Student id 
        department : department of student
        batch : batch of student
        course : assigned course of student
    """    

    # defining stream and year
    stream = st_stream()
    year = st_year()

    # defining Student ID and Batch 
    StID = stream + year[:4]
    batch = stream + year[2:4]

    # defining the course according to their stream
    course_dict = {
        'CSE' : 'JAVA',
        'IT' : 'PYTHON'
    }
    course = course_dict[stream]
    # defining department of student
    department = stream

    # returning all the values
    return StID, department, batch, course


# function to insert data into table
def insert_data():
    """This Function Adds or Insert Data into the Table in mysql Database.

        This function inserts all student data like FullName, Roll, StID, department, batch and Course\n
        using student_info() function
    """    

    # user input for Full Name
    FullName = input("\nEnter Full Name of Student(FirstName_LastName): ")
    Mark = -1 # defining the default value of marks and will update later

    # Retriving all values from student_info() function
    StID, department, Batch, course = student_info()

    RollNo = int(input('\nEnter Roll Number: '))


    # mysql code to insert data into Table
    mycursor.execute("INSERT INTO Student_tb (StID, FullName, Department, Batch, Course, RollNo, Mark) VALUES (%s,%s,%s,%s,%s,%s,%s)", (StID, FullName, department, Batch, course, RollNo, Mark))
    print('\nStudent Added\n') 
    db.commit() # commiting the change in table to save it

# To update Students Marks
def update(idMarkUpdate):
    """To Update Marks column in Student Table in Database

    Args:
        idMarkUpdate (list): list of student data containing stID and stName
    """    
    
    for student_marks_data in idMarkUpdate:
        stID, stName = student_marks_data
        print('\nUPDATE STUDENTS MARKS HERE...')

        print(f'Enter marks for UID : {stID}, Name : {stName}')
        mark = int(input('Marks> ')) # Enter Marks of the student
    
        # mysql command to update marks in the table
        mycursor.execute(f'''
        UPDATE Student_tb
        SET Mark = {mark}
        WHERE UnqID = {stID}
        ''')
    
        db.commit() # commit the changes
    
        print('Marks Updated')


# To update marks of student
def examination():
    """To find if update is required or not
        if Update is required :- it will retrive student data from update(idMarkUpdate) function
    """    

    print('Student\'s List:-')

    # fetching all the data into variale result
    mycursor.execute(students_details)
    result = mycursor.fetchall()

    idMarkUpdate = [] # to store unique ids and name of students whoose mark is not updated

    print('\nUID |   Full_Name   | Course | Marks(Default)')
    for x in result:
        if x[global_marks] == -1 or x[global_marks] < 0 or x[global_marks] > 100: # marks = -1 means they are to update
            idMarkUpdate.append((x[global_uid], x[global_name]))
            print(f'{x[global_uid]}   | {x[global_name]} | {x[global_course]} | {x[global_marks]}') # printing uid, name, course and mark to user
    
    # to check if we have students to update their marks or not
    if len(idMarkUpdate) > 0:
        update(idMarkUpdate)
    else:
        print('All Student\'s Marks are UpToDate...')
    

# Function to find the grades of student
def find_grade(marks):
    """To find grades of student

    Args:
        marks (int): marks of individual student

    Returns:
        grade: Will return A,B,C,D,E or F
    """    
    
    if 100 >= marks >= 90:
        return 'A'

    elif marks >= 80:
        return 'B'

    elif marks >= 70:
        return 'C'

    elif marks >= 60 :
        return 'D'

    elif marks >= 50 :
        return 'E'

    elif 0 <= marks < 50 :
        return 'F'

    else:
        print('This Mark is invalid plz update from option 2...')

# This function is to make graph (pie chart)
def graph():
    """This Function will plot a pie chart of all Student in college.
    """    

    # if you have updated all students marks
    yes = input('Have You Updated Students Marks? (y/n) >')
    # if not updated
    if yes == 'n':
        print('First Update Marks And Come Back...') 
        examination() # jump to examination portal or update marks portal

    elif yes == 'y':
        name_list = [] # here we have name of students
        mark_list = [] # hare we have marks corresponding to students name
        print(f'Pie Chart for Students...\n')

        # to retrive marks from mysql database
        mycursor.execute('SELECT Mark FROM Student_tb')
        result = mycursor.fetchall()
        for x in result:
            for y in x:
                # adding marks to mark_list
                mark_list.append(y)

        # now retriving FullName from mysql database
        mycursor.execute('SELECT FullName FROM Student_tb')
        result = mycursor.fetchall()
        for x in result:
            for y in x:
                # adding name to name_list
                name_list.append(y)

        # Creating pie chart
        fig = plt.figure(figsize=(10, 7)) # defining the chart size (width, height)
        plt.pie(mark_list, labels = name_list) # providing the data to make pie chart

        # Show plot
        plt.show()

# Result of all Student
def students_marks():
    """To Create marks.csv file containg all students marks in a file
    """    

    # opening file marks.cse 
    with open('marks.csv', 'w') as result:
        # defining the heading of csv file
        fieldnames = ['UID', 'FullName', 'Course', 'Marks', 'Grade']

        # using DictWriter to make a writer object 
        writer = csv.DictWriter(result, fieldnames=fieldnames)
    
        writer.writeheader() # writing the heading in csv file

        # storing the fetched data into student_info variable
        data = "SELECT * FROM Student_tb"
        mycursor.execute(data)
        student_info = mycursor.fetchall()

        # iterating through student_info variable
        for x in student_info:
            # marks = 7
            st_marks = x[global_marks] # student marks
            grade = find_grade(st_marks) # finding grade of student 
            # writing into csv file
            writer.writerow({'UID': x[global_uid], 'FullName': x[global_name], 'Course': x[global_course], 'Marks': x[global_marks], 'Grade': grade})

    # getting the path of marks.csv
    print('File Saved at ', os.getcwd() + fileName + 'marks.csv')
    
    try:
        # opening the file marks.csv 
        open_file("marks.csv")
    except:
        pass

    print('marks.csv file is Updated and Saved!')



def report_info(uniqueID):
    """To Find Student's data related to their report card 

    Args:
        uniqueID (int): This is the Unique Student ID generated during the registration Process.

    Returns:
        ReportCardInfo: All data related to individual student result
    """    

    # mysql code to fetch all students data
    studentInfoFromTable = 'SELECT * FROM Student_tb'
    mycursor.execute(studentInfoFromTable)
    fetchData = mycursor.fetchall()

    # finding the correct student using uid
    for x in fetchData:
        if x[global_uid] == uniqueID:
            break
    
    return x[global_name], x[global_roll], x[global_department], x[global_studentID], x[global_course], x[global_marks], find_grade(x[global_marks])


# To create report card of specified Student
def reportCard(Name, RollNo, Stream, StudentID, Subject, Marks, Grade, uniqueID):
    """Report Card Generator Function

    Args:
        Name (str): Student Name
        RollNo (int): student roll number
        Stream (str): stream of student
        StudentID (str): student id
        Subject (str): course enrolled
        Marks (int): marks obtained
        Grade (str): grades according to their marks
        uniqueID (int): Unique Id Generated During their Registration process
    """    

    # creating and opening reportCard
    with open(f'{Name}ReportCard.txt', 'w') as report:

        # defining the data to write into the text file
        data = f'''
Unique ID of Student: {uniID}
Name of the student : {Name}
Class Roll of the student : {RollNo} 
Stream of the student : {Stream}
Your Student ID is : {StudentID}\n
Marks obtained in {Subject}: {Marks}
Your Grade : {Grade}
'''
        # writing the data
        report.write(data)

choice = 7

while choice != 0:

    print('\n--------Student Examination Portal--------\n')
    print('''
    1. Register New Student
    2. Update Student Marks
    3. Department
    4. Course
    5. Complete Student Details
    6. Marks of Students
    7. Report Card of Perticular Student
    8. Graphical Representation of marks
    0. Exit Program
    ''')

    choice = int(input('StudentDataBase> '))
    
    # To register student details in Database
    if choice == 1 :
        print('\nWrite Full Details Here...')
        insert_data()
        continue_function()

    # To update marks of students
    elif choice == 2 :
        print('\nUpdate Marks Here...')
        # Marks
        examination()
        continue_function()

    # To filter students on base of their department
    elif choice == 3 :
        print('Students By Department:-\n')

        Department = int(input('Department of Student :-\n1. CSE\n2. IT\n>'))
        if Department == 1 :
            Department = 'CSE'
        else:
            Department = 'IT'

        mycursor.execute(f'SELECT * FROM Student_tb WHERE Department = "{Department}"')
        print()
        sql_print()
        continue_function()

    # To filter students on base of their Course
    elif choice == 4 :
        print('Student By Course:-\n')

        Course = int(input('Course of Student :-\n1. JAVA\n2. PYTHON\n>'))
        if Course == 1 :
            Course = 'JAVA'
        else:
            Course = 'PYTHON'

        mycursor.execute(f'SELECT * FROM Student_tb WHERE Course = "{Course}"\n')
        print()
        sql_print()
        continue_function()

    # This provides full details of all students
    elif choice == 5:
        print('\nListing Student\'s Deatails here...\n')
        print('(UID | SttID | FullName | Roll | Department | Batch | Course | Mark)')
        mycursor.execute(students_details)
        sql_print()
        continue_function()

    # This provides marks of all students
    elif choice ==  6:
        print('\nGrade of Students: ')
        students_marks()
        continue_function()

    # This provides Marks and reportCard of individual students
    elif choice == 7 :

        # if you have updated all students marks
        yes = input('Have You Updated Students Marks? (y/n) >')
        # if not updated
        if yes == 'n':
            print('First Update Marks And Come Back...') 
            examination() # jump to examination portal or update marks portal

        # Getting 
        print('\n')
        print(UID | StudentID | FullName)
        mycursor.execute(students_details)
        result = mycursor.fetchall()
        for x in result:
            print(x[global_uid], x[global_studentID], x[global_name])

        print('\nReport Card Generator...\n')
        uniID = int(input('Enter UID of student: '))
        Name, RollNo, Stream, StudentID, Subject, Marks, Grade = report_info(uniID)
        reportCard(Name, RollNo, Stream, StudentID, Subject, Marks, Grade, uniID)
        
        print('Report Card Generated at:-')
        print(os.getcwd() + fileName + f'{Name}ReportCard.txt')

        open_file(f'{Name}ReportCard.txt')
        continue_function()

    # Graph 
    elif choice == 8 :
        graph()
        
    # To exit program
    elif choice == 0 :
        pass

    else: 
        print('Please Choose options correctly')



print('Exiting Program...')

db.close()
