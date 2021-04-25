class Parent:
    def Properties(self):
        print("10 lack rs,2 car")

    def marry(self):
        print("with Ram")
class Child(Parent):
    def marry(self):
        print("with arun")
a=Child()
a.marry()