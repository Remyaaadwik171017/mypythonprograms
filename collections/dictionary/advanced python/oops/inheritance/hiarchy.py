#multilevel inheritance/hiarchial inheritance

class Parent:
    parentname="Ajith"
    def m1(self,age):
        self.age=age
        print("I am father of adwik.my name is ",Parent.parentname)
class Mom(Parent):
    def m2(self,name):
        self.name=name
        print("I am",self.name,"mother of Aadwik")
        print("my husband name",Parent.parentname)
class Child(Mom):
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

a=Mom()
a.m1(23)
a.m2("Remya")