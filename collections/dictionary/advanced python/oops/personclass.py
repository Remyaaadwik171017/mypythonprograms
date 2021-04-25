class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print("name: ",self.name)
        print("age:",self.age)
class Student(Person):
    def __init__(self,roll_no,marks,name,age):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.marks=marks
    def print(self):
        print("roll no :",self.roll_no)
        print("mark:",self.marks)

obj=Student(2,45,"ram",25)
obj.printvalue()
obj.print()