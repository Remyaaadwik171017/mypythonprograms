#two string method
class College:
    college_name="LT"
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def printval(self):
        print("college name:",self.college_name)
        print("Name:",name)
        print("roll no:",rollno)
    def __str__(self):
        return self.name+ str(self.rollno)
c=College(3,"Ajith")
print(c)
