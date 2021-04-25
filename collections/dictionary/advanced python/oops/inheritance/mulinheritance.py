#multiple inheritance

class Parent:
    parentname="Arun"
    def m1(self,age):
        self.age=age
        print("my name is ",Parent.parentname)
class Mom:
    def m2(self,name):
        self.name=name
        print("My name is",self.name)
        print("my husband name",Parent.parentname)
class Child(Parent,Mom):
    def m3(self,age1):
        self.age1=age1
        print("my father name is",Parent.parentname)
        print("My mom's name is", self.name)
        print("My father name",self.age)
        print("child age",self.age1)
obj=Child()
obj.m1(23)
obj.m2("Resmi")
obj.m3(3)