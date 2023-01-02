
# Project Title

A simple command line based program for College Student Managements.
This Program is mostly written in Python as well as sql.
Used python for the logic purpose and sql for Database to store all details of students.

## 1. Installing Mysql

##### To Install in windows follow this link :-
```bash
https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.31.0.msi
    
set username = root
set password = admin
```
## 2. Installing requirements.txt

This command will install all the dependencies
```bash
python install -r requirements.txt
```
## 3. How To Run

```bash
# Just For Help File...
python Help.py

# This File Will Create A DataBase
python CreateDataBase.py

# This File Will Create Student_tb Table
python CreateStudent_tb.py

# Here All Commands Are Listed To Manage Students
python StudentManager.py
```


## 4. Preview

![Options](https://user-images.githubusercontent.com/121259738/210237865-c5bdd61f-b0f3-42e1-8a28-6c9602dec9b9.png)

- Select 1 > To register new student information
- Select 2 > To update new student's mark
- Select 3 > To filter student using their department
- Select 4 > To filter student using their course
- Select 5 > To get full information of all students
- Select 6 > To get mark of all students 
- Select 7 > To get report card of perticular student
- Select 8 > To get graphical analysis of all student's mark
- Select 0 > To exit progra
