class Employee:
    cname="Luminar Technolab"
    def setvalue(self,id,empname,salary,profession):
        self.id=id
        self.empname=empname
        self.salary=salary
        self.profession=profession
    def printvalue(self):
        print(Employee.cname,",id: ",self.id,",employee name: ",self.empname,",salary: ",self.salary,",profession: ",self.profession)
obj=Employee()
obj.setvalue(1001,"Remya",15000,"Developer")
obj.printvalue()

obj1=Employee()
obj1.setvalue(1002,"Arun",20000,"network enggr")
obj1.printvalue()