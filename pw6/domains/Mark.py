
from numpy import *
from math import *

class MarkTable():
    def __init__(self, StudentName, CourseName, Mark):
        self.StudentName = StudentName
        self.CourseName = CourseName
        self.Mark = Mark
    
    def getMarkinfo(self):
        print("Student Name: " + self.StudentName)
        print("Course Name: " + self.CourseName)
        print("Mark: " + str(self.Mark))
        
    def setMarkinfo(self, StudentName, CourseName, Mark):
        self.StudentName = StudentName
        self.CourseName = CourseName
        self.Mark = Mark
        
        
def createMarkList():
    global checkStudentName
    global checkCourseName
    checkStudentName = input("Choose Student: ")
    checkCourseName = input("Choose Course: ")
    if (IsExistStudentName(checkStudentName) and IsExistCourseName(checkCourseName)):
        MarkList.append("record" + str(index+1))
        print("Index: " + str(index))
    else:
        print("Not exist Student or Course")
        
def setMark():
    global index
    Mark = float(input("Mark: "))
    MarkList[index] = MarkTable(checkStudentName, checkCourseName, floor(Mark*10)/10)
    index += 1    
    
def AverageMark(name):
    MarkArray = []
    for i in range(len(MarkList)):
        if name == MarkList[i].StudentName:
            MarkArray.append(MarkList[i].Mark)
    SumArray = array(MarkArray)
    AverageMark = average(SumArray)
    print("Average Mark of " + name + " is: " + str(AverageMark))

