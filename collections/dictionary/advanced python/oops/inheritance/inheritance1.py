class Parent:
    parentname="Arun"
    def m1(self,age):
        self.age=age
        print("my name is ",Parent.parentname)
class Child(Parent):
    def m2(self,age1):
        self.age1=age1
        print("my father name is",Parent.parentname)
        print("My father name",self.age)
        print(self.age1)
obj=Child()
obj.m1(23)
obj.m2(3)