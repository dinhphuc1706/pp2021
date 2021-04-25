
from domains.Student import *
from domains.Course import *
from domains.Mark import *

#main
index = 0
StudentCount()
createStudentList()
setStudent()
PrintStudentList()

print("\n")
CourseCount()
createCourseList()
setCourse()
PrintCourseList()

print("\n")
RecordCount()
for i in range(RecordCount):
    createMarkList()
    setMark()
PrintMarkList()
getAverageMark()

