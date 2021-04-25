class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print("name: ",self.name)
        print("age:",self.age)
obj=Person("ram",25)
obj.printvalue()