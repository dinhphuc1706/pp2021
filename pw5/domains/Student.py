
class Student():
    def __init__(self, id, name, Birthday):
        self.id = id
        self.name = name
        self.Birthday = Birthday
        
    def getStudentinfo(self):
        print("Student ID: " + self.id)
        print("Student Name: " + self.name)
        print("Student Birthday: " + self.Birthday)
        
    def setStudentinfo(self, id, name, Birthday):
        self.id = id
        self.name = name
        self.Birthday = Birthday

        
def createStudentList():
    for i in range(StudentCount):
        StudentList.append("s" + str(i))
        
def IsExistStudentName(name):
    for student in StudentList:
        if name == student.name:
            return True

