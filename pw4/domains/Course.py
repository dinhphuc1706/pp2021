
class Course():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def getCourseinfo(self):
        print("Course ID: " + self.id)
        print("Course Name: " + self.name)
        
    def setCourseinfo(self, id, name):
        self.id = id
        self.name = name
        
        
def createCourseList():
    for i in range(CourseCount):
        CourseList.append("s" + str(i))
        
def IsExistCourseName(name):
    for course in CourseList:
        if name == course.name:
            return True

