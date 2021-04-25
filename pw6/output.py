
from domains.Student import *
from domains.Course import *
from domains.Mark import *
from math import *
from numpy import *


def PrintStudentList():
    for i in range(StudentCount):
        StudentList[i].getStudentinfo()
        
def PrintCourseList():
    for i in range(CourseCount):
        CourseList[i].getCourseinfo()
        
def PrintMarkList():
    for i in range(len(MarkList)):
        MarkList[i].getMarkinfo()
        
def getAverageMark():
    Temp= input("Average Mark of Student name: ")
    AverageMark(Temp)

