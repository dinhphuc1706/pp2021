
from domains.Student import *
from domains.Course import *
from domains.Mark import *
from math import *
from numpy import *

StudentList = []
CourseList = []
MarkList = []

def RecordCount():
    global RecordCount
    RecordCount = int(input("Enter Record: "))

def StudentCount():
    global StudentCount
    StudentCount = int(input("How many student are there? "))
    
def CourseCount():
    global CourseCount
    CourseCount = int(input("How many course are there in the semester ? "))
    
    
def setStudent():
    print("Input Student Information: ")
    for i in range(StudentCount):
        student_id = input("Enter Student Id: ")
        student_name = input("Enter Student Name: ")
        student_birthday = input("Enter Student Date of Birth: ")
        StudentList[i] = Student(student_id, student_name, student_birthday)
        
def setCourse():
    print("Input Course Information: ")
    for i in range(CourseCount):
        course_id = input("Enter Course Id: ")
        course_name = input("Enter Course name: ")
        CourseList[i] = Course(course_id, course_name)
        

