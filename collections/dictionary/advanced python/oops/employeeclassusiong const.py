class Employee:
    cname="Luminar Technolab"
    def __init__(self,id,empname,salary,profession):
        self.id=id
        self.empname=empname
        self.salary=salary
        self.profession=profession
    def printvalue(self):
        print(Employee.cname,",id: ",self.id,",employee name: ",self.empname,",salary: ",self.salary,",profession: ",self.profession)
obj=Employee(1001,"Remya",15000,"Developer")
obj.printvalue()

obj1=Employee(1002,"Arun",20000,"network enggr")
obj1.printvalue()