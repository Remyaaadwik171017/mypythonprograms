class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printval(self):
        print("name:",self.name)
        print("roll no:", self.rollno)
        print("course:",self.course)
        print("mark:",self.mark)

f=open("student","r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=int(data[3])
    ob=Student(name,rollno,course,mark)
    if (mark == 200):
        ob.printval()
