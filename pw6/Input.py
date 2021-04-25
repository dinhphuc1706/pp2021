from zipfile import ZipFile
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
        

def FileWriter():
    #Create file Students.txt
    StudentWriter = open("Students.txt", "a")
    pickle.dump(StudentList,StudentWriter)
    StudentWriter.close()
    
    #Create  file Courses.txt
    CourseWriter = open("Courses.txt", "a")
    pickle.dump(CourseList,CourseWriter)
    CourseWriter.close()
    
    #Create file Mark.txt
    MarkWriter = open("Marks.txt", "a")
    pickle.dump(MarkList,MarkWriter)
    MarkWriter.close()
    
    #open and read the file after the appending:
    f1 = open("students.txt", "r")
    newStudent_dict = pickle.load(f1)
    f1.close()
    f2 = open("courses.txt", "r")
    newCourse_dict = pickle.load(f2)
    f2.close()
    f3 = open("marks.txt", "r")
    newMark_dict = pickle.load(f3)
    f3.close()

    #Compress Multi File
    zipObj = ZipFile('students.dat', 'w')
    pickle.dump(StudentList,zipObj)
    pickle.dump(CourseeList,zipObj)
    pickle.dump(MarkList,zipObj)
    zipObj.close()
    
#Decompress
def FileDecompresser():    
    try:
        f = open("students.dat")
        with ZipFile('students.dat', 'r') as zipObj:
        zipObj.extractall('Decompressed File')
        #load data
        StudentWriter = open("Students.txt", "a")
        print(StudentWriter.read())
        CourseWriter = open("Courses.txt", "a")
        print(CourseWriter.read())
        MarkWriter.read()) = open("Marks.txt", "a")
        print(MarkWriter.read())
    except IOError:
        print("File not exits")
    finally:
        f.close()
    
    
    
    