class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print("name: ",self.name)
        print("age:",self.age)
obj=Person()
obj.setvalue("ram",23)
obj.printvalue()