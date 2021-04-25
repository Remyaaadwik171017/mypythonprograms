class Employee:
    company_name="LT"
    def emp(self,emid,emname,emsalary):
        self.emid=emid
        self.emname=emname
        self.emsalary=emsalary
    def printdetails(self):
        print(self.emid)
        print(self.emname)
        print(self.emsalary)
    def __str__(self):
        return str(self.emid)
ob=Employee()
ob.emp(20,"Aadwik",200000)
print(ob)